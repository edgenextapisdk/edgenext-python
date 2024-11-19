## 单元测试
import os
import pytest
import logging
from edgenextapisdk import Sdk

class TestSdk:

    def initSdk(self):
        # Set the AK/SK to sign and authenticate the request.
        # 认证用的ak和sk硬编码到代码中或者明文存储都有很大的安全风险，建议在配置文件或者环境变量中密文存放，使用时解密，确保安全；
        # 本示例以ak和sk保存在环境变量中为例，运行本示例前请先在本地环境中设置环境变量ENV_APP_ID和ENV_APP_SECERT。
        self.sdk = Sdk({
            "app_id": os.getenv('ENV_APP_ID'),
            "app_secert": os.getenv('ENV_APP_SECERT'),
            "api_pre": "http://127.0.0.1:60041/api/V4/",
            "timeout": 30,
        })
        self._queryKey = "domain"
        self._query = {self._queryKey: 101153}
        self._postKey = "name"
        self._post = {self._postKey: 'tester'}

    def test_get(self):
        self.initSdk()
        api = 'Web.Domain.Info'

        raw, body, err = self.sdk.get(api, self._query)
        print(raw)
        print(body)
        print(err)
        assert body['status']['code'] == 1
        assert body['data'][self._queryKey] == self._query[self._queryKey]

    def test_put(self):
        self.initSdk()
        api = 'test.sdk.put'

        raw, body, err = self.sdk.put(api, self._query, self._post)
        assert body['status']['code'] == 1
        assert body['data'][self._queryKey] == self._query[self._queryKey]
        assert body['data'][self._postKey] == self._post[self._postKey]

        raw, body, err = self.sdk.post(api, self._query, self._post)
        logging.info(api)
        logging.info("raw: " + raw)
        logging.info("err: " + err)
        assert body['status']['code'] == 2

    def test_post(self):
        self.initSdk()
        postData = {
            "domains": ["www.baidu.com"],
            "group_id": 0,
            "biz_type": 1,  ## 这个真的需要吗？1网页 2直播-推流 3直播-拉流
            "sets": [
                {
                    "protocol": 0,  ## 协议: 0http 1https
                    "listen_port": 80,  ## 这个真的需要吗？监听端口，多个用逗号(,)分割
                    "get_source_protocol": 0,  ## 取源协议: 0HTTP 1HTTPS 2协议跟随
                    "load_balance": 1,  ## 负载均衡方式: 0IP哈希 1轮询 2COOKIE粘住
                    "back_source_type": 1,  ## 回源类型：0IP 1域名
                    "source_ips": [
                        {
                            "value": "www.google.com",
                            "port": "80",
                            "view": "primary",  ## 线路类别，primary 主线路 backup 备线路
                            "priority": 1,  ## 回源权重
                            "type": "CNAME"  ## 这个真的需要吗？type值为A/CNAME，对应的是DNS记录类型
                        }
                    ]
                }
            ]
        }
        print(postData)
        # 调用sdk更新scdn配置
        raw, json_data, err = self.sdk.post(
            "Web.Domain.batch.domain.add",
            postData=postData,
            query={}
        )
        print(raw)
        print(json_data)
        print(err)

    def test_patch(self):
        self.initSdk()
        api = 'test.sdk.patch'

        raw, body, err = self.sdk.patch(api, self._query, self._post)
        assert body['status']['code'] == 1
        assert body['data'][self._queryKey] == self._query[self._queryKey]
        assert body['data'][self._postKey] == self._post[self._postKey]

        raw, body, err = self.sdk.post(api, self._query, self._post)
        logging.info(api)
        logging.info("raw: " + raw)
        logging.info("err: " + err)
        assert body['status']['code'] == 2

    def test_delete(self):
        self.initSdk()
        api = 'test.sdk.delete'

        raw, body, err = self.sdk.delete(api, self._query, self._post)
        assert body['status']['code'] == 1
        assert body['data'][self._queryKey] == self._query[self._queryKey]
        assert body['data'][self._postKey] == self._post[self._postKey]

        raw, body, err = self.sdk.post(api, self._query, self._post)
        logging.info(api)
        logging.info("raw: " + raw)
        logging.info("err: " + err)
        assert body['status']['code'] == 2

    def test_domain_set_save(self):
        self.initSdk()
        ## 602 为签名失败，此处仅验证深度数据排序时的问题
        api = 'web.domain.set.save'
        postData = {"domain_id":"233707","group":{"domain_proxy_conf":{"max_fails":"300","fails_timeout":10,"keep_new_src_time":30,"proxy_keepalive":0,"proxy_connect_timeout":30,"s":"/v5manage/webcdndomain/saveProxyConf"}}}
        raw, body, err = self.sdk.put(api, self._query, postData)
        logging.info(api)
        logging.info("raw: " + raw)
        logging.info("err: " + err)
        assert body['status']['code'] != 602