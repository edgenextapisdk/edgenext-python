import sys
import types
import unittest

# The package imports requests in __init__.py. These tests exercise only the
# generated wrapper layer, so a module stub keeps them dependency-free.
sys.modules.setdefault("requests", types.ModuleType("requests"))

from edgenextapisdk.client import EdgeNextClient, _api_path_to_sdk_api
from edgenextapisdk.requests import AddDomainsRequest, ListDomainsRequest, UpdateDomainsRequest


class FakeSdk:
    def __init__(self, api_pre="https://api.edgenextscdn.com/api/v5"):
        self._apiPre = api_pre
        self.calls = []

    def get(self, api, query=None, headers=None):
        self.calls.append(("GET", api, query, None, headers))
        return "", {"ok": True}, ""

    def post(self, api, query=None, postData=None, headers=None):
        self.calls.append(("POST", api, query, postData, headers))
        return "", {"ok": True}, ""

    def put(self, api, query=None, postData=None, headers=None):
        self.calls.append(("PUT", api, query, postData, headers))
        return "", {"ok": True}, ""

    def patch(self, api, query=None, postData=None, headers=None):
        self.calls.append(("PATCH", api, query, postData, headers))
        return "", {"ok": True}, ""

    def delete(self, api, query=None, postData=None, headers=None):
        self.calls.append(("DELETE", api, query, postData, headers))
        return "", {"ok": True}, ""


class TestEdgeNextClient(unittest.TestCase):
    def test_api_path_to_sdk_api_handles_api_pre_prefixes(self):
        self.assertEqual(
            _api_path_to_sdk_api("/api/v5/domains", "https://api.edgenextscdn.com/api/v5"),
            "domains",
        )
        self.assertEqual(
            _api_path_to_sdk_api("/api/v5/domains", "https://api.edgenextscdn.com"),
            "api/v5/domains",
        )
        self.assertEqual(
            _api_path_to_sdk_api("api/v5/Web.ca.self.list", "https://api.edgenextscdn.com/api"),
            "v5/Web.ca.self.list",
        )

    def test_generated_get_method_routes_to_query(self):
        sdk = FakeSdk()
        client = EdgeNextClient(sdk)
        raw, body, err = client.list_domains(query={"page": 1}, headers={"X-Lang": "en"})

        self.assertEqual(body, {"ok": True})
        self.assertEqual(err, "")
        self.assertEqual(sdk.calls, [("GET", "domains", {"page": 1}, None, {"X-Lang": "en"})])

    def test_generated_get_method_accepts_request_object(self):
        sdk = FakeSdk()
        client = EdgeNextClient(sdk)
        request = ListDomainsRequest(page=1, page_size=20, headers={"X-Lang": "en"})
        client.list_domains(request)

        self.assertEqual(
            sdk.calls,
            [("GET", "domains", {"page": 1, "page_size": 20}, None, {"X-Lang": "en"})],
        )

    def test_generated_post_method_routes_to_body(self):
        sdk = FakeSdk()
        client = EdgeNextClient(sdk)
        client.add_domains(body={"domain": "example.com"})

        self.assertEqual(sdk.calls, [("POST", "domains", {}, {"domain": "example.com"}, {})])

    def test_generated_post_method_accepts_request_object(self):
        sdk = FakeSdk()
        client = EdgeNextClient(sdk)
        request = AddDomainsRequest(domain="example.com", group_id=1)
        client.add_domains(request)

        self.assertEqual(sdk.calls, [("POST", "domains", {}, {"domain": "example.com", "group_id": 1}, {})])

    def test_generated_post_method_keeps_dict_body_compatibility(self):
        sdk = FakeSdk()
        client = EdgeNextClient(sdk)
        client.add_domains({"domain": "example.com"})

        self.assertEqual(sdk.calls, [("POST", "domains", {}, {"domain": "example.com"}, {})])

    def test_wrong_request_object_is_rejected(self):
        client = EdgeNextClient(FakeSdk())
        with self.assertRaises(ValueError):
            client.add_domains(UpdateDomainsRequest(domain_id=123))

    def test_call_api_accepts_documented_api_name(self):
        sdk = FakeSdk()
        client = EdgeNextClient(sdk)
        client.call_api("ListDomains", request=ListDomainsRequest(page_size=20))

        self.assertEqual(sdk.calls[0][:3], ("GET", "domains", {"page_size": 20}))

    def test_multi_method_endpoint_can_override_method(self):
        sdk = FakeSdk()
        client = EdgeNextClient(sdk)
        client.log_download_task_task_list(method="GET", query={"page": 1})

        self.assertEqual(sdk.calls, [("GET", "soc.log.download.task.list", {"page": 1}, None, {})])

    def test_invalid_method_override_is_rejected(self):
        client = EdgeNextClient(FakeSdk())
        with self.assertRaises(ValueError):
            client.list_domains(method="POST")


if __name__ == "__main__":
    unittest.main()
