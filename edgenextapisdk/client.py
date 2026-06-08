"""Convenience method wrapper for EdgeNext API endpoints."""

import re
from urllib.parse import urlparse

from edgenextapisdk.apis import API_DEFINITIONS
from edgenextapisdk.requests import BaseRequest


_HTTP_METHODS = {"GET", "POST", "PUT", "PATCH", "DELETE"}


def _api_path_to_sdk_api(path, api_pre=None):
    """Convert a documented API path to the relative path Sdk._payload expects.

    If api_pre already contains an API prefix such as /api/v5, return only the
    endpoint path. If api_pre is just the host, keep api/v5 in the route.
    """
    path = re.sub(r"^/+", "", path.strip())
    api_pre_path = urlparse(api_pre or "").path.strip("/").lower()
    if re.search(r"(^|/)api/v[0-9]+$", api_pre_path):
        return re.sub(r"^api/v[0-9]+/", "", path, flags=re.IGNORECASE)
    if re.search(r"(^|/)api$", api_pre_path):
        return re.sub(r"^api/", "", path, flags=re.IGNORECASE)
    return path


class EdgeNextClient:
    """Typed-ish convenience client built on top of the authenticated Sdk.

    The base Sdk still handles signing, headers, request transport, and response
    parsing. This wrapper only maps documented API names to HTTP methods and
    routes, so callers do not need to remember route strings.

    Each generated endpoint method accepts the same common arguments:
        request: an endpoint-specific BaseRequest object, for example AddDomainsRequest
        query: query string parameters
        body: JSON request body for non-GET requests
        headers: extra request headers
        method: optional override for endpoints documented with multiple methods

    Generated endpoint methods return the parsed API response body directly.
    Transport, parse, and business errors are raised as APIError.
    """

    def __init__(self, sdk, default_headers=None):
        self.sdk = sdk
        self.default_headers = dict(default_headers or {})

    @classmethod
    def from_config(cls, params=None, oldSign=False, default_headers=None):
        from edgenextapisdk import Sdk

        return cls(Sdk(params or {}, oldSign=oldSign), default_headers=default_headers)

    def set_default_header(self, key, value):
        self.default_headers[key] = value
        return self

    def set_language(self, lang):
        return self.set_default_header("X-Lang", lang)

    @property
    def api_definitions(self):
        return API_DEFINITIONS

    def call_api(self, api_name, request=None, query=None, body=None, headers=None, method=None):
        """Call an API by its documented @apiName value."""
        definition = self.get_api_definition(api_name)
        return self._request(
            definition,
            request=request,
            query=query,
            body=body,
            headers=headers,
            method=method,
        )

    def get_api_definition(self, api_name):
        for definition in API_DEFINITIONS:
            if definition["api_name"] == api_name or definition["method_name"] == api_name:
                return definition
        raise KeyError("unknown EdgeNext API: %s" % api_name)

    def _request(self, definition, request=None, query=None, body=None, headers=None, method=None):
        methods = definition["methods"]
        selected = (method or methods[0]).upper()
        if selected not in _HTTP_METHODS:
            raise ValueError("unsupported HTTP method: %s" % selected)
        if selected not in methods:
            raise ValueError(
                "%s does not support %s; supported methods: %s"
                % (definition["api_name"], selected, ", ".join(methods))
            )

        query = query or {}
        body = body or {}
        explicit_headers = headers or {}
        headers = dict(self.default_headers)
        if isinstance(request, BaseRequest):
            if request.API_NAME and request.API_NAME != definition["api_name"]:
                raise ValueError(
                    "request %s cannot be used for API %s"
                    % (request.API_NAME, definition["api_name"])
                )
            request_query, request_body, request_headers = request.to_request_parts()
            query = dict(request_query, **query)
            body = dict(request_body, **body)
            headers = dict(headers, **request_headers)
            if method is None and request.METHOD:
                selected = request.METHOD.upper()
        elif request is not None:
            if selected == "GET":
                query = dict(request, **query)
            else:
                body = dict(request, **body)
        headers = dict(headers, **explicit_headers)

        api = _api_path_to_sdk_api(definition["path"], getattr(self.sdk, "_apiPre", ""))
        if selected == "GET":
            if body:
                query = dict(body, **query)
            return self._call_sdk(self.sdk.get, api, query=query, headers=headers)
        if selected == "POST":
            return self._call_sdk(self.sdk.post, api, query=query, postData=body, headers=headers)
        if selected == "PUT":
            return self._call_sdk(self.sdk.put, api, query=query, postData=body, headers=headers)
        if selected == "PATCH":
            return self._call_sdk(self.sdk.patch, api, query=query, postData=body, headers=headers)
        if selected == "DELETE":
            return self._call_sdk(self.sdk.delete, api, query=query, postData=body, headers=headers)
        raise ValueError("unsupported HTTP method: %s" % selected)


    def _call_sdk(self, fn, *args, **kwargs):
        raw, body, err = fn(*args, **kwargs)
        if err:
            raise APIError(message=err, response=body, raw=raw)
        status = body.get("status") if isinstance(body, dict) else None
        code = status.get("code") if isinstance(status, dict) else None
        message = status.get("message") if isinstance(status, dict) else ""
        if code is not None and code != 1:
            raise APIError(code=code, message=message, response=body, raw=raw)
        return body


class APIError(Exception):
    """Error raised by the generated EdgeNext wrapper client."""

    def __init__(self, code=None, message="", response=None, raw=""):
        self.code = code
        self.message = message or "api error"
        self.response = response
        self.raw = raw
        if code is None:
            super().__init__(self.message)
        else:
            super().__init__("%s (code: %s)" % (self.message, code))


def _make_endpoint_method(definition):
    def endpoint(self, request=None, query=None, body=None, headers=None, method=None):
        return self._request(
            definition,
            request=request,
            query=query,
            body=body,
            headers=headers,
            method=method,
        )

    endpoint.__name__ = definition["method_name"]
    endpoint.__qualname__ = "EdgeNextClient.%s" % definition["method_name"]
    endpoint.__doc__ = "%s: %s %s" % (
        definition["api_name"],
        "/".join(definition["methods"]),
        definition["path"],
    )
    return endpoint


for _definition in API_DEFINITIONS:
    setattr(EdgeNextClient, _definition["method_name"], _make_endpoint_method(_definition))


__all__ = ["EdgeNextClient", "APIError"]
