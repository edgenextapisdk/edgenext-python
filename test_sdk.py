## 单元测试
import os
import pytest
import logging
from edgenextapisdk import Sdk

class TestSdk:

    def initSdk(self):
        self.sdk = Sdk({
            "app_id": os.environ['SDK_APP_ID'],
            "app_secert": os.environ['SDK_APP_SECERT'],
            "api_pre": os.environ['SDK_API_PRE'],
            "timeout": 30,
        })
        self._queryKey = "id"
        self._query = {self._queryKey: '1'}
        self._postKey = "name"
        self._post = {self._postKey: 'tester'}

    def test_get(self):
        self.initSdk()
        api = 'test.sdk.get'

        raw, body, err = self.sdk.get(api, self._query)
        assert body['status']['code'] == 1
        assert body['data'][self._queryKey] == self._query[self._queryKey]

        raw, body, err = self.sdk.post(api, self._query)
        logging.info(api)
        logging.info("raw: " + raw)
        logging.info("err: " + err)
        assert body['status']['code'] == 2

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
        api = 'test.sdk.post'

        raw, body, err = self.sdk.post(api, self._query, self._post)
        assert body['status']['code'] == 1
        assert body['data'][self._queryKey] == self._query[self._queryKey]
        assert body['data'][self._postKey] == self._post[self._postKey]

        raw, body, err = self.sdk.put(api, self._query, self._post)
        logging.info(api)
        logging.info("raw: " + raw)
        logging.info("err: " + err)
        assert body['status']['code'] == 2

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

