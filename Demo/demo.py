from edgenextapisdk import Sdk

if __name__ == '__main__':
    sdk = Sdk({
        "app_id": "ENAK195892d9c30371985983",
        "app_secert": "57dbcb07eb4e1d5aa531afee2c4d8f26",
        "api_pre": "http://127.0.0.1:60041/api/V4/",
        "timeout": 30,
    })
    raw, body, err = sdk.get("Web.Domain.Info", {"domain": 101153})
    print(raw)
    print(body)
    print(err)