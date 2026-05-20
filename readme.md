# EdgeNext API SDK for Python

A Python SDK for interacting with the EdgeNext API, providing a simple and secure way to make authenticated API requests.

## Description

* **Base URL**: The API base URL (e.g., `https://api.local.com/V4/`). Please consult with operations staff for the specific URL.
* **API Style**: RESTful API, default request body is JSON, default response is JSON.
* **Authentication**: Contact technical support to register an account and apply for API credentials (`app_id` and `app_secret`).

## Signature Algorithm

* Every request must be signed to ensure data integrity during transmission.
* **Client**: Uses SHA256 signature algorithm. Parameters are base64 encoded and signed with `app_secret` using SHA256. Each request includes the signature.
* **Server**: Uses the same algorithm to sign the parameters and verifies the signature.

## SDK Usage

### Requirements

* Python >= 3.8
* Supports GET, POST, PATCH, PUT, DELETE methods

### Parameters

* `app_id`: Your assigned app_id
* `app_secret`: Your assigned app_secret, used for signing data
* `api_pre`: API prefix (base URL)
* `timeout`: Request timeout in seconds (default: 10 seconds). Please set appropriately.

### Return Values

Each method call returns three values: `(raw_string, parsed_json_dict, error_string)`

### Important Notes

For all requests, the URI and GET parameters are separated. For example, for `https://api.local.com/V4/version?v=1`, the `v=1` parameter must be passed via the `query` parameter:

```python
raw, body, err = sdk.get('version', query={'v': 1})
```

## Installation

```bash
pip install edgenextapisdk
```

## Usage

### Initialize SDK

```python
import os
import logging
from edgenextapisdk import Sdk

# Setup logging
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

# Log to file
fileHandle = logging.FileHandler('/tmp/sdk.log', encoding='utf-8')
fileHandle.setFormatter(formatter)
logger.addHandler(fileHandle)

# Log to stdout
streamHandle = logging.StreamHandler()
streamHandle.setFormatter(formatter)
logger.addHandler(streamHandle)

sdk = Sdk({
    "app_id": os.environ['SDK_APP_ID'],                # Replace with your actual value in production
    "app_secert": os.environ['SDK_APP_SECERT'],        # Replace with your actual value in production
    "api_pre": os.environ['SDK_API_PRE'],              # Replace with your actual value in production
    "timeout": 30,
    "logger": logger,                                   # Optional: omit if logging is not needed
})
```

### EdgeNext API Method Wrapper

The SDK also provides `EdgeNextClient`, which wraps documented EdgeNext V5 APIs as Python methods. The old low-level `Sdk.get/post/put/delete/patch` calls are still available.

```python
import os
from edgenextapisdk import EdgeNextClient

client = EdgeNextClient.from_config({
    "app_id": os.environ["SDK_APP_ID"],
    "app_secert": os.environ["SDK_APP_SECERT"],
    "api_pre": os.environ["SDK_API_PRE"],
    "timeout": 30,
})

raw, body, err = client.list_domains(
    query={"page": 1, "page_size": 20},
    headers={"X-Lang": "en"},
)

raw, body, err = client.add_domains(
    body={"domain": "www.example.com"},
    headers={"X-Lang": "en"},
)
```

Generated method names are snake_case versions of the API document `@apiName`, for example `ListDomains` becomes `list_domains` and `AddDomains` becomes `add_domains`. Every method accepts `query`, `body`, `headers`, and optional `method` for APIs documented with multiple HTTP methods. You can also call by the original API name:

```python
raw, body, err = client.call_api("ListDomains", query={"page": 1})
```

### GET Request

```python
api = 'test.sdk.get'
query = {
    "page": 1,
    "pagesize": 10,
    "data": {
        "name": "name名称",
        "domain": "baidu.com",
    }
}
raw, jsonData, err = sdk.get(api, query=query)
print("api: ", api)
print("raw: ", raw)
print("jsonData: ", jsonData)
print("err: ", err)
```

### POST Request

```python
api = 'test.sdk.post'
query = {}
postData = {
    "name": 1,
    "age": 10,
    "data": {
        "name": "name",
        "domain": "baidu.com",
    }
}
raw, jsonData, err = sdk.post(api, postData=postData, query=query)
print("api: ", api)
print("raw: ", raw)
print("jsonData: ", jsonData)
print("err: ", err)
```

### PATCH Request

```python
api = 'test.sdk.patch'
query = {}
postData = {
    "name": 1,
    "age": 10,
    "data": {
        "name": "name",
        "domain": "baidu.com",
    }
}
raw, jsonData, err = sdk.patch(api, postData=postData, query=query)
print("api: ", api)
print("raw: ", raw)
print("jsonData: ", jsonData)
print("err: ", err)
```

### PUT Request

```python
api = 'test.sdk.put'
query = {}
postData = {
    "name": 1,
    "age": 10,
    "data": {
        "name": "name",
        "domain": "baidu.com",
    }
}
raw, jsonData, err = sdk.put(api, postData=postData, query=query)
print("api: ", api)
print("raw: ", raw)
print("jsonData: ", jsonData)
print("err: ", err)
```

### DELETE Request

```python
api = 'test.sdk.delete'
query = {}
postData = {
    "name": 1,
    "age": 10,
    "data": {
        "name": "name",
        "domain": "baidu.com",
    }
}
raw, jsonData, err = sdk.delete(api, postData=postData, query=query)
print("api: ", api)
print("raw: ", raw)
print("jsonData: ", jsonData)
print("err: ", err)
```

## Changelog
