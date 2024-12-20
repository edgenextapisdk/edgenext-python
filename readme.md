# api sdk for python

### 说明

* 接口基地址，如 https://api.local.com/V4/ ，具体请咨询运营人员
* 接口遵循RESTful,默认请求体json,接口默认返回json
* app_id, app_secret 联系技术客服，先注册一个的账号，用于申请绑定api身份

### 签名算法

* 每次请求都签名，保证传输过程数据不被篡改
* 客户端：sha256签名算法，将参数base64编码+app_secret用sha256签名，每次请求带上签名
* 服务端：拿到参数用相同的算法签名，对比签名是否正确

### sdk 使用说明

* 环境：python >=3.5
* 支持get/post/patch/put/delete方法
* 参数说明
    * app_id 分配的app_id
    * app_secert 分配的app_secert, 用于签名数据
    * api_pre api前缀
    * timeout 请求超时时间，默认10秒，请合理设置
* 每次调用会返回三个参数：(原始字符串，解析后的json字典，错误字符串)
* 注意事项
    针对所有请求，uri与get参数是分离的，如 https://api.local.com/V4/version?v=1, 调用时v=1参数，须通过query传递
        raw, body, err = sdk.get('version', query={'v': 1})

### 安装

pip install edgenextapisdk

### 使用

```
### 实例化 Sdk
import os
import logging
from edgenextapisdk import Sdk

## 添加日志
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

##日志输出到文件
fileHandle = logging.FileHandler('/tmp/sdk.log', encoding='utf-8')
fileHandle.setFormatter(formatter)
logger.addHandler(fileHandle)

##日志输出到stdout
streamHandle = logging.StreamHandler()
streamHandle.setFormatter(formatter)
logger.addHandler(streamHandle)

sdk = Sdk({
    "app_id": os.environ['SDK_APP_ID'],                ## 业务上使用时，替换为具体的值
    "app_secert": os.environ['SDK_APP_SECERT'],        ## 业务上使用时，替换为具体的值
    "api_pre": os.environ['SDK_API_PRE'],              ## 业务上使用时，替换为具体的值
    "timeout": 30,
    "logger": logger,               ##如果不需要，此参数可不传
})

### get 方式请求数据
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
print("")

### post 方式请求数据
api = 'test.sdk.post'
query    = {}
postData = {
    "name": 1,
    "age": 10,
    "data": {
        "name": "name名称",
        "domain": "baidu.com",
    }
}
raw, jsonData, err = sdk.post(api, postData = postData, query=query)
print("api: ", api)
print("raw: ", raw)
print("jsonData: ", jsonData)
print("err: ", err)
print("")

### patch 方式请求数据
api = 'test.sdk.patch'
query    = {}
postData = {
    "name": 1,
    "age": 10,
    "data": {
        "name": "name名称",
        "domain": "baidu.com",
    }
}
raw, jsonData, err = sdk.patch(api, postData = postData, query=query)
print("api: ", api)
print("raw: ", raw)
print("jsonData: ", jsonData)
print("err: ", err)
print("")

### put 方式请求数据
api = 'test.sdk.put'
query    = {}
postData = {
    "name": 1,
    "age": 10,
    "data": {
        "name": "name名称",
        "domain": "baidu.com",
    }
}
raw, jsonData, err = sdk.put(api, postData = postData, query=query)
print("api: ", api)
print("raw: ", raw)
print("jsonData: ", jsonData)
print("err: ", err)
print("")

### delete 方式请求数据
api = 'test.sdk.delete'
query    = {}
postData = {
    "name": 1,
    "age": 10,
    "data": {
        "name": "name名称",
        "domain": "baidu.com",
    }
}
raw, jsonData, err = sdk.delete(api, postData = postData, query=query)
print("api: ", api)
print("raw: ", raw)
print("jsonData: ", jsonData)
print("err: ", err)
print("")
```

### 更新日志

* 2022.11.09 

完成python版SDK开发
