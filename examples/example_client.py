import os

from edgenextapisdk import AddDomainsRequest, EdgeNextClient, ListDomainsRequest


client = EdgeNextClient.from_config({
    "app_id": os.environ["SDK_APP_ID"],
    "app_secert": os.environ["SDK_APP_SECERT"],
    "api_pre": os.environ["SDK_API_PRE"],
    "timeout": 30,
})

raw, body, err = client.list_domains(ListDomainsRequest(
    page=1,
    page_size=20,
    headers={"X-Lang": "en"},
))
print(raw, body, err)

raw, body, err = client.add_domains(AddDomainsRequest(
    domain="www.example.com",
    group_id=0,
    origins=[{
        "protocol": 0,
        "listen_ports": [80],
        "origin_protocol": 0,
        "load_balance": 1,
        "origin_type": 1,
        "records": [{
            "view": "primary",
            "value": "origin.example.com",
            "port": 80,
            "priority": 1,
        }],
    }],
    protect_status="scdn",
    headers={"X-Lang": "en"},
))
print(raw, body, err)

# Low-level dict calls remain supported for compatibility.
raw, body, err = client.call_api("ListDomains", query={"page": 1})
print(raw, body, err)
