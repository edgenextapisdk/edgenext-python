"""Request models for generated EdgeNext V5 API methods."""

_UNSET = object()


class BaseRequest:
    """Base request object. Subclasses define API_NAME, METHOD, PATH, and PARAMS."""

    API_NAME = ""
    METHOD = ""
    METHODS = ()
    PATH = ""
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None):
        self.query = dict(query or {})
        self.body = dict(body or {})
        self.headers = dict(headers or {})

    def to_request_parts(self):
        return dict(self.query), dict(self.body), dict(self.headers)

    def to_dict(self):
        query, body, headers = self.to_request_parts()
        return {"query": query, "body": body, "headers": headers}

    @classmethod
    def parameter_names(cls, location=None):
        if location is None:
            return [p["name"] for p in cls.PARAMS]
        return [p["name"] for p in cls.PARAMS if p["in"] == location]


class CdnHighDefenseIpGetArticleIpRequest(BaseRequest):
    """加白IP列表.

    API: GET /api/v5/ip.article.list
    """
    API_NAME = 'CdnHighDefenseIP_getArticleIP'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/ip.article.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DnsDomainGetDomainListRequest(BaseRequest):
    """查询域名列表.

    API: GET /api/v5/sdns/domains
    """
    API_NAME = 'DnsDomain_getDomainList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/sdns/domains'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DnsDomainAddDomainRequest(BaseRequest):
    """添加域名.

    API: POST /api/v5/sdns/domains

    Parameters:
        domain (String, required): 域名
    """
    API_NAME = 'DnsDomain_addDomain'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/domains'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'domain', 'required': True, 'default': None, 'description': '域名'},)

    def __init__(self, domain=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain is not _UNSET:
            self.body['domain'] = domain
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainBatchAddDomainsRequest(BaseRequest):
    """批量添加域名.

    API: POST /api/v5/sdns/domains_batch_add

    Parameters:
        domains (String[], required): 域名数组
        add_record (Number, optional, default=0): 添加记录 (0: 否, 1: 是)
        record_value (String, optional): 记录值
        group_id (Number, optional): 分组ID
    """
    API_NAME = 'DnsDomain_batchAddDomains'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/domains_batch_add'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'domains', 'required': True, 'default': None, 'description': '域名数组'}, {'in': 'body', 'type': 'Number', 'name': 'add_record', 'required': False, 'default': '0', 'description': '添加记录 (0: 否, 1: 是)'}, {'in': 'body', 'type': 'String', 'name': 'record_value', 'required': False, 'default': None, 'description': '记录值'}, {'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': False, 'default': None, 'description': '分组ID'})

    def __init__(self, domains=_UNSET, add_record=0, record_value=_UNSET, group_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domains is not _UNSET:
            self.body['domains'] = domains
        self.body['add_record'] = add_record
        if record_value is not _UNSET:
            self.body['record_value'] = record_value
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainBatchDeleteDomainsRequest(BaseRequest):
    """批量删除域名.

    API: DELETE /api/v5/sdns/domains_batch_delete

    Parameters:
        domain_ids (Number[], required): 域名ID数组
    """
    API_NAME = 'DnsDomain_batchDeleteDomains'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/sdns/domains_batch_delete'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '域名ID数组'},)

    def __init__(self, domain_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainGetDomainStatRequest(BaseRequest):
    """查询域名统计.

    API: GET /api/v5/sdns/domains/stat
    """
    API_NAME = 'DnsDomain_getDomainStat'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/sdns/domains/stat'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DnsDomainGetDomainServersRequest(BaseRequest):
    """查询域名服务器.

    API: GET /api/v5/sdns/domains/servers
    """
    API_NAME = 'DnsDomain_getDomainServers'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/sdns/domains/servers'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DnsDomainGetTasksListRequest(BaseRequest):
    """查询任务列表.

    API: GET /api/v5/sdns/tasks
    """
    API_NAME = 'DnsDomain_getTasksList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/sdns/tasks'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DnsDomainGetTaskDetailRequest(BaseRequest):
    """查询任务详情.

    API: GET /api/v5/sdns/tasks/detail
    """
    API_NAME = 'DnsDomain_getTaskDetail'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/sdns/tasks/detail'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class CloudDnsDomainGroupGetGroupListRequest(BaseRequest):
    """查询域名分组列表.

    API: GET /api/v5/sdns/domains/groups
    """
    API_NAME = 'CloudDns_DomainGroup_getGroupList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/sdns/domains/groups'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class CloudDnsDomainGroupAddGroupRequest(BaseRequest):
    """添加域名分组.

    API: POST /api/v5/sdns/domains/groups

    Parameters:
        group_name (String, required): 分组名称
        remark (String, required): 备注
    """
    API_NAME = 'CloudDns_DomainGroup_addGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/domains/groups'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'group_name', 'required': True, 'default': None, 'description': '分组名称'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': True, 'default': None, 'description': '备注'})

    def __init__(self, group_name=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_name is not _UNSET:
            self.body['group_name'] = group_name
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class CloudDnsDomainGroupUpdateGroupRequest(BaseRequest):
    """更新域名分组.

    API: PUT /api/v5/sdns/domains/groups

    Parameters:
        group_id (Number, required): 分组ID
        group_name (String, required): 分组名称
        remark (String, required): 备注
        domain_ids (Number[], required): 域名ID数组
    """
    API_NAME = 'CloudDns_DomainGroup_updateGroup'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/sdns/domains/groups'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': True, 'default': None, 'description': '分组ID'}, {'in': 'body', 'type': 'String', 'name': 'group_name', 'required': True, 'default': None, 'description': '分组名称'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': True, 'default': None, 'description': '备注'}, {'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '域名ID数组'})

    def __init__(self, group_id=_UNSET, group_name=_UNSET, remark=_UNSET, domain_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if group_name is not _UNSET:
            self.body['group_name'] = group_name
        if remark is not _UNSET:
            self.body['remark'] = remark
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        for key, value in kwargs.items():
            self.body[key] = value


class CloudDnsDomainGroupDeleteGroupRequest(BaseRequest):
    """删除域名分组.

    API: DELETE /api/v5/sdns/domains/groups

    Parameters:
        group_id (Number, required): 分组ID
    """
    API_NAME = 'CloudDns_DomainGroup_deleteGroup'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/sdns/domains/groups'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': True, 'default': None, 'description': '分组ID'},)

    def __init__(self, group_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        for key, value in kwargs.items():
            self.body[key] = value


class CloudDnsDomainGroupGetGroupRecordListRequest(BaseRequest):
    """查询域名分组记录列表.

    API: GET /api/v5/sdns/records/groups
    """
    API_NAME = 'CloudDns_DomainGroup_getGroupRecordList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/sdns/records/groups'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class CloudDnsDomainGroupSaveDomainToGroupRequest(BaseRequest):
    """域名分组记录操作.

    API: POST /api/v5/sdns/records/groups_relations

    Parameters:
        group_id (Number, required): 分组ID
        domain_ids (Number[], required): 域名ID
        action (String=add,del, required): 操作 (add 或 del)
    """
    API_NAME = 'CloudDns_DomainGroup_saveDomainToGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/records/groups_relations'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': True, 'default': None, 'description': '分组ID'}, {'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '域名ID'}, {'in': 'body', 'type': 'String=add,del', 'name': 'action', 'required': True, 'default': None, 'description': '操作 (add 或 del)'})

    def __init__(self, group_id=_UNSET, domain_ids=_UNSET, action=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        if action is not _UNSET:
            self.body['action'] = action
        for key, value in kwargs.items():
            self.body[key] = value


class CloudDnsDomainGroupGetGroupDomainListRequest(BaseRequest):
    """查询域名组关联的域名列表.

    API: POST /api/v5/cloud.dns.domain.group.domain.list
    """
    API_NAME = 'CloudDns_DomainGroup_getGroupDomainList'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/cloud.dns.domain.group.domain.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.body[key] = value


class CloudDnsDomainGroupGetGroupUndistributedDomainListRequest(BaseRequest):
    """查询未关联域名组的域名列表.

    API: POST /api/v5/cloud.dns.domain.group.undistributed.domain.list

    Parameters:
        group_id (String, required): 组名ID
        domain (String, optional): 组内域名
    """
    API_NAME = 'CloudDns_DomainGroup_getGroupUndistributedDomainList'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/cloud.dns.domain.group.undistributed.domain.list'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'group_id', 'required': True, 'default': None, 'description': '组名ID'}, {'in': 'body', 'type': 'String', 'name': 'domain', 'required': False, 'default': None, 'description': '组内域名'})

    def __init__(self, group_id=_UNSET, domain=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if domain is not _UNSET:
            self.body['domain'] = domain
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainRecordsGetRecordTypesRequest(BaseRequest):
    """列出支持的记录类型.

    API: GET /api/v5/sdns/types
    """
    API_NAME = 'DnsDomainRecords_getRecordTypes'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/sdns/types'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DnsDomainRecordsGetRecordListRequest(BaseRequest):
    """查询域名记录列表.

    API: GET /api/v5/sdns/records
    """
    API_NAME = 'DnsDomainRecords_getRecordList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/sdns/records'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DnsDomainRecordsAddRecordRequest(BaseRequest):
    """添加域名记录.

    API: POST /api/v5/sdns/records

    Parameters:
        domain_id (Number, required): 域名ID
        record_name (String, required): 记录名称
        record_type (String, required): 记录类型
        record_view (String, required): 线路
        record_value (String, required): 记录值
        record_mx (Number, optional, default=0): MX
        record_ttl (Number, optional, default=600): TTL
        record_remark (String, optional): 记录备注
    """
    API_NAME = 'DnsDomainRecords_addRecord'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/records'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '域名ID'}, {'in': 'body', 'type': 'String', 'name': 'record_name', 'required': True, 'default': None, 'description': '记录名称'}, {'in': 'body', 'type': 'String', 'name': 'record_type', 'required': True, 'default': None, 'description': '记录类型'}, {'in': 'body', 'type': 'String', 'name': 'record_view', 'required': True, 'default': None, 'description': '线路'}, {'in': 'body', 'type': 'String', 'name': 'record_value', 'required': True, 'default': None, 'description': '记录值'}, {'in': 'body', 'type': 'Number', 'name': 'record_mx', 'required': False, 'default': '0', 'description': 'MX'}, {'in': 'body', 'type': 'Number', 'name': 'record_ttl', 'required': False, 'default': '600', 'description': 'TTL'}, {'in': 'body', 'type': 'String', 'name': 'record_remark', 'required': False, 'default': None, 'description': '记录备注'})

    def __init__(self, domain_id=_UNSET, record_name=_UNSET, record_type=_UNSET, record_view=_UNSET, record_value=_UNSET, record_mx=0, record_ttl=600, record_remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if record_name is not _UNSET:
            self.body['record_name'] = record_name
        if record_type is not _UNSET:
            self.body['record_type'] = record_type
        if record_view is not _UNSET:
            self.body['record_view'] = record_view
        if record_value is not _UNSET:
            self.body['record_value'] = record_value
        self.body['record_mx'] = record_mx
        self.body['record_ttl'] = record_ttl
        if record_remark is not _UNSET:
            self.body['record_remark'] = record_remark
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainRecordsBatchAddRecordsRequest(BaseRequest):
    """批量添加域名记录.

    API: POST /api/v5/sdns/records_batch_add

    Parameters:
        domain_ids (Number[], required): 域名ID列表
        records (Object[], required): 记录列表
        records.record_name (String, required): 记录名称
        records.record_type (String, required): 记录类型
        records.record_view (String, required): 线路
        records.record_value (String, required): 记录值
        records.record_mx (Number, optional, default=0): MX
        records.record_ttl (Number, optional, default=600): TTL
        records.record_remark (String, optional): 记录备注
    """
    API_NAME = 'DnsDomainRecords_batchAddRecords'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/records_batch_add'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '域名ID列表'}, {'in': 'body', 'type': 'Object[]', 'name': 'records', 'required': True, 'default': None, 'description': '记录列表'}, {'in': 'body', 'type': 'String', 'name': 'records.record_name', 'required': True, 'default': None, 'description': '记录名称'}, {'in': 'body', 'type': 'String', 'name': 'records.record_type', 'required': True, 'default': None, 'description': '记录类型'}, {'in': 'body', 'type': 'String', 'name': 'records.record_view', 'required': True, 'default': None, 'description': '线路'}, {'in': 'body', 'type': 'String', 'name': 'records.record_value', 'required': True, 'default': None, 'description': '记录值'}, {'in': 'body', 'type': 'Number', 'name': 'records.record_mx', 'required': False, 'default': '0', 'description': 'MX'}, {'in': 'body', 'type': 'Number', 'name': 'records.record_ttl', 'required': False, 'default': '600', 'description': 'TTL'}, {'in': 'body', 'type': 'String', 'name': 'records.record_remark', 'required': False, 'default': None, 'description': '记录备注'})

    def __init__(self, domain_ids=_UNSET, records=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        if records is not _UNSET:
            self.body['records'] = records
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainRecordsEditRecordRequest(BaseRequest):
    """编辑域名记录.

    API: PUT /api/v5/sdns/records

    Parameters:
        record_id (Number, required): 记录ID
        domain_id (Number, required): 域名ID
        record_name (String, required): 记录名称
        record_type (String, required): 记录类型
        record_view (String, required): 线路
        record_value (String, required): 记录值
        record_mx (Number, optional, default=0): MX
        record_ttl (Number, optional, default=600): TTL
        record_remark (String, optional): 记录备注
    """
    API_NAME = 'DnsDomainRecords_editRecord'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/sdns/records'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'record_id', 'required': True, 'default': None, 'description': '记录ID'}, {'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '域名ID'}, {'in': 'body', 'type': 'String', 'name': 'record_name', 'required': True, 'default': None, 'description': '记录名称'}, {'in': 'body', 'type': 'String', 'name': 'record_type', 'required': True, 'default': None, 'description': '记录类型'}, {'in': 'body', 'type': 'String', 'name': 'record_view', 'required': True, 'default': None, 'description': '线路'}, {'in': 'body', 'type': 'String', 'name': 'record_value', 'required': True, 'default': None, 'description': '记录值'}, {'in': 'body', 'type': 'Number', 'name': 'record_mx', 'required': False, 'default': '0', 'description': 'MX'}, {'in': 'body', 'type': 'Number', 'name': 'record_ttl', 'required': False, 'default': '600', 'description': 'TTL'}, {'in': 'body', 'type': 'String', 'name': 'record_remark', 'required': False, 'default': None, 'description': '记录备注'})

    def __init__(self, record_id=_UNSET, domain_id=_UNSET, record_name=_UNSET, record_type=_UNSET, record_view=_UNSET, record_value=_UNSET, record_mx=0, record_ttl=600, record_remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if record_id is not _UNSET:
            self.body['record_id'] = record_id
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if record_name is not _UNSET:
            self.body['record_name'] = record_name
        if record_type is not _UNSET:
            self.body['record_type'] = record_type
        if record_view is not _UNSET:
            self.body['record_view'] = record_view
        if record_value is not _UNSET:
            self.body['record_value'] = record_value
        self.body['record_mx'] = record_mx
        self.body['record_ttl'] = record_ttl
        if record_remark is not _UNSET:
            self.body['record_remark'] = record_remark
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainRecordsBatchPauseRecordsRequest(BaseRequest):
    """批量暂停域名记录.

    API: POST /api/v5/sdns/records_batch_pause

    Parameters:
        domain_id (Number, required): 域名ID
        record_ids (Number[], required): 记录ID列表
    """
    API_NAME = 'DnsDomainRecords_batchPauseRecords'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/records_batch_pause'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '域名ID'}, {'in': 'body', 'type': 'Number[]', 'name': 'record_ids', 'required': True, 'default': None, 'description': '记录ID列表'})

    def __init__(self, domain_id=_UNSET, record_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if record_ids is not _UNSET:
            self.body['record_ids'] = record_ids
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainRecordsBatchEnableRecordsRequest(BaseRequest):
    """批量启用域名记录.

    API: POST /api/v5/sdns/records_batch_enable

    Parameters:
        domain_id (Number, required): 域名ID
        record_ids (Number[], required): 记录ID列表
    """
    API_NAME = 'DnsDomainRecords_batchEnableRecords'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/records_batch_enable'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '域名ID'}, {'in': 'body', 'type': 'Number[]', 'name': 'record_ids', 'required': True, 'default': None, 'description': '记录ID列表'})

    def __init__(self, domain_id=_UNSET, record_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if record_ids is not _UNSET:
            self.body['record_ids'] = record_ids
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainRecordsDeleteRecordRequest(BaseRequest):
    """删除域名记录.

    API: DELETE /api/v5/sdns/records

    Parameters:
        record_id (Number, required): 记录ID
        domain_id (Number, required): 域名ID
    """
    API_NAME = 'DnsDomainRecords_deleteRecord'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/sdns/records'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'record_id', 'required': True, 'default': None, 'description': '记录ID'}, {'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '域名ID'})

    def __init__(self, record_id=_UNSET, domain_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if record_id is not _UNSET:
            self.body['record_id'] = record_id
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainRecordsImportRecordsRequest(BaseRequest):
    """导入域名记录.

    API: POST /api/v5/sdns/records_import

    Parameters:
        xls_file (File, required): Excel文件
    """
    API_NAME = 'DnsDomainRecords_importRecords'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/records_import'
    PARAMS = ({'in': 'body', 'type': 'File', 'name': 'xls_file', 'required': True, 'default': None, 'description': 'Excel文件'},)

    def __init__(self, xls_file=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if xls_file is not _UNSET:
            self.body['xls_file'] = xls_file
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainRecordsExportRecordsRequest(BaseRequest):
    """导出域名记录.

    API: POST /api/v5/sdns/records_export

    Parameters:
        domain_ids (Number[], required): 域名ID列表
    """
    API_NAME = 'DnsDomainRecords_exportRecords'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/records_export'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '域名ID列表'},)

    def __init__(self, domain_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainRecordsGetLinesRequest(BaseRequest):
    """列出线路.

    API: GET /api/v5/sdns/lines
    """
    API_NAME = 'DnsDomainRecords_getLines'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/sdns/lines'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DnsDomainRecordsBatchDeleteRecordsRequest(BaseRequest):
    """批量删除域名记录.

    API: POST /api/v5/sdns/records_batch_delete

    Parameters:
        domain_id (Number, required): 域名ID
        record_ids (Number[], required): 记录ID列表
    """
    API_NAME = 'DnsDomainRecords_batchDeleteRecords'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/records_batch_delete'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '域名ID'}, {'in': 'body', 'type': 'Number[]', 'name': 'record_ids', 'required': True, 'default': None, 'description': '记录ID列表'})

    def __init__(self, domain_id=_UNSET, record_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if record_ids is not _UNSET:
            self.body['record_ids'] = record_ids
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainRecordsGetRecordGroupsListRequest(BaseRequest):
    """查询记录组列表.

    API: GET /api/v5/sdns/records/groups
    """
    API_NAME = 'DnsDomainRecords_getRecordGroupsList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/sdns/records/groups'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DnsDomainRecordsAddRecordGroupRequest(BaseRequest):
    """添加记录组.

    API: POST /api/v5/sdns/records/groups

    Parameters:
        domain_id (Number, required): 域名ID
        group_name (String, required): 组名称
    """
    API_NAME = 'DnsDomainRecords_addRecordGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/records/groups'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '域名ID'}, {'in': 'body', 'type': 'String', 'name': 'group_name', 'required': True, 'default': None, 'description': '组名称'})

    def __init__(self, domain_id=_UNSET, group_name=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if group_name is not _UNSET:
            self.body['group_name'] = group_name
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainRecordsAddRecordGroupRelationsRequest(BaseRequest):
    """添加记录组关系.

    API: POST /api/v5/sdns/records/groups_relations

    Parameters:
        group_id (Number, required): 组ID
        record_ids (Number[], required): 记录ID列表
    """
    API_NAME = 'DnsDomainRecords_addRecordGroupRelations'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/sdns/records/groups_relations'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': True, 'default': None, 'description': '组ID'}, {'in': 'body', 'type': 'Number[]', 'name': 'record_ids', 'required': True, 'default': None, 'description': '记录ID列表'})

    def __init__(self, group_id=_UNSET, record_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if record_ids is not _UNSET:
            self.body['record_ids'] = record_ids
        for key, value in kwargs.items():
            self.body[key] = value


class DnsDomainRecordsDeleteRecordGroupRequest(BaseRequest):
    """删除记录组.

    API: DELETE /api/v5/sdns/records/groups

    Parameters:
        group_id (Number, required): 组ID
    """
    API_NAME = 'DnsDomainRecords_deleteRecordGroup'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/sdns/records/groups'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': True, 'default': None, 'description': '组ID'},)

    def __init__(self, group_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        for key, value in kwargs.items():
            self.body[key] = value


class UserIpUserIpListRequest(BaseRequest):
    """获取 IP 列表.

    API: GET /api/v5/user.ip.list
    """
    API_NAME = 'UserIp_userIpList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/user.ip.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class UserIpUserIpAddRequest(BaseRequest):
    """新增 IP 列表.

    API: POST /api/v5/user.ip.add

    Parameters:
        name (String, required): 列表名称
        remark (String, optional): 备注/描述
    """
    API_NAME = 'UserIp_userIpAdd'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/user.ip.add'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'name', 'required': True, 'default': None, 'description': '列表名称'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '备注/描述'})

    def __init__(self, name=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if name is not _UNSET:
            self.body['name'] = name
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class UserIpUserIpSaveRequest(BaseRequest):
    """更新 IP 列表.

    API: PUT /api/v5/user.ip.save

    Parameters:
        id (String, required): 列表唯一 ID
        name (String, required): 列表名称
        remark (String, optional): 备注/描述
    """
    API_NAME = 'UserIp_userIpSave'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/user.ip.save'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'id', 'required': True, 'default': None, 'description': '列表唯一 ID'}, {'in': 'body', 'type': 'String', 'name': 'name', 'required': True, 'default': None, 'description': '列表名称'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '备注/描述'})

    def __init__(self, id=_UNSET, name=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if name is not _UNSET:
            self.body['name'] = name
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class UserIpUserIpDelRequest(BaseRequest):
    """删除 IP 列表.

    API: DELETE /api/v5/user.ip.del

    Parameters:
        ids (String[], required): 需要删除的 ID 数组，例如 ["1", "2"]
    """
    API_NAME = 'UserIp_userIpDel'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/user.ip.del'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'ids', 'required': True, 'default': None, 'description': '需要删除的 ID 数组，例如 ["1", "2"]'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class UserIpListUserIpItemRequest(BaseRequest):
    """IP 项列表.

    API: GET /api/v5/user.ip.item.list
    """
    API_NAME = 'UserIp_listUserIpItem'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/user.ip.item.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class UserIpAddUserIpItemRequest(BaseRequest):
    """新增 IP 项.

    API: POST /api/v5/user.ip.item.text.save

    Parameters:
        user_ip_id (String, required): 所属 IP 列表 ID
        ip (String, required): IP 地址
        remark (String, optional): 备注
    """
    API_NAME = 'UserIp_AddUserIpItem'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/user.ip.item.text.save'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'user_ip_id', 'required': True, 'default': None, 'description': '所属 IP 列表 ID'}, {'in': 'body', 'type': 'String', 'name': 'ip', 'required': True, 'default': None, 'description': 'IP 地址'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '备注'})

    def __init__(self, user_ip_id=_UNSET, ip=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if user_ip_id is not _UNSET:
            self.body['user_ip_id'] = user_ip_id
        if ip is not _UNSET:
            self.body['ip'] = ip
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class UserIpUpdateUserIpItemRequest(BaseRequest):
    """编辑 IP 项.

    API: PUT /api/v5/user.ip.item.edit

    Parameters:
        _id (String, required): IP UUID
        user_ip_id (String, required): 所属 IP 列表 ID
        ip (String, required): 新的 IP 地址或 CIDR
        remark (String, optional): 备注
    """
    API_NAME = 'UserIp_UpdateUserIpItem'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/user.ip.item.edit'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': '_id', 'required': True, 'default': None, 'description': 'IP UUID'}, {'in': 'body', 'type': 'String', 'name': 'user_ip_id', 'required': True, 'default': None, 'description': '所属 IP 列表 ID'}, {'in': 'body', 'type': 'String', 'name': 'ip', 'required': True, 'default': None, 'description': '新的 IP 地址或 CIDR'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '备注'})

    def __init__(self, _id=_UNSET, user_ip_id=_UNSET, ip=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if _id is not _UNSET:
            self.body['_id'] = _id
        if user_ip_id is not _UNSET:
            self.body['user_ip_id'] = user_ip_id
        if ip is not _UNSET:
            self.body['ip'] = ip
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class UserIpBatchDeleteUserIpItemRequest(BaseRequest):
    """删除 IP 项.

    API: DELETE /api/v5/user.ip.item.del

    Parameters:
        ids (String[], required): 需要删除的 IP 项 UUID 数组
        user_ip_id (String, required): 所属 IP 列表 ID
    """
    API_NAME = 'UserIp_BatchDeleteUserIpItem'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/user.ip.item.del'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'ids', 'required': True, 'default': None, 'description': '需要删除的 IP 项 UUID 数组'}, {'in': 'body', 'type': 'String', 'name': 'user_ip_id', 'required': True, 'default': None, 'description': '所属 IP 列表 ID'})

    def __init__(self, ids=_UNSET, user_ip_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        if user_ip_id is not _UNSET:
            self.body['user_ip_id'] = user_ip_id
        for key, value in kwargs.items():
            self.body[key] = value


class UserIpDeleteAllUserIpItemRequest(BaseRequest):
    """删除所有 IP 项.

    API: POST /api/v5/user.ip.item.all

    Parameters:
        user_ip_id (String, required): 目标 IP 列表 ID
    """
    API_NAME = 'UserIp_DeleteAllUserIpItem'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/user.ip.item.all'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'user_ip_id', 'required': True, 'default': None, 'description': '目标 IP 列表 ID'},)

    def __init__(self, user_ip_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if user_ip_id is not _UNSET:
            self.body['user_ip_id'] = user_ip_id
        for key, value in kwargs.items():
            self.body[key] = value


class UserIpCopyUserIpRequest(BaseRequest):
    """复制 IP 列表.

    API: POST /api/v5/user.ip.copy

    Parameters:
        user_ip_id (String, required): 源 IP 列表 ID
        name (String, required): 新 IP 列表名称
        remark (String, optional): 新列表备注
    """
    API_NAME = 'UserIp_CopyUserIp'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/user.ip.copy'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'user_ip_id', 'required': True, 'default': None, 'description': '源 IP 列表 ID'}, {'in': 'body', 'type': 'String', 'name': 'name', 'required': True, 'default': None, 'description': '新 IP 列表名称'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '新列表备注'})

    def __init__(self, user_ip_id=_UNSET, name=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if user_ip_id is not _UNSET:
            self.body['user_ip_id'] = user_ip_id
        if name is not _UNSET:
            self.body['name'] = name
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class UserIpFileSaveIpItemRequest(BaseRequest):
    """上传 IP 文件.

    API: POST /api/v5/user.ip.item.file.save

    Parameters:
        Content-Type (String, required): 必须为 multipart/form-data
        x-token (String, required): 用户会话令牌，用于身份认证
        Accept-Language (String, optional): 语言偏好（如 en、zh）
        file (File, required): 必填，IP 列表文件（CSV 或 TXT 格式）
        user_ip_id (Number, required): 必填，目标 IP 列表的唯一 ID
        remark (String, optional): 可选，本次批量上传说明
    """
    API_NAME = 'UserIp_FileSaveIpItem'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/user.ip.item.file.save'
    PARAMS = ({'in': 'header', 'type': 'String', 'name': 'Content-Type', 'required': True, 'default': None, 'description': '必须为 multipart/form-data'}, {'in': 'header', 'type': 'String', 'name': 'x-token', 'required': True, 'default': None, 'description': '用户会话令牌，用于身份认证'}, {'in': 'header', 'type': 'String', 'name': 'Accept-Language', 'required': False, 'default': None, 'description': '语言偏好（如 en、zh）'}, {'in': 'body', 'type': 'File', 'name': 'file', 'required': True, 'default': None, 'description': '必填，IP 列表文件（CSV 或 TXT 格式）'}, {'in': 'body', 'type': 'Number', 'name': 'user_ip_id', 'required': True, 'default': None, 'description': '必填，目标 IP 列表的唯一 ID'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '可选，本次批量上传说明'})

    def __init__(self, file=_UNSET, user_ip_id=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if file is not _UNSET:
            self.body['file'] = file
        if user_ip_id is not _UNSET:
            self.body['user_ip_id'] = user_ip_id
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class ServiceBatchListTaskRequest(BaseRequest):
    """查询任务列表.

    API: GET /api/v5/task/list
    """
    API_NAME = 'service_batch_ListTask'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/task/list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class ServiceBatchListSubTaskRequest(BaseRequest):
    """查询子任务列表.

    API: GET /api/v5/subtask/list
    """
    API_NAME = 'service_batch_ListSubTask'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/subtask/list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class WebCdnCleanCacheGetCacheListRequest(BaseRequest):
    """缓存清理可用余额查询.

    API: GET /api/v5/Web.Domain.DashBoard.getCache
    """
    API_NAME = 'WebCdnCleanCache_getCacheList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Web.Domain.DashBoard.getCache'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class WebCdnCleanCacheSaveCacheRequest(BaseRequest):
    """提交缓存清理任务.

    API: PUT /api/v5/Web.Domain.DashBoard.saveCache

    Parameters:
        group_id (Number, optional): 组ID， 可按组刷新缓存
        protocol (Number, optional): 协议：http/https；只有按组刷新的时候才有效
        port (Number, optional): 网站端口，仅有特殊端口时，需要指定；只有按组刷新的时候才有效
        wholesite (String[], optional): 整站
        specialurl (String[], optional): 指定url
        specialdir (String[], optional): 指定目录
    """
    API_NAME = 'WebCdnCleanCache_saveCache'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/Web.Domain.DashBoard.saveCache'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': False, 'default': None, 'description': '组ID， 可按组刷新缓存'}, {'in': 'body', 'type': 'Number', 'name': 'protocol', 'required': False, 'default': None, 'description': '协议：http/https；只有按组刷新的时候才有效'}, {'in': 'body', 'type': 'Number', 'name': 'port', 'required': False, 'default': None, 'description': '网站端口，仅有特殊端口时，需要指定；只有按组刷新的时候才有效'}, {'in': 'body', 'type': 'String[]', 'name': 'wholesite', 'required': False, 'default': None, 'description': '整站'}, {'in': 'body', 'type': 'String[]', 'name': 'specialurl', 'required': False, 'default': None, 'description': '指定url'}, {'in': 'body', 'type': 'String[]', 'name': 'specialdir', 'required': False, 'default': None, 'description': '指定目录'})

    def __init__(self, group_id=_UNSET, protocol=_UNSET, port=_UNSET, wholesite=_UNSET, specialurl=_UNSET, specialdir=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if protocol is not _UNSET:
            self.body['protocol'] = protocol
        if port is not _UNSET:
            self.body['port'] = port
        if wholesite is not _UNSET:
            self.body['wholesite'] = wholesite
        if specialurl is not _UNSET:
            self.body['specialurl'] = specialurl
        if specialdir is not _UNSET:
            self.body['specialdir'] = specialdir
        for key, value in kwargs.items():
            self.body[key] = value


class WebCdnCleanCacheGetTaskListRequest(BaseRequest):
    """查询缓存清理任务列表.

    API: GET /api/v5/Web.Domain.DashBoard.cache.clean.list
    """
    API_NAME = 'WebCdnCleanCache_getTaskList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Web.Domain.DashBoard.cache.clean.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class WebCdnCleanCacheGetTaskDetailRequest(BaseRequest):
    """查询缓存清理任务详情.

    API: GET /api/v5/Web.Domain.DashBoard.cache.clean.detail
    """
    API_NAME = 'WebCdnCleanCache_getTaskDetail'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Web.Domain.DashBoard.cache.clean.detail'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class WebCdnPreheatCacheGetPreheatCacheQuotaRequest(BaseRequest):
    """缓存预热可用余额查询.

    API: GET /api/v5/Web.Domain.DashBoard.get.preheat.cache.list
    """
    API_NAME = 'WebCdnPreheatCache_getPreheatCacheQuota'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Web.Domain.DashBoard.get.preheat.cache.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class WebCdnPreheatCacheGetPreheatCacheListRequest(BaseRequest):
    """查询预热任务列表.

    API: GET /api/v5/Web.Domain.DashBoard.get.preheat.cache.new.list
    """
    API_NAME = 'WebCdnPreheatCache_getPreheatCacheList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Web.Domain.DashBoard.get.preheat.cache.new.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class WebCdnPreheatCacheSavePreheatCacheRequest(BaseRequest):
    """提交预热任务.

    API: POST /api/v5/Web.Domain.DashBoard.save.preheat.cache

    Parameters:
        group_id (Number, optional): 组ID， 可按组刷新缓存
        protocol (Number, optional): 协议：http/https；只有按组刷新的时候才有效
        port (Number, optional): 网站端口，仅有特殊端口时，需要指定；只有按组刷新的时候才有效
        preheat_url (String[], optional): 预热url
    """
    API_NAME = 'WebCdnPreheatCache_savePreheatCache'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/Web.Domain.DashBoard.save.preheat.cache'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': False, 'default': None, 'description': '组ID， 可按组刷新缓存'}, {'in': 'body', 'type': 'Number', 'name': 'protocol', 'required': False, 'default': None, 'description': '协议：http/https；只有按组刷新的时候才有效'}, {'in': 'body', 'type': 'Number', 'name': 'port', 'required': False, 'default': None, 'description': '网站端口，仅有特殊端口时，需要指定；只有按组刷新的时候才有效'}, {'in': 'body', 'type': 'String[]', 'name': 'preheat_url', 'required': False, 'default': None, 'description': '预热url'})

    def __init__(self, group_id=_UNSET, protocol=_UNSET, port=_UNSET, preheat_url=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if protocol is not _UNSET:
            self.body['protocol'] = protocol
        if port is not _UNSET:
            self.body['port'] = port
        if preheat_url is not _UNSET:
            self.body['preheat_url'] = preheat_url
        for key, value in kwargs.items():
            self.body[key] = value


class OplogInfoRequest(BaseRequest):
    """查询操作日志详情.

    API: GET /api/v5/oplog.info
    """
    API_NAME = 'Oplog_info'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/oplog.info'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class OplogMapRequest(BaseRequest):
    """操作日志数据映射.

    API: GET /api/v5/oplog.map
    """
    API_NAME = 'Oplog_map'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/oplog.map'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class OplogGetOplogsRequest(BaseRequest):
    """查询操作日志列表.

    API: GET /api/v5/oplog.list
    """
    API_NAME = 'Oplog_getOplogs'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/oplog.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class CaCertificateSelfAddCaRequest(BaseRequest):
    """上传证书.

    API: POST /api/v5/Web.ca.self.add

    Parameters:
        ca_name (String, required): 证书名称
        product_flag (String, optional): 产品标识
        ca_crt (File, required): 证书公钥，针对控制台上传证书
        ca_key (File, required): 证书私钥，针对控制台上传证书
    """
    API_NAME = 'CaCertificateSelf_addCa'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/Web.ca.self.add'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'ca_name', 'required': True, 'default': None, 'description': '证书名称'}, {'in': 'body', 'type': 'String', 'name': 'product_flag', 'required': False, 'default': None, 'description': '产品标识'}, {'in': 'body', 'type': 'File', 'name': 'ca_crt', 'required': True, 'default': None, 'description': '证书公钥，针对控制台上传证书'}, {'in': 'body', 'type': 'File', 'name': 'ca_key', 'required': True, 'default': None, 'description': '证书私钥，针对控制台上传证书'})

    def __init__(self, ca_name=_UNSET, ca_crt=_UNSET, ca_key=_UNSET, product_flag=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ca_name is not _UNSET:
            self.body['ca_name'] = ca_name
        if ca_crt is not _UNSET:
            self.body['ca_crt'] = ca_crt
        if ca_key is not _UNSET:
            self.body['ca_key'] = ca_key
        if product_flag is not _UNSET:
            self.body['product_flag'] = product_flag
        for key, value in kwargs.items():
            self.body[key] = value


class BatchCaListRequest(BaseRequest):
    """查询域名证书列表.

    API: POST /api/v5/Web.Domain.batch.ca.list

    Parameters:
        domains (String[]], required): 域名列表
    """
    API_NAME = 'Batch_caList'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/Web.Domain.batch.ca.list'
    PARAMS = ({'in': 'body', 'type': 'String[]]', 'name': 'domains', 'required': True, 'default': None, 'description': '域名列表'},)

    def __init__(self, domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domains is not _UNSET:
            self.body['domains'] = domains
        for key, value in kwargs.items():
            self.body[key] = value


class CaCertificateSelfSaveTextCaInfoRequest(BaseRequest):
    """新增证书.

    API: POST /api/v5/Web.ca.text.save

    Parameters:
        id (Number, optional): 证书ID，不传则为新增证书
        ca_name (String, required): 证书名称
        product_flag (String, optional): 产品标识
        ca_cert (String, required): 证书公钥
        ca_key (String, required): 证书私钥
    """
    API_NAME = 'CaCertificateSelf_saveTextCaInfo'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/Web.ca.text.save'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': False, 'default': None, 'description': '证书ID，不传则为新增证书'}, {'in': 'body', 'type': 'String', 'name': 'ca_name', 'required': True, 'default': None, 'description': '证书名称'}, {'in': 'body', 'type': 'String', 'name': 'product_flag', 'required': False, 'default': None, 'description': '产品标识'}, {'in': 'body', 'type': 'String', 'name': 'ca_cert', 'required': True, 'default': None, 'description': '证书公钥'}, {'in': 'body', 'type': 'String', 'name': 'ca_key', 'required': True, 'default': None, 'description': '证书私钥'})

    def __init__(self, ca_name=_UNSET, ca_cert=_UNSET, ca_key=_UNSET, id=_UNSET, product_flag=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ca_name is not _UNSET:
            self.body['ca_name'] = ca_name
        if ca_cert is not _UNSET:
            self.body['ca_cert'] = ca_cert
        if ca_key is not _UNSET:
            self.body['ca_key'] = ca_key
        if id is not _UNSET:
            self.body['id'] = id
        if product_flag is not _UNSET:
            self.body['product_flag'] = product_flag
        for key, value in kwargs.items():
            self.body[key] = value


class CaCertificateSelfEditCaInfoRequest(BaseRequest):
    """编辑证书.

    API: POST /api/v5/Web.ca.info.edit

    Parameters:
        id (Number, required): 证书id
        ca_name (String, required): 证书名称
        product_flag (String, required): 
        ca_cert (File, optional): 证书公钥
        ca_key (File, optional): 证书私钥
    """
    API_NAME = 'CaCertificateSelf_editCaInfo'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/Web.ca.info.edit'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '证书id'}, {'in': 'body', 'type': 'String', 'name': 'ca_name', 'required': True, 'default': None, 'description': '证书名称'}, {'in': 'body', 'type': 'String', 'name': 'product_flag', 'required': True, 'default': None, 'description': ''}, {'in': 'body', 'type': 'File', 'name': 'ca_cert', 'required': False, 'default': None, 'description': '证书公钥'}, {'in': 'body', 'type': 'File', 'name': 'ca_key', 'required': False, 'default': None, 'description': '证书私钥'})

    def __init__(self, id=_UNSET, ca_name=_UNSET, product_flag=_UNSET, ca_cert=_UNSET, ca_key=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if ca_name is not _UNSET:
            self.body['ca_name'] = ca_name
        if product_flag is not _UNSET:
            self.body['product_flag'] = product_flag
        if ca_cert is not _UNSET:
            self.body['ca_cert'] = ca_cert
        if ca_key is not _UNSET:
            self.body['ca_key'] = ca_key
        for key, value in kwargs.items():
            self.body[key] = value


class CaCertificateSelfListCaRequest(BaseRequest):
    """查询证书列表.

    API: GET /api/v5/Web.ca.self.list
    """
    API_NAME = 'CaCertificateSelf_listCa'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Web.ca.self.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class CaCertificateSelfCaExportRequest(BaseRequest):
    """导出证书.

    API: GET /api/v5/Web.ca.self.export
    """
    API_NAME = 'CaCertificateSelf_caExport'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Web.ca.self.export'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class CaCertificateSelfBatchOperatSslRequest(BaseRequest):
    """批量证书绑定域名.

    API: GET/POST /api/v5/Web.ca.batch.operat

    Parameters:
        id (String[], required): 证书id
        type (String=relation, optional): 操作类型: relation(目前唯一可选值)
        product_flag (String, optional): 产品标识
        is_confirm (Number=0,1, optional, default=1): 是否再次检查证书到期: 0-否 1-是
        del_id (String[], optional): 需要剔除不进行关联的证书id
    """
    API_NAME = 'CaCertificateSelf_batchOperatSsl'
    METHOD = 'GET'
    METHODS = ('GET', 'POST')
    PATH = '/api/v5/Web.ca.batch.operat'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'id', 'required': True, 'default': None, 'description': '证书id'}, {'in': 'body', 'type': 'String=relation', 'name': 'type', 'required': False, 'default': None, 'description': '操作类型: relation(目前唯一可选值)'}, {'in': 'body', 'type': 'String', 'name': 'product_flag', 'required': False, 'default': None, 'description': '产品标识'}, {'in': 'body', 'type': 'Number=0,1', 'name': 'is_confirm', 'required': False, 'default': '1', 'description': '是否再次检查证书到期: 0-否 1-是'}, {'in': 'body', 'type': 'String[]', 'name': 'del_id', 'required': False, 'default': None, 'description': '需要剔除不进行关联的证书id'})

    def __init__(self, id=_UNSET, type=_UNSET, product_flag=_UNSET, is_confirm=1, del_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if type is not _UNSET:
            self.body['type'] = type
        if product_flag is not _UNSET:
            self.body['product_flag'] = product_flag
        self.body['is_confirm'] = is_confirm
        if del_id is not _UNSET:
            self.body['del_id'] = del_id
        for key, value in kwargs.items():
            self.query[key] = value


class CaCertificateSelfDelCaRequest(BaseRequest):
    """删除证书.

    API: DELETE /api/v5/Web.ca.self.del

    Parameters:
        ids (String, required): 证书ids,逗号分隔
        product_flag (String, optional): 产品标识
    """
    API_NAME = 'CaCertificateSelf_delCa'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/Web.ca.self.del'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'ids', 'required': True, 'default': None, 'description': '证书ids,逗号分隔'}, {'in': 'body', 'type': 'String', 'name': 'product_flag', 'required': False, 'default': None, 'description': '产品标识'})

    def __init__(self, ids=_UNSET, product_flag=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        if product_flag is not _UNSET:
            self.body['product_flag'] = product_flag
        for key, value in kwargs.items():
            self.body[key] = value


class CaCertificateSelfGetCaDetailRequest(BaseRequest):
    """查询证书详情.

    API: GET /api/v5/Web.ca.self
    """
    API_NAME = 'CaCertificateSelf_getCaDetail'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Web.ca.self'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class CaCertificateSelfEditCaNameRequest(BaseRequest):
    """修改证书名称.

    API: POST /api/v5/Web.ca.self.editcaname

    Parameters:
        id (Number, required): 证书id
        ca_name (String, required): 证书名称
        product_flag (String, optional): 产品标识
    """
    API_NAME = 'CaCertificateSelf_editCaName'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/Web.ca.self.editcaname'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '证书id'}, {'in': 'body', 'type': 'String', 'name': 'ca_name', 'required': True, 'default': None, 'description': '证书名称'}, {'in': 'body', 'type': 'String', 'name': 'product_flag', 'required': False, 'default': None, 'description': '产品标识'})

    def __init__(self, id=_UNSET, ca_name=_UNSET, product_flag=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if ca_name is not _UNSET:
            self.body['ca_name'] = ca_name
        if product_flag is not _UNSET:
            self.body['product_flag'] = product_flag
        for key, value in kwargs.items():
            self.body[key] = value


class CaCertificateApplyAddApplyCaRequest(BaseRequest):
    """申购证书.

    API: POST /api/v5/Web.ca.apply.add

    Parameters:
        domain (string[], required): 域名数组
        type (Number=1,2, optional, default=1): 接入方式
        ca_type (Number=2,3, optional, default=2): 证书机构
    """
    API_NAME = 'CaCertificateApply_addApplyCa'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/Web.ca.apply.add'
    PARAMS = ({'in': 'body', 'type': 'string[]', 'name': 'domain', 'required': True, 'default': None, 'description': '域名数组'}, {'in': 'body', 'type': 'Number=1,2', 'name': 'type', 'required': False, 'default': '1', 'description': '接入方式'}, {'in': 'body', 'type': 'Number=2,3', 'name': 'ca_type', 'required': False, 'default': '2', 'description': '证书机构'})

    def __init__(self, domain=_UNSET, type=1, ca_type=2, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain is not _UNSET:
            self.body['domain'] = domain
        self.body['type'] = type
        self.body['ca_type'] = ca_type
        for key, value in kwargs.items():
            self.body[key] = value


class CaCertificateApplyGetAddByNsSettingRequest(BaseRequest):
    """获取未接入证书申购授权记录.

    API: GET /api/v5/Web.ca.apply.getAddByNsSetting
    """
    API_NAME = 'CaCertificateApply_getAddByNsSetting'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Web.ca.apply.getAddByNsSetting'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DomainGroupSaveGroupRequest(BaseRequest):
    """修改域名组.

    API: POST /api/v5/web.domain.group.save

    Parameters:
        group_id (Number, required): 组ID
        group_name (String, required): 组名
        remark (String, required): 备注
    """
    API_NAME = 'DomainGroup_saveGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/web.domain.group.save'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': True, 'default': None, 'description': '组ID'}, {'in': 'body', 'type': 'String', 'name': 'group_name', 'required': True, 'default': None, 'description': '组名'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': True, 'default': None, 'description': '备注'})

    def __init__(self, group_id=_UNSET, group_name=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if group_name is not _UNSET:
            self.body['group_name'] = group_name
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class DomainGroupGetGroupListRequest(BaseRequest):
    """查询域名组列表.

    API: GET /api/v5/web.domain.group.list
    """
    API_NAME = 'DomainGroup_getGroupList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/web.domain.group.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DomainGroupDelGroupRequest(BaseRequest):
    """删除域名组.

    API: POST /api/v5/web.domain.group.del

    Parameters:
        group_id (Number, required): 组ID
    """
    API_NAME = 'DomainGroup_delGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/web.domain.group.del'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': True, 'default': None, 'description': '组ID'},)

    def __init__(self, group_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        for key, value in kwargs.items():
            self.body[key] = value


class DomainGroupGetGroupDomainListRequest(BaseRequest):
    """查询已绑定域名组的域名列表.

    API: GET /api/v5/web.domain.group.domain.list
    """
    API_NAME = 'DomainGroup_getGroupDomainList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/web.domain.group.domain.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DomainGroupGgtUndistributedDomainListRequest(BaseRequest):
    """查询未绑定域名组的域名列表.

    API: GET /api/v5/web.domain.group.undistributed.domain.list
    """
    API_NAME = 'DomainGroup_ggtUndistributedDomainList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/web.domain.group.undistributed.domain.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DomainGroupAddGroupRequest(BaseRequest):
    """添加域名组.

    API: POST /api/v5/web.domain.group.add

    Parameters:
        group_name (String, required): 组名
        remark (String, optional): 备注
    """
    API_NAME = 'DomainGroup_addGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/web.domain.group.add'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'group_name', 'required': True, 'default': None, 'description': '组名'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '备注'})

    def __init__(self, group_name=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_name is not _UNSET:
            self.body['group_name'] = group_name
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class DomainGroupSaveDomainToGroupRequest(BaseRequest):
    """域名绑定域名组.

    API: POST /api/v5/web.domain.group.domain.save

    Parameters:
        group_id (Number, required): 组名ID
        domain_ids (String[], required): 域名IDs，domain_ids/domains二选一
        domains (String[], required): 域名, domain_ids/domains二选一
        only_unbind_tpl_domain_group (String, required): 域名是否解绑模板（字段废弃，不再使用）
        action (String=add,del, required): 操作: add添加 del删除
    """
    API_NAME = 'DomainGroup_saveDomainToGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/web.domain.group.domain.save'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': True, 'default': None, 'description': '组名ID'}, {'in': 'body', 'type': 'String[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '域名IDs，domain_ids/domains二选一'}, {'in': 'body', 'type': 'String[]', 'name': 'domains', 'required': True, 'default': None, 'description': '域名, domain_ids/domains二选一'}, {'in': 'body', 'type': 'String', 'name': 'only_unbind_tpl_domain_group', 'required': True, 'default': None, 'description': '域名是否解绑模板（字段废弃，不再使用）'}, {'in': 'body', 'type': 'String=add,del', 'name': 'action', 'required': True, 'default': None, 'description': '操作: add添加 del删除'})

    def __init__(self, group_id=_UNSET, domain_ids=_UNSET, domains=_UNSET, only_unbind_tpl_domain_group=_UNSET, action=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        if domains is not _UNSET:
            self.body['domains'] = domains
        if only_unbind_tpl_domain_group is not _UNSET:
            self.body['only_unbind_tpl_domain_group'] = only_unbind_tpl_domain_group
        if action is not _UNSET:
            self.body['action'] = action
        for key, value in kwargs.items():
            self.body[key] = value


class DomainGroupGetGroupInfoRequest(BaseRequest):
    """查询域名组详情.

    API: GET /api/v5/web.domain.group.info
    """
    API_NAME = 'DomainGroup_getGroupInfo'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/web.domain.group.info'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class DomainGroupMoveDomainRequest(BaseRequest):
    """迁移域名组内域名.

    API: POST /api/v5/web.domain.group.move_domain

    Parameters:
        from_group_id (Number, required): 来源组ID
        to_group_id (Number, required): 目标组ID
        domain_ids (Number[], required): 域名ID数组
    """
    API_NAME = 'DomainGroup_moveDomain'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/web.domain.group.move_domain'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'from_group_id', 'required': True, 'default': None, 'description': '来源组ID'}, {'in': 'body', 'type': 'Number', 'name': 'to_group_id', 'required': True, 'default': None, 'description': '目标组ID'}, {'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '域名ID数组'})

    def __init__(self, from_group_id=_UNSET, to_group_id=_UNSET, domain_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if from_group_id is not _UNSET:
            self.body['from_group_id'] = from_group_id
        if to_group_id is not _UNSET:
            self.body['to_group_id'] = to_group_id
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        for key, value in kwargs.items():
            self.body[key] = value


class ListDomainsRequest(BaseRequest):
    """列出域名.

    API: GET /api/v5/domains

    Parameters:
        page (Number, optional): 页码，用于分页。
        page_size (Number, optional): 每页条目数，用于分页。
        access_progress (String, optional): 按接入状态筛选：review_failed (审核失败), review_pending (审核中), enabled (已启用), not_enabled (未启用), access_pending (接入中), deploy_pending (部署中), disabled (已禁用)。
        group_id (Number, optional): 按域名组 ID 筛选。
        domain (String, optional): 按域名名称筛选（模糊搜索）。
        remark (String, optional): 按备注筛选（模糊搜索）。
        origin_ip (String, optional): 按源站 IP 筛选。
        ca_status (String, optional): 按证书绑定状态筛选：bind (已绑定), unbind (未绑定)。
        access_mode (String, optional): 按接入模式筛选：ns (NS 接入), cname (CNAME 接入)。
        protect_status (String, optional): 按边缘节点类型筛选：back_source (回源), scdn (共享节点), exclusive (专属节点)。使用 exclusive_resource_id 筛选时须为 exclusive。
        exclusive_resource_id (Number, optional): 按专属资源包 ID 筛选；使用本参数时 protect_status 必须为 exclusive。
    """
    API_NAME = 'ListDomains'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/domains'
    PARAMS = ({'in': 'param', 'type': 'Number', 'name': 'page', 'required': False, 'default': None, 'description': '页码，用于分页。'}, {'in': 'param', 'type': 'Number', 'name': 'page_size', 'required': False, 'default': None, 'description': '每页条目数，用于分页。'}, {'in': 'param', 'type': 'String', 'name': 'access_progress', 'required': False, 'default': None, 'description': '按接入状态筛选：review_failed (审核失败), review_pending (审核中), enabled (已启用), not_enabled (未启用), access_pending (接入中), deploy_pending (部署中), disabled (已禁用)。'}, {'in': 'param', 'type': 'Number', 'name': 'group_id', 'required': False, 'default': None, 'description': '按域名组 ID 筛选。'}, {'in': 'param', 'type': 'String', 'name': 'domain', 'required': False, 'default': None, 'description': '按域名名称筛选（模糊搜索）。'}, {'in': 'param', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '按备注筛选（模糊搜索）。'}, {'in': 'param', 'type': 'String', 'name': 'origin_ip', 'required': False, 'default': None, 'description': '按源站 IP 筛选。'}, {'in': 'param', 'type': 'String', 'name': 'ca_status', 'required': False, 'default': None, 'description': '按证书绑定状态筛选：bind (已绑定), unbind (未绑定)。'}, {'in': 'param', 'type': 'String', 'name': 'access_mode', 'required': False, 'default': None, 'description': '按接入模式筛选：ns (NS 接入), cname (CNAME 接入)。'}, {'in': 'param', 'type': 'String', 'name': 'protect_status', 'required': False, 'default': None, 'description': '按边缘节点类型筛选：back_source (回源), scdn (共享节点), exclusive (专属节点)。使用 exclusive_resource_id 筛选时须为 exclusive。'}, {'in': 'param', 'type': 'Number', 'name': 'exclusive_resource_id', 'required': False, 'default': None, 'description': '按专属资源包 ID 筛选；使用本参数时 protect_status 必须为 exclusive。'})

    def __init__(self, page=_UNSET, page_size=_UNSET, access_progress=_UNSET, group_id=_UNSET, domain=_UNSET, remark=_UNSET, origin_ip=_UNSET, ca_status=_UNSET, access_mode=_UNSET, protect_status=_UNSET, exclusive_resource_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if page is not _UNSET:
            self.query['page'] = page
        if page_size is not _UNSET:
            self.query['page_size'] = page_size
        if access_progress is not _UNSET:
            self.query['access_progress'] = access_progress
        if group_id is not _UNSET:
            self.query['group_id'] = group_id
        if domain is not _UNSET:
            self.query['domain'] = domain
        if remark is not _UNSET:
            self.query['remark'] = remark
        if origin_ip is not _UNSET:
            self.query['origin_ip'] = origin_ip
        if ca_status is not _UNSET:
            self.query['ca_status'] = ca_status
        if access_mode is not _UNSET:
            self.query['access_mode'] = access_mode
        if protect_status is not _UNSET:
            self.query['protect_status'] = protect_status
        if exclusive_resource_id is not _UNSET:
            self.query['exclusive_resource_id'] = exclusive_resource_id
        for key, value in kwargs.items():
            self.query[key] = value


class AddDomainsRequest(BaseRequest):
    """添加域名.

    API: POST /api/v5/domains

    Parameters:
        domain (String, required): 要添加的域名。
        group_id (Number, optional): 域名组的 ID。
        exclusive_resource_id (Number, optional): 专属资源的 ID。
        remark (String, optional): 域名的备注。
        tpl_id (Number, optional): 应用于域名的模板 ID。(与推荐配置tpl_recommend二选一)
        origins (Object[], optional): 源站服务器设置数组。
        origins.protocol (Number, required): 源站协议：0 (HTTP), 1 (HTTPS)。
        origins.listen_ports (Number[], required): 源站的监听端口数组。
        origins.origin_protocol (Number, required): 源站协议：0 (HTTP), 1 (HTTPS), 2 (跟随)。
        origins.load_balance (Number, required): 负载均衡方法：0 (IP hash), 1 (轮询), 2 (cookie)。
        origins.origin_type (Number, required): 源站类型：0 (IP), 1 (域名)。
        origins.records (Object[], required): 源站记录数组。
        origins.records.view (String, required): 线路：primary-主线路, backup-备用线路。
        origins.records.value (String, required): 记录的值（IP 地址或域名）。
        origins.records.port (Number, required): 记录的端口。
        origins.records.priority (Number, required): 记录的优先级。
        origins.records.host (String, optional): 回源Host，指定回源时的Host头。
        protect_status (String, optional): 边缘节点类型：back_source (回源), scdn (共享节点), exclusive (专属节点)。
        tpl_recommend (String, optional): 推荐配置：大文件下载 - large_file, 网站加速 - web_acce(与模板tpl_id二选一)
    """
    API_NAME = 'AddDomains'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/domains'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'domain', 'required': True, 'default': None, 'description': '要添加的域名。'}, {'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': False, 'default': None, 'description': '域名组的 ID。'}, {'in': 'body', 'type': 'Number', 'name': 'exclusive_resource_id', 'required': False, 'default': None, 'description': '专属资源的 ID。'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '域名的备注。'}, {'in': 'body', 'type': 'Number', 'name': 'tpl_id', 'required': False, 'default': None, 'description': '应用于域名的模板 ID。(与推荐配置tpl_recommend二选一)'}, {'in': 'body', 'type': 'Object[]', 'name': 'origins', 'required': False, 'default': None, 'description': '源站服务器设置数组。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.protocol', 'required': True, 'default': None, 'description': '源站协议：0 (HTTP), 1 (HTTPS)。'}, {'in': 'body', 'type': 'Number[]', 'name': 'origins.listen_ports', 'required': True, 'default': None, 'description': '源站的监听端口数组。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.origin_protocol', 'required': True, 'default': None, 'description': '源站协议：0 (HTTP), 1 (HTTPS), 2 (跟随)。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.load_balance', 'required': True, 'default': None, 'description': '负载均衡方法：0 (IP hash), 1 (轮询), 2 (cookie)。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.origin_type', 'required': True, 'default': None, 'description': '源站类型：0 (IP), 1 (域名)。'}, {'in': 'body', 'type': 'Object[]', 'name': 'origins.records', 'required': True, 'default': None, 'description': '源站记录数组。'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.view', 'required': True, 'default': None, 'description': '线路：primary-主线路, backup-备用线路。'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.value', 'required': True, 'default': None, 'description': '记录的值（IP 地址或域名）。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.records.port', 'required': True, 'default': None, 'description': '记录的端口。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.records.priority', 'required': True, 'default': None, 'description': '记录的优先级。'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.host', 'required': False, 'default': None, 'description': '回源Host，指定回源时的Host头。'}, {'in': 'body', 'type': 'String', 'name': 'protect_status', 'required': False, 'default': None, 'description': '边缘节点类型：back_source (回源), scdn (共享节点), exclusive (专属节点)。'}, {'in': 'body', 'type': 'String', 'name': 'tpl_recommend', 'required': False, 'default': None, 'description': '推荐配置：大文件下载 - large_file, 网站加速 - web_acce(与模板tpl_id二选一)'})

    def __init__(self, domain=_UNSET, origins=_UNSET, group_id=_UNSET, exclusive_resource_id=_UNSET, remark=_UNSET, tpl_id=_UNSET, protect_status=_UNSET, tpl_recommend=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain is not _UNSET:
            self.body['domain'] = domain
        if origins is not _UNSET:
            self.body['origins'] = origins
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if exclusive_resource_id is not _UNSET:
            self.body['exclusive_resource_id'] = exclusive_resource_id
        if remark is not _UNSET:
            self.body['remark'] = remark
        if tpl_id is not _UNSET:
            self.body['tpl_id'] = tpl_id
        if protect_status is not _UNSET:
            self.body['protect_status'] = protect_status
        if tpl_recommend is not _UNSET:
            self.body['tpl_recommend'] = tpl_recommend
        for key, value in kwargs.items():
            self.body[key] = value


class UpdateDomainsRequest(BaseRequest):
    """更新域名.

    API: PUT /api/v5/domains

    Parameters:
        domain_id (Number, required): 要更新的域名 ID。
        remark (String, optional): 域名的最新备注。
    """
    API_NAME = 'UpdateDomains'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/domains'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '要更新的域名 ID。'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '域名的最新备注。'})

    def __init__(self, domain_id=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class BindDomainCertRequest(BaseRequest):
    """绑定域名证书.

    API: POST /api/v5/domains/bind_cert

    Parameters:
        domain_id (Number, required): 要绑定证书的域名 ID。
        ca_id (Number, required): 要绑定的证书 ID。
    """
    API_NAME = 'BindDomainCert'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/domains/bind_cert'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '要绑定证书的域名 ID。'}, {'in': 'body', 'type': 'Number', 'name': 'ca_id', 'required': True, 'default': None, 'description': '要绑定的证书 ID。'})

    def __init__(self, domain_id=_UNSET, ca_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if ca_id is not _UNSET:
            self.body['ca_id'] = ca_id
        for key, value in kwargs.items():
            self.body[key] = value


class UnBindDomainCertRequest(BaseRequest):
    """解绑域名证书.

    API: POST /api/v5/domains/unbind_cert

    Parameters:
        domain_id (Number, required): 要解绑证书的域名 ID。
        ca_id (Number, required): 要解绑的证书 ID。
    """
    API_NAME = 'UnBindDomainCert'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/domains/unbind_cert'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '要解绑证书的域名 ID。'}, {'in': 'body', 'type': 'Number', 'name': 'ca_id', 'required': True, 'default': None, 'description': '要解绑的证书 ID。'})

    def __init__(self, domain_id=_UNSET, ca_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if ca_id is not _UNSET:
            self.body['ca_id'] = ca_id
        for key, value in kwargs.items():
            self.body[key] = value


class DeleteDomainsRequest(BaseRequest):
    """删除域名.

    API: DELETE /api/v5/domains

    Parameters:
        ids (Number[], required): 要删除的域名 ID 数组。
    """
    API_NAME = 'DeleteDomains'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/domains'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'ids', 'required': True, 'default': None, 'description': '要删除的域名 ID 数组。'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class DisableDomainsRequest(BaseRequest):
    """禁用域名.

    API: POST /api/v5/domains_disable

    Parameters:
        domain_ids (Number[], required): 要禁用的域名 ID 数组。
    """
    API_NAME = 'DisableDomains'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/domains_disable'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '要禁用的域名 ID 数组。'},)

    def __init__(self, domain_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        for key, value in kwargs.items():
            self.body[key] = value


class EnableDomainsRequest(BaseRequest):
    """启用域名.

    API: POST /api/v5/domains_enable

    Parameters:
        domain_ids (Number[], required): 要启用的域名 ID 数组。
    """
    API_NAME = 'EnableDomains'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/domains_enable'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '要启用的域名 ID 数组。'},)

    def __init__(self, domain_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        for key, value in kwargs.items():
            self.body[key] = value


class RefreshDomainsAccessRequest(BaseRequest):
    """刷新域名接入状态.

    API: POST /api/v5/domains/access_refresh

    Parameters:
        domain_ids (Number[], required): 要刷新的域名 ID 数组。
    """
    API_NAME = 'RefreshDomainsAccess'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/domains/access_refresh'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '要刷新的域名 ID 数组。'},)

    def __init__(self, domain_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        for key, value in kwargs.items():
            self.body[key] = value


class ExportDomainsRequest(BaseRequest):
    """导出域名.

    API: POST /api/v5/domains/domains_export

    Parameters:
        domain_ids (Number[], optional): 要导出的特定域名 ID 数组。
        access_progress (String, optional): 按接入状态筛选：review_failed (审核失败), review_pending (审核中), enabled (已启用), not_enabled (未启用), access_pending (接入中), deploy_pending (部署中), disabled (已禁用)。
        group_id (Number, optional): 按域名组 ID 筛选。
        domain (String, optional): 按域名名称筛选（模糊搜索）。
        remark (String, optional): 按备注筛选（模糊搜索）。
        origin_ip (String, optional): 按源站 IP 筛选。
        ca_status (String, optional): 按证书绑定状态筛选：bind (已绑定), unbind (未绑定)。
        access_mode (String, optional): 按接入模式筛选：ns (NS 接入), cname (CNAME 接入)。
        protect_status (String, optional): 按边缘节点类型筛选：back_source (回源), scdn (共享节点), exclusive (专属节点)。使用 exclusive_resource_id 筛选时须为 exclusive。
        exclusive_resource_id (Number, optional): 按专属资源包 ID 筛选；使用本参数时 protect_status 必须为 exclusive。
    """
    API_NAME = 'ExportDomains'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/domains/domains_export'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': False, 'default': None, 'description': '要导出的特定域名 ID 数组。'}, {'in': 'body', 'type': 'String', 'name': 'access_progress', 'required': False, 'default': None, 'description': '按接入状态筛选：review_failed (审核失败), review_pending (审核中), enabled (已启用), not_enabled (未启用), access_pending (接入中), deploy_pending (部署中), disabled (已禁用)。'}, {'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': False, 'default': None, 'description': '按域名组 ID 筛选。'}, {'in': 'body', 'type': 'String', 'name': 'domain', 'required': False, 'default': None, 'description': '按域名名称筛选（模糊搜索）。'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '按备注筛选（模糊搜索）。'}, {'in': 'body', 'type': 'String', 'name': 'origin_ip', 'required': False, 'default': None, 'description': '按源站 IP 筛选。'}, {'in': 'body', 'type': 'String', 'name': 'ca_status', 'required': False, 'default': None, 'description': '按证书绑定状态筛选：bind (已绑定), unbind (未绑定)。'}, {'in': 'body', 'type': 'String', 'name': 'access_mode', 'required': False, 'default': None, 'description': '按接入模式筛选：ns (NS 接入), cname (CNAME 接入)。'}, {'in': 'body', 'type': 'String', 'name': 'protect_status', 'required': False, 'default': None, 'description': '按边缘节点类型筛选：back_source (回源), scdn (共享节点), exclusive (专属节点)。使用 exclusive_resource_id 筛选时须为 exclusive。'}, {'in': 'body', 'type': 'Number', 'name': 'exclusive_resource_id', 'required': False, 'default': None, 'description': '按专属资源包 ID 筛选；使用本参数时 protect_status 必须为 exclusive。'})

    def __init__(self, domain_ids=_UNSET, access_progress=_UNSET, group_id=_UNSET, domain=_UNSET, remark=_UNSET, origin_ip=_UNSET, ca_status=_UNSET, access_mode=_UNSET, protect_status=_UNSET, exclusive_resource_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        if access_progress is not _UNSET:
            self.body['access_progress'] = access_progress
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if domain is not _UNSET:
            self.body['domain'] = domain
        if remark is not _UNSET:
            self.body['remark'] = remark
        if origin_ip is not _UNSET:
            self.body['origin_ip'] = origin_ip
        if ca_status is not _UNSET:
            self.body['ca_status'] = ca_status
        if access_mode is not _UNSET:
            self.body['access_mode'] = access_mode
        if protect_status is not _UNSET:
            self.body['protect_status'] = protect_status
        if exclusive_resource_id is not _UNSET:
            self.body['exclusive_resource_id'] = exclusive_resource_id
        for key, value in kwargs.items():
            self.body[key] = value


class AddOriginsRequest(BaseRequest):
    """添加源站.

    API: POST /api/v5/domains/origins

    Parameters:
        domain_id (Number, required): 要添加源站的域名 ID。
        origins (Object[], required): 源站服务器设置数组。
        origins.protocol (Number, required): 源站协议：0 (HTTP), 1 (HTTPS)。
        origins.listen_ports (Number[], required): 源站的监听端口数组。
        origins.origin_protocol (Number, required): 源站协议：0 (HTTP), 1 (HTTPS), 2 (跟随)。
        origins.load_balance (Number, required): 负载均衡方法：0 (IP hash), 1 (轮询), 2 (cookie)。
        origins.origin_type (Number, required): 源站类型：0 (IP), 1 (域名)。
        origins.records (Object[], required): 源站记录数组。
        origins.records.view (String, required): 线路：primary-主线路, backup-备用线路。
        origins.records.value (String, required): 记录的值（IP 地址或域名）。
        origins.records.port (Number, required): 记录的端口。
        origins.records.priority (Number, required): 记录的优先级。
        origins.records.host (String, optional): 回源Host，指定回源时的Host头。
    """
    API_NAME = 'AddOrigins'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/domains/origins'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '要添加源站的域名 ID。'}, {'in': 'body', 'type': 'Object[]', 'name': 'origins', 'required': True, 'default': None, 'description': '源站服务器设置数组。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.protocol', 'required': True, 'default': None, 'description': '源站协议：0 (HTTP), 1 (HTTPS)。'}, {'in': 'body', 'type': 'Number[]', 'name': 'origins.listen_ports', 'required': True, 'default': None, 'description': '源站的监听端口数组。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.origin_protocol', 'required': True, 'default': None, 'description': '源站协议：0 (HTTP), 1 (HTTPS), 2 (跟随)。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.load_balance', 'required': True, 'default': None, 'description': '负载均衡方法：0 (IP hash), 1 (轮询), 2 (cookie)。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.origin_type', 'required': True, 'default': None, 'description': '源站类型：0 (IP), 1 (域名)。'}, {'in': 'body', 'type': 'Object[]', 'name': 'origins.records', 'required': True, 'default': None, 'description': '源站记录数组。'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.view', 'required': True, 'default': None, 'description': '线路：primary-主线路, backup-备用线路。'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.value', 'required': True, 'default': None, 'description': '记录的值（IP 地址或域名）。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.records.port', 'required': True, 'default': None, 'description': '记录的端口。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.records.priority', 'required': True, 'default': None, 'description': '记录的优先级。'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.host', 'required': False, 'default': None, 'description': '回源Host，指定回源时的Host头。'})

    def __init__(self, domain_id=_UNSET, origins=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if origins is not _UNSET:
            self.body['origins'] = origins
        for key, value in kwargs.items():
            self.body[key] = value


class UpdateOriginsRequest(BaseRequest):
    """更新源站.

    API: PUT /api/v5/domains/origins

    Parameters:
        domain_id (Number, required): 正在更新源站的域名 ID。
        origins (Object[], required): 更新后的源站设置数组。
        origins.id (Number, required): 要更新的源站设置 ID。
        origins.domain_id (Number, required): 与源站关联的域名 ID。
        origins.protocol (Number, required): 源站协议：0 (HTTP), 1 (HTTPS)。
        origins.listen_port (Number, required): 源站的监听端口。
        origins.origin_protocol (Number, required): 源站协议：0 (HTTP), 1 (HTTPS), 2 (跟随)。
        origins.load_balance (Number, required): 负载均衡方法：0 (IP hash), 1 (轮询), 2 (cookie)。
        origins.origin_type (Number, required): 源站类型：0 (IP), 1 (域名)。
        origins.records (Object[], required): 源站记录数组。
        origins.records.view (String, required): 线路：primary-主线路, backup-备用线路。
        origins.records.value (String, required): 记录的值（IP 地址或域名）。
        origins.records.port (Number, required): 记录的端口。
        origins.records.priority (Number, required): 记录的优先级。
        origins.records.host (String, optional): 回源Host，指定回源时的Host头。
    """
    API_NAME = 'UpdateOrigins'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/domains/origins'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '正在更新源站的域名 ID。'}, {'in': 'body', 'type': 'Object[]', 'name': 'origins', 'required': True, 'default': None, 'description': '更新后的源站设置数组。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.id', 'required': True, 'default': None, 'description': '要更新的源站设置 ID。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.domain_id', 'required': True, 'default': None, 'description': '与源站关联的域名 ID。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.protocol', 'required': True, 'default': None, 'description': '源站协议：0 (HTTP), 1 (HTTPS)。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.listen_port', 'required': True, 'default': None, 'description': '源站的监听端口。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.origin_protocol', 'required': True, 'default': None, 'description': '源站协议：0 (HTTP), 1 (HTTPS), 2 (跟随)。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.load_balance', 'required': True, 'default': None, 'description': '负载均衡方法：0 (IP hash), 1 (轮询), 2 (cookie)。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.origin_type', 'required': True, 'default': None, 'description': '源站类型：0 (IP), 1 (域名)。'}, {'in': 'body', 'type': 'Object[]', 'name': 'origins.records', 'required': True, 'default': None, 'description': '源站记录数组。'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.view', 'required': True, 'default': None, 'description': '线路：primary-主线路, backup-备用线路。'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.value', 'required': True, 'default': None, 'description': '记录的值（IP 地址或域名）。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.records.port', 'required': True, 'default': None, 'description': '记录的端口。'}, {'in': 'body', 'type': 'Number', 'name': 'origins.records.priority', 'required': True, 'default': None, 'description': '记录的优先级。'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.host', 'required': False, 'default': None, 'description': '回源Host，指定回源时的Host头。'})

    def __init__(self, domain_id=_UNSET, origins=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if origins is not _UNSET:
            self.body['origins'] = origins
        for key, value in kwargs.items():
            self.body[key] = value


class DeleteOriginsRequest(BaseRequest):
    """删除源站.

    API: DELETE /api/v5/domains/origins

    Parameters:
        ids (Number[], required): 要删除的源站设置 ID 数组。
        domain_id (Number, required): 与源站关联的域名 ID。
    """
    API_NAME = 'DeleteOrigins'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/domains/origins'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'ids', 'required': True, 'default': None, 'description': '要删除的源站设置 ID 数组。'}, {'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '与源站关联的域名 ID。'})

    def __init__(self, ids=_UNSET, domain_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        for key, value in kwargs.items():
            self.body[key] = value


class ListOriginsRequest(BaseRequest):
    """列出源站.

    API: GET /api/v5/domains/origins

    Parameters:
        domain_id (Number, optional): 要列出源站的域名 ID。
    """
    API_NAME = 'ListOrigins'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/domains/origins'
    PARAMS = ({'in': 'param', 'type': 'Number', 'name': 'domain_id', 'required': False, 'default': None, 'description': '要列出源站的域名 ID。'},)

    def __init__(self, domain_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.query['domain_id'] = domain_id
        for key, value in kwargs.items():
            self.query[key] = value


class SwitchDomainNodesRequest(BaseRequest):
    """切换域名节点.

    API: POST /api/v5/domains/nodes_switch

    Parameters:
        domain_id (Number, required): 要切换节点的域名 ID。
        protect_status (String, required): 新的边缘节点类型：origin (回源), scdn (共享节点), exclusive (专属节点)。
        exclusive_resource_id (Number, optional): 如果 protect_status 为 exclusive，则为专属资源 ID。
    """
    API_NAME = 'SwitchDomainNodes'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/domains/nodes_switch'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '要切换节点的域名 ID。'}, {'in': 'body', 'type': 'String', 'name': 'protect_status', 'required': True, 'default': None, 'description': '新的边缘节点类型：origin (回源), scdn (共享节点), exclusive (专属节点)。'}, {'in': 'body', 'type': 'Number', 'name': 'exclusive_resource_id', 'required': False, 'default': None, 'description': '如果 protect_status 为 exclusive，则为专属资源 ID。'})

    def __init__(self, domain_id=_UNSET, protect_status=_UNSET, exclusive_resource_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if protect_status is not _UNSET:
            self.body['protect_status'] = protect_status
        if exclusive_resource_id is not _UNSET:
            self.body['exclusive_resource_id'] = exclusive_resource_id
        for key, value in kwargs.items():
            self.body[key] = value


class SwitchDomainAccessModeRequest(BaseRequest):
    """切换域名接入模式.

    API: POST /api/v5/domains/access_switch

    Parameters:
        domain_id (Number, required): 要切换接入模式的域名 ID。
        access_mode (String, required): 新的接入模式：cname (CNAME 接入), ns (NS 接入)。
    """
    API_NAME = 'SwitchDomainAccessMode'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/domains/access_switch'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '要切换接入模式的域名 ID。'}, {'in': 'body', 'type': 'String', 'name': 'access_mode', 'required': True, 'default': None, 'description': '新的接入模式：cname (CNAME 接入), ns (NS 接入)。'})

    def __init__(self, domain_id=_UNSET, access_mode=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if access_mode is not _UNSET:
            self.body['access_mode'] = access_mode
        for key, value in kwargs.items():
            self.body[key] = value


class UpdateDomainBaseSettingsRequest(BaseRequest):
    """更新域名基础设置.

    API: PUT /api/v5/domains/base_settings

    Parameters:
        domain_id (Number, required): 要更新的域名 ID。
        value (Object, required): 新的基础设置值。
        value.proxy_host (Object, optional): 代理主机设置。
        value.proxy_host.proxy_host (String, optional): 代理主机值。
        value.proxy_host.proxy_host_type (String, optional): 如果存在 proxy_host，则代理主机类型：default, off。
        value.proxy_sni (Object, optional): 代理 SNI 设置。
        value.proxy_sni.proxy_sni (String, optional): 代理 SNI 值。
        value.proxy_sni.status (String, optional): 如果存在 proxy_sni，则代理 SNI 状态：on, off。
        value.domain_redirect (Object, optional): 域名重定向设置。
        value.domain_redirect.status (String, optional): 如果存在 domain_redirect，则显式/隐式转发状态：on, off。
        value.domain_redirect.jump_to (String, optional): 域名重定向跳转到的 URL。
        value.domain_redirect.jump_type (String, optional): 如果存在 domain_redirect，则显式/隐式转发类型：explicit, implicit。
    """
    API_NAME = 'UpdateDomainBaseSettings'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/domains/base_settings'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '要更新的域名 ID。'}, {'in': 'body', 'type': 'Object', 'name': 'value', 'required': True, 'default': None, 'description': '新的基础设置值。'}, {'in': 'body', 'type': 'Object', 'name': 'value.proxy_host', 'required': False, 'default': None, 'description': '代理主机设置。'}, {'in': 'body', 'type': 'String', 'name': 'value.proxy_host.proxy_host', 'required': False, 'default': None, 'description': '代理主机值。'}, {'in': 'body', 'type': 'String', 'name': 'value.proxy_host.proxy_host_type', 'required': False, 'default': None, 'description': '如果存在 proxy_host，则代理主机类型：default, off。'}, {'in': 'body', 'type': 'Object', 'name': 'value.proxy_sni', 'required': False, 'default': None, 'description': '代理 SNI 设置。'}, {'in': 'body', 'type': 'String', 'name': 'value.proxy_sni.proxy_sni', 'required': False, 'default': None, 'description': '代理 SNI 值。'}, {'in': 'body', 'type': 'String', 'name': 'value.proxy_sni.status', 'required': False, 'default': None, 'description': '如果存在 proxy_sni，则代理 SNI 状态：on, off。'}, {'in': 'body', 'type': 'Object', 'name': 'value.domain_redirect', 'required': False, 'default': None, 'description': '域名重定向设置。'}, {'in': 'body', 'type': 'String', 'name': 'value.domain_redirect.status', 'required': False, 'default': None, 'description': '如果存在 domain_redirect，则显式/隐式转发状态：on, off。'}, {'in': 'body', 'type': 'String', 'name': 'value.domain_redirect.jump_to', 'required': False, 'default': None, 'description': '域名重定向跳转到的 URL。'}, {'in': 'body', 'type': 'String', 'name': 'value.domain_redirect.jump_type', 'required': False, 'default': None, 'description': '如果存在 domain_redirect，则显式/隐式转发类型：explicit, implicit。'})

    def __init__(self, domain_id=_UNSET, value=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if value is not _UNSET:
            self.body['value'] = value
        for key, value in kwargs.items():
            self.body[key] = value


class GetDomainBaseSettingsRequest(BaseRequest):
    """获取域名基础设置.

    API: GET /api/v5/domains/base_settings
    """
    API_NAME = 'GetDomainBaseSettings'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/domains/base_settings'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class ListBriefDomainsRequest(BaseRequest):
    """列出简要域名.

    API: POST /api/v5/brief_domains

    Parameters:
        ids (Number[], optional): 要检索的域名 ID 数组。如果为空，则返回所有域名（行为可能因实现而异）。
    """
    API_NAME = 'ListBriefDomains'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/brief_domains'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'ids', 'required': False, 'default': None, 'description': '要检索的域名 ID 数组。如果为空，则返回所有域名（行为可能因实现而异）。'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class GetDomainTemplatesRequest(BaseRequest):
    """获取域名模板.

    API: GET /api/v5/domains/templates
    """
    API_NAME = 'GetDomainTemplates'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/domains/templates'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class AccessInfoDownloadRequest(BaseRequest):
    """批量添加域名任务，已添加域名接入信息下载.

    API: POST /api/v5/domains/access_info_download

    Parameters:
        domain_infos (Object[], required): 要下载接入信息的域名信息数组。
        domain_infos.domain (String, required): 域名。
        domain_infos.data_key (String, required): 域名。
        domain_infos.biz_main_key (String, required): 固定传domain。
    """
    API_NAME = 'AccessInfoDownload'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/domains/access_info_download'
    PARAMS = ({'in': 'body', 'type': 'Object[]', 'name': 'domain_infos', 'required': True, 'default': None, 'description': '要下载接入信息的域名信息数组。'}, {'in': 'body', 'type': 'String', 'name': 'domain_infos.domain', 'required': True, 'default': None, 'description': '域名。'}, {'in': 'body', 'type': 'String', 'name': 'domain_infos.data_key', 'required': True, 'default': None, 'description': '域名。'}, {'in': 'body', 'type': 'String', 'name': 'domain_infos.biz_main_key', 'required': True, 'default': None, 'description': '固定传domain。'})

    def __init__(self, domain_infos=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_infos is not _UNSET:
            self.body['domain_infos'] = domain_infos
        for key, value in kwargs.items():
            self.body[key] = value


class OriginGroupGetOriginGroupListRequest(BaseRequest):
    """查询源站组列表.

    API: GET /api/v5/origin_groups
    """
    API_NAME = 'OriginGroup_getOriginGroupList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/origin_groups'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class OriginGroupGetOriginGroupInfoRequest(BaseRequest):
    """查询源站组详情.

    API: GET /api/v5/origin_groups/detail
    """
    API_NAME = 'OriginGroup_getOriginGroupInfo'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/origin_groups/detail'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class OriginGroupAddOriginGroupRequest(BaseRequest):
    """添加源站组.

    API: POST /api/v5/origin_groups

    Parameters:
        name (String, required): 源站组名称(2-16个字符)
        remark (String, optional): 备注(2-64个字符)
        origins (Object[], required): 源站列表(至少1个)
        origins.origin_type (Number=0,1, required): 源站类型: 0-IP, 1-域名
        origins.records (Object[], required): 源站记录列表(至少1个)
        origins.records.value (String, required): 源站地址
        origins.records.view (String=primary,backup, required): 源站类型: primary-主源, backup-备源
        origins.records.host (String, optional): 回源Host
        origins.protocol_ports (Object[], required): 协议端口映射关系(至少1个)
        origins.protocol_ports.protocol (Number=0,1, required): 协议: 0-http, 1-https
        origins.protocol_ports.listen_ports (Number[], required): 监听端口列表
        origins.origin_protocol (Number=0,1,2, required): 回源协议: 0-http, 1-https, 2-follow(协议跟随)
        origins.load_balance (Number=0,1,2, required): 负载均衡策略: 0-ip_hash, 1-round_robin(轮询), 2-cookie
    """
    API_NAME = 'OriginGroup_addOriginGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/origin_groups'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'name', 'required': True, 'default': None, 'description': '源站组名称(2-16个字符)'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '备注(2-64个字符)'}, {'in': 'body', 'type': 'Object[]', 'name': 'origins', 'required': True, 'default': None, 'description': '源站列表(至少1个)'}, {'in': 'body', 'type': 'Number=0,1', 'name': 'origins.origin_type', 'required': True, 'default': None, 'description': '源站类型: 0-IP, 1-域名'}, {'in': 'body', 'type': 'Object[]', 'name': 'origins.records', 'required': True, 'default': None, 'description': '源站记录列表(至少1个)'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.value', 'required': True, 'default': None, 'description': '源站地址'}, {'in': 'body', 'type': 'String=primary,backup', 'name': 'origins.records.view', 'required': True, 'default': None, 'description': '源站类型: primary-主源, backup-备源'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.host', 'required': False, 'default': None, 'description': '回源Host'}, {'in': 'body', 'type': 'Object[]', 'name': 'origins.protocol_ports', 'required': True, 'default': None, 'description': '协议端口映射关系(至少1个)'}, {'in': 'body', 'type': 'Number=0,1', 'name': 'origins.protocol_ports.protocol', 'required': True, 'default': None, 'description': '协议: 0-http, 1-https'}, {'in': 'body', 'type': 'Number[]', 'name': 'origins.protocol_ports.listen_ports', 'required': True, 'default': None, 'description': '监听端口列表'}, {'in': 'body', 'type': 'Number=0,1,2', 'name': 'origins.origin_protocol', 'required': True, 'default': None, 'description': '回源协议: 0-http, 1-https, 2-follow(协议跟随)'}, {'in': 'body', 'type': 'Number=0,1,2', 'name': 'origins.load_balance', 'required': True, 'default': None, 'description': '负载均衡策略: 0-ip_hash, 1-round_robin(轮询), 2-cookie'})

    def __init__(self, name=_UNSET, origins=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if name is not _UNSET:
            self.body['name'] = name
        if origins is not _UNSET:
            self.body['origins'] = origins
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class OriginGroupUpdateOriginGroupRequest(BaseRequest):
    """修改源站组.

    API: PUT /api/v5/origin_groups

    Parameters:
        id (Number, required): 源站组ID
        name (String, required): 源站组名称(2-16个字符)
        remark (String, required): 备注(2-64个字符)
        origins (Object[], required): 源站列表(至少1个)
        origins.id (Number, required): 源站记录ID(为0表示新增，大于0表示更新)
        origins.origin_type (Number=0,1, required): 源站类型: 0-IP, 1-域名
        origins.records (Object[], required): 源站记录列表(至少1个)
        origins.records.value (String, required): 源站地址
        origins.records.view (String=primary,backup, required): 源站类型: primary-主源, backup-备源
        origins.records.host (String, required): 回源Host
        origins.protocol_ports (Object[], required): 协议端口映射关系(至少1个)
        origins.protocol_ports.protocol (Number=0,1, required): 协议: 0-http, 1-https
        origins.protocol_ports.listen_ports (Number[], required): 监听端口列表
        origins.origin_protocol (Number=0,1,2, required): 回源协议: 0-http, 1-https, 2-follow(协议跟随)
        origins.load_balance (Number=0,1,2, required): 负载均衡策略: 0-ip_hash, 1-round_robin(轮询), 2-cookie
    """
    API_NAME = 'OriginGroup_updateOriginGroup'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/origin_groups'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '源站组ID'}, {'in': 'body', 'type': 'String', 'name': 'name', 'required': True, 'default': None, 'description': '源站组名称(2-16个字符)'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': True, 'default': None, 'description': '备注(2-64个字符)'}, {'in': 'body', 'type': 'Object[]', 'name': 'origins', 'required': True, 'default': None, 'description': '源站列表(至少1个)'}, {'in': 'body', 'type': 'Number', 'name': 'origins.id', 'required': True, 'default': None, 'description': '源站记录ID(为0表示新增，大于0表示更新)'}, {'in': 'body', 'type': 'Number=0,1', 'name': 'origins.origin_type', 'required': True, 'default': None, 'description': '源站类型: 0-IP, 1-域名'}, {'in': 'body', 'type': 'Object[]', 'name': 'origins.records', 'required': True, 'default': None, 'description': '源站记录列表(至少1个)'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.value', 'required': True, 'default': None, 'description': '源站地址'}, {'in': 'body', 'type': 'String=primary,backup', 'name': 'origins.records.view', 'required': True, 'default': None, 'description': '源站类型: primary-主源, backup-备源'}, {'in': 'body', 'type': 'String', 'name': 'origins.records.host', 'required': True, 'default': None, 'description': '回源Host'}, {'in': 'body', 'type': 'Object[]', 'name': 'origins.protocol_ports', 'required': True, 'default': None, 'description': '协议端口映射关系(至少1个)'}, {'in': 'body', 'type': 'Number=0,1', 'name': 'origins.protocol_ports.protocol', 'required': True, 'default': None, 'description': '协议: 0-http, 1-https'}, {'in': 'body', 'type': 'Number[]', 'name': 'origins.protocol_ports.listen_ports', 'required': True, 'default': None, 'description': '监听端口列表'}, {'in': 'body', 'type': 'Number=0,1,2', 'name': 'origins.origin_protocol', 'required': True, 'default': None, 'description': '回源协议: 0-http, 1-https, 2-follow(协议跟随)'}, {'in': 'body', 'type': 'Number=0,1,2', 'name': 'origins.load_balance', 'required': True, 'default': None, 'description': '负载均衡策略: 0-ip_hash, 1-round_robin(轮询), 2-cookie'})

    def __init__(self, id=_UNSET, name=_UNSET, remark=_UNSET, origins=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if name is not _UNSET:
            self.body['name'] = name
        if remark is not _UNSET:
            self.body['remark'] = remark
        if origins is not _UNSET:
            self.body['origins'] = origins
        for key, value in kwargs.items():
            self.body[key] = value


class OriginGroupDelOriginGroupRequest(BaseRequest):
    """删除源站组.

    API: DELETE /api/v5/origin_groups

    Parameters:
        ids (Number[], required): 源站组ID数组(至少1个)
    """
    API_NAME = 'OriginGroup_delOriginGroup'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/origin_groups'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'ids', 'required': True, 'default': None, 'description': '源站组ID数组(至少1个)'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class OriginGroupBindOriginGroupToDomainsRequest(BaseRequest):
    """绑定源站组到域名.

    API: POST /api/v5/origin_groups/domains_bind

    Parameters:
        origin_group_id (Number, required): 源站组ID
        domain_ids (Number[], optional): 域名ID数组
        domain_group_ids (Number[], optional): 域名组ID数组
        domains (String[], optional): 域名数组
    """
    API_NAME = 'OriginGroup_bindOriginGroupToDomains'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/origin_groups/domains_bind'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'origin_group_id', 'required': True, 'default': None, 'description': '源站组ID'}, {'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': False, 'default': None, 'description': '域名ID数组'}, {'in': 'body', 'type': 'Number[]', 'name': 'domain_group_ids', 'required': False, 'default': None, 'description': '域名组ID数组'}, {'in': 'body', 'type': 'String[]', 'name': 'domains', 'required': False, 'default': None, 'description': '域名数组'})

    def __init__(self, origin_group_id=_UNSET, domain_ids=_UNSET, domain_group_ids=_UNSET, domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if origin_group_id is not _UNSET:
            self.body['origin_group_id'] = origin_group_id
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        if domain_group_ids is not _UNSET:
            self.body['domain_group_ids'] = domain_group_ids
        if domains is not _UNSET:
            self.body['domains'] = domains
        for key, value in kwargs.items():
            self.body[key] = value


class OriginGroupGetAllOriginGroupsRequest(BaseRequest):
    """查询所有源站组列表(用于域名配置选择).

    API: GET /api/v5/origin_groups/all
    """
    API_NAME = 'OriginGroup_getAllOriginGroups'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/origin_groups/all'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class OriginGroupCopyOriginGroupRequest(BaseRequest):
    """复制源站组到域名.

    API: POST /api/v5/origin_groups/copy

    Parameters:
        origin_group_id (Number, required): 源站组ID
        domain_id (Number, required): 域名ID
    """
    API_NAME = 'OriginGroup_copyOriginGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/origin_groups/copy'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'origin_group_id', 'required': True, 'default': None, 'description': '源站组ID'}, {'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '域名ID'})

    def __init__(self, origin_group_id=_UNSET, domain_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if origin_group_id is not _UNSET:
            self.body['origin_group_id'] = origin_group_id
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        for key, value in kwargs.items():
            self.body[key] = value


class FireWallReportGetBlockListRequest(BaseRequest):
    """SCDN拦截统计.

    API: GET /api/v5/firewall.report.block.list
    """
    API_NAME = 'FireWallReport_getBlockList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.report.block.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class FireWallReportGetBlockDetailsRequest(BaseRequest):
    """查询SCDN拦截详情.

    API: GET /api/v5/firewall.report.block.details
    """
    API_NAME = 'FireWallReport_getBlockDetails'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.report.block.details'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class FireWallReportGetPackageBlockListRequest(BaseRequest):
    """四层拦截统计.

    API: GET /api/v5/firewall.report.package.block.list
    """
    API_NAME = 'FireWallReport_getPackageBlockList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.report.package.block.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class FireWallReportGetPackageBlockDetailsRequest(BaseRequest):
    """查询四层拦截详情.

    API: GET /api/v5/firewall.report.package.block.details
    """
    API_NAME = 'FireWallReport_getPackageBlockDetails'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.report.package.block.details'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class CcQpsMaxRequest(BaseRequest):
    """查询CC攻击最大QPS.

    API: POST /api/v5/stats_data.cc.qps.max

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cc_qps_max'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cc.qps.max'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CcAttackTimesRequest(BaseRequest):
    """查询CC攻击次数.

    API: POST /api/v5/stats_data.cc.attack.times

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cc_attack_times'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cc.attack.times'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CcTimesLineRequest(BaseRequest):
    """查询CC攻击趋势.

    API: POST /api/v5/stats_data.cc.times.line

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        interval (String=1m,5m,1h,1d, required): 粒度，1m｜5m（24小时内），1h（7天内），1d（不限）
    """
    API_NAME = 'cc_times_line'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cc.times.line'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String=1m,5m,1h,1d', 'name': 'interval', 'required': True, 'default': None, 'description': '粒度，1m｜5m（24小时内），1h（7天内），1d（不限）'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, interval=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if interval is not _UNSET:
            self.body['interval'] = interval
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CcReportStatsRequest(BaseRequest):
    """统计CC数据.

    API: POST /api/v5/stats_data.cc.report.stats

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cc_report_stats'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cc.report.stats'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainUaispDistributeRequest(BaseRequest):
    """UA、ISP分布.

    API: POST /api/v5/stats_data.cdn.domain.uaisp.distribute

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cdn_domain_uaisp_distribute'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.uaisp.distribute'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainCountryDistributeRequest(BaseRequest):
    """国家分布.

    API: POST /api/v5/stats_data.cdn.domain.country.distribute

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cdn_domain_country_distribute'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.country.distribute'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainProvinceDistributeRequest(BaseRequest):
    """省份分布.

    API: POST /api/v5/stats_data.cdn.domain.province.distribute

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cdn_domain_province_distribute'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.province.distribute'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainStatusDistributeRequest(BaseRequest):
    """状态码分布.

    API: POST /api/v5/stats_data.cdn.domain.status.distribute

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cdn_domain_status_distribute'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.status.distribute'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainNodeFlowBandwidthRequest(BaseRequest):
    """回源、命中缓存流量带宽趋势.

    API: POST /api/v5/stats_data.cdn.domain.node.flow.bandwidth

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        interval (String=1m,5m,1h,1d, required): 粒度，1m｜5m（24小时内），1h（7天内），1d（不限）
    """
    API_NAME = 'cdn_domain_node_flow_bandwidth'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.node.flow.bandwidth'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String=1m,5m,1h,1d', 'name': 'interval', 'required': True, 'default': None, 'description': '粒度，1m｜5m（24小时内），1h（7天内），1d（不限）'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, interval=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if interval is not _UNSET:
            self.body['interval'] = interval
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainNodeFlowBandwidthCn2Request(BaseRequest):
    """国内、海外、cn2流量带宽趋势.

    API: POST /api/v5/stats_data.cdn.domain.node.flow.bandwidth.cn2

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        interval (String=1m,5m,1h,1d, required): 粒度，1m｜5m（24小时内），1h（7天内），1d（不限）
    """
    API_NAME = 'cdn_domain_node_flow_bandwidth_cn2'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.node.flow.bandwidth.cn2'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String=1m,5m,1h,1d', 'name': 'interval', 'required': True, 'default': None, 'description': '粒度，1m｜5m（24小时内），1h（7天内），1d（不限）'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, interval=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if interval is not _UNSET:
            self.body['interval'] = interval
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainNodeFlowBandwidthNodeRequest(BaseRequest):
    """各个节点的流量带宽趋势.

    API: POST /api/v5/stats_data.cdn.domain.node.flow.bandwidth.node

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        interval (String=1m,5m,1h,1d, required): 粒度，1m｜5m（24小时内），1h（7天内），1d（不限）
    """
    API_NAME = 'cdn_domain_node_flow_bandwidth_node'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.node.flow.bandwidth.node'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String=1m,5m,1h,1d', 'name': 'interval', 'required': True, 'default': None, 'description': '粒度，1m｜5m（24小时内），1h（7天内），1d（不限）'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, interval=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if interval is not _UNSET:
            self.body['interval'] = interval
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class DomainTimesRequest(BaseRequest):
    """域名访问次数趋势.

    API: POST /api/v5/stats_data.cdn.domain.times
    """
    API_NAME = 'domainTimes'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.times'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.body[key] = value


class DomainQpsRequest(BaseRequest):
    """域名QPS趋势.

    API: POST /api/v5/stats_data.cdn.domain.qps

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        interval (String=1m,5m,1h,1d, required): 粒度，1m｜5m（24小时内），1h（7天内），1d（不限）
    """
    API_NAME = 'domainQps'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.qps'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String=1m,5m,1h,1d', 'name': 'interval', 'required': True, 'default': None, 'description': '粒度，1m｜5m（24小时内），1h（7天内），1d（不限）'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, interval=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if interval is not _UNSET:
            self.body['interval'] = interval
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainFlowLineRequest(BaseRequest):
    """根据节点类型查流量趋势.

    API: POST /api/v5/stats_data.cdn.domain.flow.line

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        interval (String=1m,5m,1h,1d, required): 粒度，1m｜5m（24小时内），1h（7天内），1d（不限）
        node_type (String=ALL,RIM,OVERSEAS_OPTIMIZATION,CN2,HK_HIGH_DEFENSE_CN2, required): 节点类型，必须，多个值用逗号分隔
    """
    API_NAME = 'cdn_domain_flow_line'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.flow.line'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String=1m,5m,1h,1d', 'name': 'interval', 'required': True, 'default': None, 'description': '粒度，1m｜5m（24小时内），1h（7天内），1d（不限）'}, {'in': 'body', 'type': 'String=ALL,RIM,OVERSEAS_OPTIMIZATION,CN2,HK_HIGH_DEFENSE_CN2', 'name': 'node_type', 'required': True, 'default': None, 'description': '节点类型，必须，多个值用逗号分隔'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, interval=_UNSET, node_type=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if interval is not _UNSET:
            self.body['interval'] = interval
        if node_type is not _UNSET:
            self.body['node_type'] = node_type
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainBandwidthLineRequest(BaseRequest):
    """根据节点类型查带宽趋势.

    API: POST /api/v5/stats_data.cdn.domain.bandwidth.line

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        interval (String=1m,5m,1h,1d, required): 粒度，1m｜5m（24小时内），1h（7天内），1d（不限）
        node_type (String=ALL,RIM,OVERSEAS_OPTIMIZATION,CN2,HK_HIGH_DEFENSE_CN2, required): 节点类型，必须，多个值用逗号分隔
    """
    API_NAME = 'cdn_domain_bandwidth_line'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.bandwidth.line'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String=1m,5m,1h,1d', 'name': 'interval', 'required': True, 'default': None, 'description': '粒度，1m｜5m（24小时内），1h（7天内），1d（不限）'}, {'in': 'body', 'type': 'String=ALL,RIM,OVERSEAS_OPTIMIZATION,CN2,HK_HIGH_DEFENSE_CN2', 'name': 'node_type', 'required': True, 'default': None, 'description': '节点类型，必须，多个值用逗号分隔'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, interval=_UNSET, node_type=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if interval is not _UNSET:
            self.body['interval'] = interval
        if node_type is not _UNSET:
            self.body['node_type'] = node_type
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainBandwidth95Request(BaseRequest):
    """根据节点类型查95带宽.

    API: POST /api/v5/stats_data.cdn.domain.bandwidth_95

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        node_type (String=ALL,RIM,OVERSEAS_OPTIMIZATION,CN2,HK_HIGH_DEFENSE_CN2, required): 节点类型，必须，多个值用逗号分隔
    """
    API_NAME = 'cdn_domain_bandwidth_95'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.bandwidth_95'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String=ALL,RIM,OVERSEAS_OPTIMIZATION,CN2,HK_HIGH_DEFENSE_CN2', 'name': 'node_type', 'required': True, 'default': None, 'description': '节点类型，必须，多个值用逗号分隔'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, node_type=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if node_type is not _UNSET:
            self.body['node_type'] = node_type
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainPvtimesRequest(BaseRequest):
    """域名PV次数.

    API: POST /api/v5/stats_data.cdn.domain.pvtimes

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cdn_domain_pvtimes'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.pvtimes'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainFlowTopRequest(BaseRequest):
    """域名流量TOP.

    API: POST /api/v5/stats_data.cdn.domain.flow.top

    Parameters:
        acct_id (Number, required): 用户id
        top_size (Number, required): top N
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cdn_domain_flow_top'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.flow.top'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'Number', 'name': 'top_size', 'required': True, 'default': None, 'description': 'top N'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, top_size=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if top_size is not _UNSET:
            self.body['top_size'] = top_size
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainBandwidthTopRequest(BaseRequest):
    """域名带宽TOP.

    API: POST /api/v5/stats_data.cdn.domain.bandwidth.top

    Parameters:
        acct_id (Number, required): 用户id
        top_size (Number, required): top N
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cdn_domain_bandwidth_top'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.bandwidth.top'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'Number', 'name': 'top_size', 'required': True, 'default': None, 'description': 'top N'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, top_size=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if top_size is not _UNSET:
            self.body['top_size'] = top_size
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainTimesTopRequest(BaseRequest):
    """域名访问次数TOP.

    API: POST /api/v5/stats_data.cdn.domain.times.top

    Parameters:
        acct_id (Number, required): 用户id
        top_size (Number, required): top N
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cdn_domain_times_top'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.times.top'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'Number', 'name': 'top_size', 'required': True, 'default': None, 'description': 'top N'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, top_size=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if top_size is not _UNSET:
            self.body['top_size'] = top_size
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainTimesTopEsRequest(BaseRequest):
    """域名访问次数TOP(ES).

    API: POST /api/v5/stats_data.cdn.domain.times.top.es

    Parameters:
        acct_id (Number, required): 用户id
        top_size (Number, required): top N
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        http_referer (String, required): 可选参数，限制请求referer条件
    """
    API_NAME = 'cdn_domain_times_top_es'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.times.top.es'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'Number', 'name': 'top_size', 'required': True, 'default': None, 'description': 'top N'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'http_referer', 'required': True, 'default': None, 'description': '可选参数，限制请求referer条件'})

    def __init__(self, acct_id=_UNSET, top_size=_UNSET, start_time=_UNSET, end_time=_UNSET, http_referer=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if top_size is not _UNSET:
            self.body['top_size'] = top_size
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if http_referer is not _UNSET:
            self.body['http_referer'] = http_referer
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainUrlTopRequest(BaseRequest):
    """热门URL.

    API: POST /api/v5/stats_data.cdn.domain.url.top

    Parameters:
        acct_id (Number, required): 用户id
        top_size (Number, required): top N
        http_referer (String, required): http_referer
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cdn_domain_url_top'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.url.top'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'Number', 'name': 'top_size', 'required': True, 'default': None, 'description': 'top N'}, {'in': 'body', 'type': 'String', 'name': 'http_referer', 'required': True, 'default': None, 'description': 'http_referer'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, top_size=_UNSET, http_referer=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if top_size is not _UNSET:
            self.body['top_size'] = top_size
        if http_referer is not _UNSET:
            self.body['http_referer'] = http_referer
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainRefererTopRequest(BaseRequest):
    """热门REFERER.

    API: POST /api/v5/stats_data.cdn.domain.referer.top

    Parameters:
        acct_id (Number, required): 用户id
        top_size (Number, required): top N
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'cdn_domain_referer_top'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.referer.top'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'Number', 'name': 'top_size', 'required': True, 'default': None, 'description': 'top N'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, top_size=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if top_size is not _UNSET:
            self.body['top_size'] = top_size
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainStatusTopDownloadRequest(BaseRequest):
    """状态码下载.

    API: POST /api/v5/stats_data.cdn.domain.status.top.download

    Parameters:
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        group_id (String[], optional): 按域名分组查询（默认查该用户id下的所有域名）
        resource_ids (String[], optional): 按独享资源id查询（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        time_zone (String, required): 时区，格式 UTC+08:00形式
    """
    API_NAME = 'cdn_domain_status_top_download'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.status.top.download'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String[]', 'name': 'group_id', 'required': False, 'default': None, 'description': '按域名分组查询（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String[]', 'name': 'resource_ids', 'required': False, 'default': None, 'description': '按独享资源id查询（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'time_zone', 'required': True, 'default': None, 'description': '时区，格式 UTC+08:00形式'})

    def __init__(self, start_time=_UNSET, end_time=_UNSET, time_zone=_UNSET, sub_domains=_UNSET, group_id=_UNSET, resource_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if time_zone is not _UNSET:
            self.body['time_zone'] = time_zone
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if resource_ids is not _UNSET:
            self.body['resource_ids'] = resource_ids
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainBandwidthDownloadRequest(BaseRequest):
    """域名带宽使用下载.

    API: POST /api/v5/stats_data.cdn.domain.bandwidth.download

    Parameters:
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        group_id (String[], optional): 按域名分组查询（默认查该用户id下的所有域名）
        resource_ids (String[], optional): 按独享资源id查询（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        time_zone (String, required): 时区，格式 UTC+08:00形式
    """
    API_NAME = 'cdn_domain_bandwidth_download'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.bandwidth.download'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String[]', 'name': 'group_id', 'required': False, 'default': None, 'description': '按域名分组查询（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String[]', 'name': 'resource_ids', 'required': False, 'default': None, 'description': '按独享资源id查询（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'time_zone', 'required': True, 'default': None, 'description': '时区，格式 UTC+08:00形式'})

    def __init__(self, start_time=_UNSET, end_time=_UNSET, time_zone=_UNSET, sub_domains=_UNSET, group_id=_UNSET, resource_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if time_zone is not _UNSET:
            self.body['time_zone'] = time_zone
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if resource_ids is not _UNSET:
            self.body['resource_ids'] = resource_ids
        for key, value in kwargs.items():
            self.body[key] = value


class CdnDomainFlowDownloadRequest(BaseRequest):
    """域名流量使用下载.

    API: POST /api/v5/stats_data.cdn.domain.flow.download

    Parameters:
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        group_id (String[], optional): 按域名分组查询（默认查该用户id下的所有域名）
        resource_ids (String[], optional): 按独享资源id查询（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        time_zone (String, required): 时区，格式 UTC+08:00形式
    """
    API_NAME = 'cdn_domain_flow_download'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.cdn.domain.flow.download'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String[]', 'name': 'group_id', 'required': False, 'default': None, 'description': '按域名分组查询（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String[]', 'name': 'resource_ids', 'required': False, 'default': None, 'description': '按独享资源id查询（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'time_zone', 'required': True, 'default': None, 'description': '时区，格式 UTC+08:00形式'})

    def __init__(self, start_time=_UNSET, end_time=_UNSET, time_zone=_UNSET, sub_domains=_UNSET, group_id=_UNSET, resource_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if time_zone is not _UNSET:
            self.body['time_zone'] = time_zone
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if resource_ids is not _UNSET:
            self.body['resource_ids'] = resource_ids
        for key, value in kwargs.items():
            self.body[key] = value


class TcpBandwidthRequest(BaseRequest):
    """查询TCP带宽数据.

    API: POST /api/v5/stats_data.tcp.bandwidth

    Parameters:
        package_ids (NUMBER[], required): tcp套餐id，如果为空，没有数据。
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'tcp_bandwidth'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.tcp.bandwidth'
    PARAMS = ({'in': 'body', 'type': 'NUMBER[]', 'name': 'package_ids', 'required': True, 'default': None, 'description': 'tcp套餐id，如果为空，没有数据。'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, package_ids=_UNSET, start_time=_UNSET, end_time=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if package_ids is not _UNSET:
            self.body['package_ids'] = package_ids
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        for key, value in kwargs.items():
            self.body[key] = value


class TcpCcFlawRequest(BaseRequest):
    """查询TCP流量数据.

    API: POST /api/v5/statistic.tjkd.plus.tcp.cc.flaw

    Parameters:
        package_id (Number, required): 套餐ID
        ip (String[], optional): 套餐IP
        port (String[], optional): 套餐端口
        start_time (String, optional): 开始时间
        end_time (String, optional): 结束时间
        interval (String=1m,5m,15m,1h, optional): 时间间隔
    """
    API_NAME = 'tcp_cc_flaw'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/statistic.tjkd.plus.tcp.cc.flaw'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'package_id', 'required': True, 'default': None, 'description': '套餐ID'}, {'in': 'body', 'type': 'String[]', 'name': 'ip', 'required': False, 'default': None, 'description': '套餐IP'}, {'in': 'body', 'type': 'String[]', 'name': 'port', 'required': False, 'default': None, 'description': '套餐端口'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': False, 'default': None, 'description': '开始时间'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': False, 'default': None, 'description': '结束时间'}, {'in': 'body', 'type': 'String=1m,5m,15m,1h', 'name': 'interval', 'required': False, 'default': None, 'description': '时间间隔'})

    def __init__(self, package_id=_UNSET, ip=_UNSET, port=_UNSET, start_time=_UNSET, end_time=_UNSET, interval=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if package_id is not _UNSET:
            self.body['package_id'] = package_id
        if ip is not _UNSET:
            self.body['ip'] = ip
        if port is not _UNSET:
            self.body['port'] = port
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if interval is not _UNSET:
            self.body['interval'] = interval
        for key, value in kwargs.items():
            self.body[key] = value


class WafAttackTimesRequest(BaseRequest):
    """WAF攻击次数.

    API: POST /api/v5/stats_data.waf.attack.times

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'waf_attack_times'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.waf.attack.times'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class WafReportStatsRequest(BaseRequest):
    """WAF数据统计.

    API: POST /api/v5/stats_data.waf.report.stats

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
    """
    API_NAME = 'waf_report_stats'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.waf.report.stats'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class WafWebshellEventListRequest(BaseRequest):
    """入侵事件.

    API: POST /api/v5/stats_data.waf.webshell.event.list

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        page (Number, required): 页码
        per_page (Number, required): 每页数目
    """
    API_NAME = 'waf_webshell_event_list'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.waf.webshell.event.list'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'Number', 'name': 'page', 'required': True, 'default': None, 'description': '页码'}, {'in': 'body', 'type': 'Number', 'name': 'per_page', 'required': True, 'default': None, 'description': '每页数目'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, page=_UNSET, per_page=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if page is not _UNSET:
            self.body['page'] = page
        if per_page is not _UNSET:
            self.body['per_page'] = per_page
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class WafWebshellEventDetailRequest(BaseRequest):
    """入侵事件详情.

    API: POST /api/v5/stats_data.waf.webshell.event.detail

    Parameters:
        remote_addr (String, required): 攻击ip
        request_url (String, required): url
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        page (Number, required): 页码
        per_page (Number, required): 每页数目
    """
    API_NAME = 'waf_webshell_event_detail'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.waf.webshell.event.detail'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'remote_addr', 'required': True, 'default': None, 'description': '攻击ip'}, {'in': 'body', 'type': 'String', 'name': 'request_url', 'required': True, 'default': None, 'description': 'url'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'Number', 'name': 'page', 'required': True, 'default': None, 'description': '页码'}, {'in': 'body', 'type': 'Number', 'name': 'per_page', 'required': True, 'default': None, 'description': '每页数目'})

    def __init__(self, remote_addr=_UNSET, request_url=_UNSET, start_time=_UNSET, end_time=_UNSET, page=_UNSET, per_page=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if remote_addr is not _UNSET:
            self.body['remote_addr'] = remote_addr
        if request_url is not _UNSET:
            self.body['request_url'] = request_url
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if page is not _UNSET:
            self.body['page'] = page
        if per_page is not _UNSET:
            self.body['per_page'] = per_page
        for key, value in kwargs.items():
            self.body[key] = value


class WafAttackEventListRequest(BaseRequest):
    """定向攻击事件.

    API: POST /api/v5/stats_data.waf.attack.event.list

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        page (Number, required): 页码
        per_page (Number, required): 每页数目
    """
    API_NAME = 'waf_attack_event_list'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.waf.attack.event.list'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'Number', 'name': 'page', 'required': True, 'default': None, 'description': '页码'}, {'in': 'body', 'type': 'Number', 'name': 'per_page', 'required': True, 'default': None, 'description': '每页数目'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, page=_UNSET, per_page=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if page is not _UNSET:
            self.body['page'] = page
        if per_page is not _UNSET:
            self.body['per_page'] = per_page
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class WafAttackEventDetailRequest(BaseRequest):
    """定向攻击事件详情.

    API: POST /api/v5/stats_data.waf.attack.event.detail

    Parameters:
        remote_addr (String, required): 攻击ip
        http_host (String, required): 被攻击域名
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        page (Number, required): 页码
        per_page (Number, required): 每页数目
    """
    API_NAME = 'waf_attack_event_detail'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.waf.attack.event.detail'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'remote_addr', 'required': True, 'default': None, 'description': '攻击ip'}, {'in': 'body', 'type': 'String', 'name': 'http_host', 'required': True, 'default': None, 'description': '被攻击域名'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'Number', 'name': 'page', 'required': True, 'default': None, 'description': '页码'}, {'in': 'body', 'type': 'Number', 'name': 'per_page', 'required': True, 'default': None, 'description': '每页数目'})

    def __init__(self, remote_addr=_UNSET, http_host=_UNSET, start_time=_UNSET, end_time=_UNSET, page=_UNSET, per_page=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if remote_addr is not _UNSET:
            self.body['remote_addr'] = remote_addr
        if http_host is not _UNSET:
            self.body['http_host'] = http_host
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if page is not _UNSET:
            self.body['page'] = page
        if per_page is not _UNSET:
            self.body['per_page'] = per_page
        for key, value in kwargs.items():
            self.body[key] = value


class WafScanEventListRequest(BaseRequest):
    """扫描事件.

    API: POST /api/v5/stats_data.waf.scan.event.list

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        page (Number, required): 页码
        per_page (Number, required): 每页数目
    """
    API_NAME = 'waf_scan_event_list'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.waf.scan.event.list'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'Number', 'name': 'page', 'required': True, 'default': None, 'description': '页码'}, {'in': 'body', 'type': 'Number', 'name': 'per_page', 'required': True, 'default': None, 'description': '每页数目'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, page=_UNSET, per_page=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if page is not _UNSET:
            self.body['page'] = page
        if per_page is not _UNSET:
            self.body['per_page'] = per_page
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class WafScanEventDetailRequest(BaseRequest):
    """扫描事件详情.

    API: POST /api/v5/stats_data.waf.scan.event.detail

    Parameters:
        remote_addr (String, required): 攻击ip
        http_host (String, required): 被攻击的域名
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        page (Number, required): 页码
        per_page (Number, required): 每页数目
    """
    API_NAME = 'waf_scan_event_detail'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.waf.scan.event.detail'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'remote_addr', 'required': True, 'default': None, 'description': '攻击ip'}, {'in': 'body', 'type': 'String', 'name': 'http_host', 'required': True, 'default': None, 'description': '被攻击的域名'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'Number', 'name': 'page', 'required': True, 'default': None, 'description': '页码'}, {'in': 'body', 'type': 'Number', 'name': 'per_page', 'required': True, 'default': None, 'description': '每页数目'})

    def __init__(self, remote_addr=_UNSET, http_host=_UNSET, start_time=_UNSET, end_time=_UNSET, page=_UNSET, per_page=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if remote_addr is not _UNSET:
            self.body['remote_addr'] = remote_addr
        if http_host is not _UNSET:
            self.body['http_host'] = http_host
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if page is not _UNSET:
            self.body['page'] = page
        if per_page is not _UNSET:
            self.body['per_page'] = per_page
        for key, value in kwargs.items():
            self.body[key] = value


class WafTypeLineRequest(BaseRequest):
    """waf各类型攻击趋势.

    API: POST /api/v5/stats_data.waf.type.line

    Parameters:
        acct_id (Number, required): 用户id
        sub_domains (String[], optional): 用户勾选的子域名（默认查该用户id下的所有域名）
        start_time (String, required): 起始时间，格式 yyyy-MM-dd HH:mm:ss
        end_time (String, required): 截止时间，格式 yyyy-MM-dd HH:mm:ss
        interval (String=1m,5m,1h,1d, required): 粒度，1m｜5m（24小时内），1h（7天内），1d（不限）
    """
    API_NAME = 'waf_type_line'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/stats_data.waf.type.line'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'acct_id', 'required': True, 'default': None, 'description': '用户id'}, {'in': 'body', 'type': 'String[]', 'name': 'sub_domains', 'required': False, 'default': None, 'description': '用户勾选的子域名（默认查该用户id下的所有域名）'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '起始时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '截止时间，格式 yyyy-MM-dd HH:mm:ss'}, {'in': 'body', 'type': 'String=1m,5m,1h,1d', 'name': 'interval', 'required': True, 'default': None, 'description': '粒度，1m｜5m（24小时内），1h（7天内），1d（不限）'})

    def __init__(self, acct_id=_UNSET, start_time=_UNSET, end_time=_UNSET, interval=_UNSET, sub_domains=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if acct_id is not _UNSET:
            self.body['acct_id'] = acct_id
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if interval is not _UNSET:
            self.body['interval'] = interval
        if sub_domains is not _UNSET:
            self.body['sub_domains'] = sub_domains
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTaskTaskListRequest(BaseRequest):
    """查询日志下载任务列表.

    API: POST/GET /api/v5/soc.log.download.task.list
    """
    API_NAME = 'LogDownloadTask_taskList'
    METHOD = 'POST'
    METHODS = ('POST', 'GET')
    PATH = '/api/v5/soc.log.download.task.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTaskAddTaskRequest(BaseRequest):
    """添加日志下载任务.

    API: POST /api/v5/soc.log.download.task.add

    Parameters:
        task_name (String, required): 任务名称
        is_use_template (Number=0,1, required): 是否使用模板 0未使用 1 使用
        template_id (Number, optional): 模板ID
        data_source (String=ng,cc,waf, required): 数据来源 ng，cc，waf
        download_fields (String[], required): 下载字段(当选择ja3_hash、ja3n字段时，日期范围仅支持2024年12月19日及之后的时间)
        search_terms (Object, required): 限制字段 搜索条件 (键为字段名，值为字符串或字符串数组)
        file_type (String=csv,json, required): 文件类型 xls csv json
        start_time (String, required): 开始时间
        end_time (String, required): 结束时间
        lang (String=zh_CN,en_US, optional, default=zh_CN): 下载语言 zh_CN=中文 en_US=英文
    """
    API_NAME = 'LogDownloadTask_addTask'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/soc.log.download.task.add'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'task_name', 'required': True, 'default': None, 'description': '任务名称'}, {'in': 'body', 'type': 'Number=0,1', 'name': 'is_use_template', 'required': True, 'default': None, 'description': '是否使用模板 0未使用 1 使用'}, {'in': 'body', 'type': 'Number', 'name': 'template_id', 'required': False, 'default': None, 'description': '模板ID'}, {'in': 'body', 'type': 'String=ng,cc,waf', 'name': 'data_source', 'required': True, 'default': None, 'description': '数据来源 ng，cc，waf'}, {'in': 'body', 'type': 'String[]', 'name': 'download_fields', 'required': True, 'default': None, 'description': '下载字段(当选择ja3_hash、ja3n字段时，日期范围仅支持2024年12月19日及之后的时间)'}, {'in': 'body', 'type': 'Object', 'name': 'search_terms', 'required': True, 'default': None, 'description': '限制字段 搜索条件 (键为字段名，值为字符串或字符串数组)'}, {'in': 'body', 'type': 'String=csv,json', 'name': 'file_type', 'required': True, 'default': None, 'description': '文件类型 xls csv json'}, {'in': 'body', 'type': 'String', 'name': 'start_time', 'required': True, 'default': None, 'description': '开始时间'}, {'in': 'body', 'type': 'String', 'name': 'end_time', 'required': True, 'default': None, 'description': '结束时间'}, {'in': 'body', 'type': 'String=zh_CN,en_US', 'name': 'lang', 'required': False, 'default': 'zh_CN', 'description': '下载语言 zh_CN=中文 en_US=英文'})

    def __init__(self, task_name=_UNSET, is_use_template=_UNSET, data_source=_UNSET, download_fields=_UNSET, search_terms=_UNSET, file_type=_UNSET, start_time=_UNSET, end_time=_UNSET, template_id=_UNSET, lang='zh_CN', query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if task_name is not _UNSET:
            self.body['task_name'] = task_name
        if is_use_template is not _UNSET:
            self.body['is_use_template'] = is_use_template
        if data_source is not _UNSET:
            self.body['data_source'] = data_source
        if download_fields is not _UNSET:
            self.body['download_fields'] = download_fields
        if search_terms is not _UNSET:
            self.body['search_terms'] = search_terms
        if file_type is not _UNSET:
            self.body['file_type'] = file_type
        if start_time is not _UNSET:
            self.body['start_time'] = start_time
        if end_time is not _UNSET:
            self.body['end_time'] = end_time
        if template_id is not _UNSET:
            self.body['template_id'] = template_id
        self.body['lang'] = lang
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTaskCancelTaskRequest(BaseRequest):
    """取消日志下载任务.

    API: POST /api/v5/soc.log.download.task.cancel

    Parameters:
        task_id (Number, required): 任务ID.
    """
    API_NAME = 'LogDownloadTask_cancelTask'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/soc.log.download.task.cancel'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'task_id', 'required': True, 'default': None, 'description': '任务ID.'},)

    def __init__(self, task_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if task_id is not _UNSET:
            self.body['task_id'] = task_id
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTaskBatchCancelTaskRequest(BaseRequest):
    """批量取消日志下载任务.

    API: DELETE /api/v5/soc.log.download.task.batch.cancel

    Parameters:
        task_ids (String[], required): 任务IDs
    """
    API_NAME = 'LogDownloadTask_batchCancelTask'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/soc.log.download.task.batch.cancel'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'task_ids', 'required': True, 'default': None, 'description': '任务IDs'},)

    def __init__(self, task_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if task_ids is not _UNSET:
            self.body['task_ids'] = task_ids
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTaskDeleteTaskRequest(BaseRequest):
    """删除日志下载任务.

    API: DELETE /api/v5/soc.log.download.task.del

    Parameters:
        task_id (Number, required): 任务ID.
    """
    API_NAME = 'LogDownloadTask_deleteTask'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/soc.log.download.task.del'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'task_id', 'required': True, 'default': None, 'description': '任务ID.'},)

    def __init__(self, task_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if task_id is not _UNSET:
            self.body['task_id'] = task_id
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTaskBatchDeleteTaskRequest(BaseRequest):
    """批量删除日志下载任务.

    API: DELETE /api/v5/soc.log.download.task.batch.del

    Parameters:
        task_ids (String[], required): 任务IDs
    """
    API_NAME = 'LogDownloadTask_batchDeleteTask'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/soc.log.download.task.batch.del'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'task_ids', 'required': True, 'default': None, 'description': '任务IDs'},)

    def __init__(self, task_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if task_ids is not _UNSET:
            self.body['task_ids'] = task_ids
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTaskRegenerateTaskRequest(BaseRequest):
    """重新生成日志下载任务.

    API: POST /api/v5/soc.log.download.task.regenerate

    Parameters:
        task_id (Number, required): 任务ID.
    """
    API_NAME = 'LogDownloadTask_regenerateTask'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/soc.log.download.task.regenerate'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'task_id', 'required': True, 'default': None, 'description': '任务ID.'},)

    def __init__(self, task_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if task_id is not _UNSET:
            self.body['task_id'] = task_id
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadFieldConfDownloadFieldsRequest(BaseRequest):
    """查询日志下载字段列表.

    API: GET /api/v5/soc.log.download.fields
    """
    API_NAME = 'LogDownloadFieldConf_downloadFields'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/soc.log.download.fields'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class LogDownloadTemplateTemplateListRequest(BaseRequest):
    """查询日志下载模板列表.

    API: POST/GET /api/v5/soc.log.download.template.list
    """
    API_NAME = 'LogDownloadTemplate_templateList'
    METHOD = 'POST'
    METHODS = ('POST', 'GET')
    PATH = '/api/v5/soc.log.download.template.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTemplateGetTemplateDomainListRequest(BaseRequest):
    """查询日志下载模板选择域名列表.

    API: GET /api/v5/soc.log.download.template.domain.list
    """
    API_NAME = 'LogDownloadTemplate_getTemplateDomainList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/soc.log.download.template.domain.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class LogDownloadTemplateAddTemplateRequest(BaseRequest):
    """新增日志下载模板.

    API: POST /api/v5/soc.log.download.template.add

    Parameters:
        template_name (String, required): 模板名称
        group_name (String, required): 分Group Name
        group_id (Number, required): 分组ID
        data_source (String, required): 数据来源 ng，cc，waf
        status (Number, required): 状态 启用1 禁用0 默认1
        download_fields (String[], required): 下载字段
        search_terms (Object[], required): 限制字段 搜索条件
        domain_select_type (Number, required): 域名选中状态  0.局部选中 1.全
    """
    API_NAME = 'LogDownloadTemplate_addTemplate'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/soc.log.download.template.add'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'template_name', 'required': True, 'default': None, 'description': '模板名称'}, {'in': 'body', 'type': 'String', 'name': 'group_name', 'required': True, 'default': None, 'description': '分Group Name'}, {'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': True, 'default': None, 'description': '分组ID'}, {'in': 'body', 'type': 'String', 'name': 'data_source', 'required': True, 'default': None, 'description': '数据来源 ng，cc，waf'}, {'in': 'body', 'type': 'Number', 'name': 'status', 'required': True, 'default': None, 'description': '状态 启用1 禁用0 默认1'}, {'in': 'body', 'type': 'String[]', 'name': 'download_fields', 'required': True, 'default': None, 'description': '下载字段'}, {'in': 'body', 'type': 'Object[]', 'name': 'search_terms', 'required': True, 'default': None, 'description': '限制字段 搜索条件'}, {'in': 'body', 'type': 'Number', 'name': 'domain_select_type', 'required': True, 'default': None, 'description': '域名选中状态  0.局部选中 1.全'})

    def __init__(self, template_name=_UNSET, group_name=_UNSET, group_id=_UNSET, data_source=_UNSET, status=_UNSET, download_fields=_UNSET, search_terms=_UNSET, domain_select_type=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if template_name is not _UNSET:
            self.body['template_name'] = template_name
        if group_name is not _UNSET:
            self.body['group_name'] = group_name
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if data_source is not _UNSET:
            self.body['data_source'] = data_source
        if status is not _UNSET:
            self.body['status'] = status
        if download_fields is not _UNSET:
            self.body['download_fields'] = download_fields
        if search_terms is not _UNSET:
            self.body['search_terms'] = search_terms
        if domain_select_type is not _UNSET:
            self.body['domain_select_type'] = domain_select_type
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTemplateSaveTemplateRequest(BaseRequest):
    """修改日志下载模板.

    API: POST /api/v5/soc.log.download.template.save

    Parameters:
        template_id (Number, required): 模板ID
        template_name (String, required): 模板名称
        group_name (String, required): 分Group Name
        group_id (Number, required): 分组ID
        data_source (String, required): 数据来源 ng，cc，waf
        status (Number=0,1, optional, default=1): 状态 启用1 禁用0 默认1
        download_fields (String[], required): 下载字段
        search_terms (String[], required): 限制字段 搜索条件
    """
    API_NAME = 'LogDownloadTemplate_saveTemplate'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/soc.log.download.template.save'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'template_id', 'required': True, 'default': None, 'description': '模板ID'}, {'in': 'body', 'type': 'String', 'name': 'template_name', 'required': True, 'default': None, 'description': '模板名称'}, {'in': 'body', 'type': 'String', 'name': 'group_name', 'required': True, 'default': None, 'description': '分Group Name'}, {'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': True, 'default': None, 'description': '分组ID'}, {'in': 'body', 'type': 'String', 'name': 'data_source', 'required': True, 'default': None, 'description': '数据来源 ng，cc，waf'}, {'in': 'body', 'type': 'Number=0,1', 'name': 'status', 'required': False, 'default': '1', 'description': '状态 启用1 禁用0 默认1'}, {'in': 'body', 'type': 'String[]', 'name': 'download_fields', 'required': True, 'default': None, 'description': '下载字段'}, {'in': 'body', 'type': 'String[]', 'name': 'search_terms', 'required': True, 'default': None, 'description': '限制字段 搜索条件'})

    def __init__(self, template_id=_UNSET, template_name=_UNSET, group_name=_UNSET, group_id=_UNSET, data_source=_UNSET, download_fields=_UNSET, search_terms=_UNSET, status=1, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if template_id is not _UNSET:
            self.body['template_id'] = template_id
        if template_name is not _UNSET:
            self.body['template_name'] = template_name
        if group_name is not _UNSET:
            self.body['group_name'] = group_name
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if data_source is not _UNSET:
            self.body['data_source'] = data_source
        if download_fields is not _UNSET:
            self.body['download_fields'] = download_fields
        if search_terms is not _UNSET:
            self.body['search_terms'] = search_terms
        self.body['status'] = status
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTemplateDelTemplateRequest(BaseRequest):
    """删除日志下载模板.

    API: DELETE /api/v5/soc.log.download.template.del

    Parameters:
        template_id (Number, required): 组ID.
    """
    API_NAME = 'LogDownloadTemplate_delTemplate'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/soc.log.download.template.del'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'template_id', 'required': True, 'default': None, 'description': '组ID.'},)

    def __init__(self, template_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if template_id is not _UNSET:
            self.body['template_id'] = template_id
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTemplateBatchDelTemplateRequest(BaseRequest):
    """批量删除日志下载模板.

    API: DELETE /api/v5/soc.log.download.template.batch.del

    Parameters:
        template_ids (String[], required): 组ID
    """
    API_NAME = 'LogDownloadTemplate_batchDelTemplate'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/soc.log.download.template.batch.del'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'template_ids', 'required': True, 'default': None, 'description': '组ID'},)

    def __init__(self, template_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if template_ids is not _UNSET:
            self.body['template_ids'] = template_ids
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTemplateChangeStatusRequest(BaseRequest):
    """更改日志下载模板状态.

    API: POST /api/v5/soc.log.download.template.change.status

    Parameters:
        template_id (Number, required): 组ID.
        status (Number=0,1, required): 状态 1 开启 0禁用.
    """
    API_NAME = 'LogDownloadTemplate_changeStatus'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/soc.log.download.template.change.status'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'template_id', 'required': True, 'default': None, 'description': '组ID.'}, {'in': 'body', 'type': 'Number=0,1', 'name': 'status', 'required': True, 'default': None, 'description': '状态 1 开启 0禁用.'})

    def __init__(self, template_id=_UNSET, status=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if template_id is not _UNSET:
            self.body['template_id'] = template_id
        if status is not _UNSET:
            self.body['status'] = status
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTemplateBatchChangeStatusRequest(BaseRequest):
    """批量更改日志下载模板状态.

    API: POST /api/v5/soc.log.download.template.batch.change.status

    Parameters:
        template_ids (String[], required): 组ID
        status (Number=0,1, required): 状态 1 开启 0禁用
    """
    API_NAME = 'LogDownloadTemplate_batchChangeStatus'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/soc.log.download.template.batch.change.status'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'template_ids', 'required': True, 'default': None, 'description': '组ID'}, {'in': 'body', 'type': 'Number=0,1', 'name': 'status', 'required': True, 'default': None, 'description': '状态 1 开启 0禁用'})

    def __init__(self, template_ids=_UNSET, status=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if template_ids is not _UNSET:
            self.body['template_ids'] = template_ids
        if status is not _UNSET:
            self.body['status'] = status
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTemplateAllTemplateRequest(BaseRequest):
    """查询日志下载模板列表（添加任务时使用）.

    API: POST/GET /api/v5/soc.log.download.template.all
    """
    API_NAME = 'LogDownloadTemplate_allTemplate'
    METHOD = 'POST'
    METHODS = ('POST', 'GET')
    PATH = '/api/v5/soc.log.download.template.all'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.body[key] = value


class LogDownloadTemplateAllTemplateGroupRequest(BaseRequest):
    """查询日志下载模板分组列表（搜索或添加模板使用）.

    API: POST/GET /api/v5/soc.log.download.template.group.all
    """
    API_NAME = 'LogDownloadTemplate_allTemplateGroup'
    METHOD = 'POST'
    METHODS = ('POST', 'GET')
    PATH = '/api/v5/soc.log.download.template.group.all'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdPlusPackageGetMemberPackageListRequest(BaseRequest):
    """查询独享IP资源包列表.

    API: GET /api/v5/Tjkd.plus.package.list
    """
    API_NAME = 'TjkdPlusPackage_getMemberPackageList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Tjkd.plus.package.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class TjkdPlusPackageGetAllPackageRequest(BaseRequest):
    """查询独享IP资源包列表(简).

    API: GET /api/v5/Tjkd.plus.package.all
    """
    API_NAME = 'TjkdPlusPackage_getAllPackage'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Tjkd.plus.package.all'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class TjkdPlusPackageGetPackageInfoRequest(BaseRequest):
    """查询独享IP资源包详情.

    API: GET /api/v5/tjkd.plus.package.info
    """
    API_NAME = 'TjkdPlusPackage_getPackageInfo'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/tjkd.plus.package.info'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class TjkdPlusPackageGetPackageIpListRequest(BaseRequest):
    """查询独享IP资源包IP列表.

    API: GET /api/v5/Tjkd.plus.package.ip.list
    """
    API_NAME = 'TjkdPlusPackage_getPackageIpList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Tjkd.plus.package.ip.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class TjkdPlusPackageGetPackageOverviewRequest(BaseRequest):
    """独享IP资源包总览.

    API: GET /api/v5/Tjkd.plus.package.overview
    """
    API_NAME = 'TjkdPlusPackage_getPackageOverview'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Tjkd.plus.package.overview'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class TjkdPlusPackageGetPackagePortListRequest(BaseRequest):
    """查询独享IP资源包的转发端口列表.

    API: GET /api/v5/tjkd.plus.package.port.list
    """
    API_NAME = 'TjkdPlusPackage_getPackagePortList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/tjkd.plus.package.port.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class TjkdPlusPackageSavePackageRequest(BaseRequest):
    """修改独享IP资源包名称.

    API: POST /api/v5/tjkd.plus.package.save
    """
    API_NAME = 'TjkdPlusPackage_savePackage'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/tjkd.plus.package.save'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdPlusPackageSavePackageHealthyConfRequest(BaseRequest):
    """保存独享IP资源包回源配置.

    API: POST /api/v5/tjkd.plus.package.save.healthy.conf

    Parameters:
        package_id (Number, optional): 套餐ID
        fails_timeout (Number, required): 回源失败统计时间
        max_fails (Number, required): 回源失败次数统计
        keep_new_src_time (Number, required): 源站IP保持时间
    """
    API_NAME = 'TjkdPlusPackage_savePackageHealthyConf'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/tjkd.plus.package.save.healthy.conf'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'package_id', 'required': False, 'default': None, 'description': '套餐ID'}, {'in': 'body', 'type': 'Number', 'name': 'fails_timeout', 'required': True, 'default': None, 'description': '回源失败统计时间'}, {'in': 'body', 'type': 'Number', 'name': 'max_fails', 'required': True, 'default': None, 'description': '回源失败次数统计'}, {'in': 'body', 'type': 'Number', 'name': 'keep_new_src_time', 'required': True, 'default': None, 'description': '源站IP保持时间'})

    def __init__(self, fails_timeout=_UNSET, max_fails=_UNSET, keep_new_src_time=_UNSET, package_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if fails_timeout is not _UNSET:
            self.body['fails_timeout'] = fails_timeout
        if max_fails is not _UNSET:
            self.body['max_fails'] = max_fails
        if keep_new_src_time is not _UNSET:
            self.body['keep_new_src_time'] = keep_new_src_time
        if package_id is not _UNSET:
            self.body['package_id'] = package_id
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdPlusForwardRuleSavePlusForwardRuleRequest(BaseRequest):
    """保存转发规则.

    API: POST /api/v5/Tjkd.plus.forward.rule.save

    Parameters:
        package_id (Number, required): 套餐ID
        protocol (Number=1,2, required): 协议 1tcp 2udp
        protocol_port (Number, required): 端口号
        loading (Number=1,2, required): 负载均衡 1轮询 2ip哈希
        source_ip (String[], required): 源IP
        source_port (String[], required): 源端口
        backup (String[], required): 主备 1主 2备
        source_type (Number=1,2, required): 源类型 1IP 2域名
        actions (string=add,edit, required): 方式 add添加 edit编辑
        remark (string, required): 备注
        protocol_port_old (Number, optional): 端口号(编辑是旧，添加时候可不传）
    """
    API_NAME = 'TjkdPlusForwardRule_savePlusForwardRule'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/Tjkd.plus.forward.rule.save'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'package_id', 'required': True, 'default': None, 'description': '套餐ID'}, {'in': 'body', 'type': 'Number=1,2', 'name': 'protocol', 'required': True, 'default': None, 'description': '协议 1tcp 2udp'}, {'in': 'body', 'type': 'Number', 'name': 'protocol_port', 'required': True, 'default': None, 'description': '端口号'}, {'in': 'body', 'type': 'Number=1,2', 'name': 'loading', 'required': True, 'default': None, 'description': '负载均衡 1轮询 2ip哈希'}, {'in': 'body', 'type': 'String[]', 'name': 'source_ip', 'required': True, 'default': None, 'description': '源IP'}, {'in': 'body', 'type': 'String[]', 'name': 'source_port', 'required': True, 'default': None, 'description': '源端口'}, {'in': 'body', 'type': 'String[]', 'name': 'backup', 'required': True, 'default': None, 'description': '主备 1主 2备'}, {'in': 'body', 'type': 'Number=1,2', 'name': 'source_type', 'required': True, 'default': None, 'description': '源类型 1IP 2域名'}, {'in': 'body', 'type': 'string=add,edit', 'name': 'actions', 'required': True, 'default': None, 'description': '方式 add添加 edit编辑'}, {'in': 'body', 'type': 'string', 'name': 'remark', 'required': True, 'default': None, 'description': '备注'}, {'in': 'body', 'type': 'Number', 'name': 'protocol_port_old', 'required': False, 'default': None, 'description': '端口号(编辑是旧，添加时候可不传）'})

    def __init__(self, package_id=_UNSET, protocol=_UNSET, protocol_port=_UNSET, loading=_UNSET, source_ip=_UNSET, source_port=_UNSET, backup=_UNSET, source_type=_UNSET, actions=_UNSET, remark=_UNSET, protocol_port_old=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if package_id is not _UNSET:
            self.body['package_id'] = package_id
        if protocol is not _UNSET:
            self.body['protocol'] = protocol
        if protocol_port is not _UNSET:
            self.body['protocol_port'] = protocol_port
        if loading is not _UNSET:
            self.body['loading'] = loading
        if source_ip is not _UNSET:
            self.body['source_ip'] = source_ip
        if source_port is not _UNSET:
            self.body['source_port'] = source_port
        if backup is not _UNSET:
            self.body['backup'] = backup
        if source_type is not _UNSET:
            self.body['source_type'] = source_type
        if actions is not _UNSET:
            self.body['actions'] = actions
        if remark is not _UNSET:
            self.body['remark'] = remark
        if protocol_port_old is not _UNSET:
            self.body['protocol_port_old'] = protocol_port_old
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdPlusForwardRuleBatchAddPlusForwardRuleRequest(BaseRequest):
    """添加转发规则.

    API: POST /api/v5/Tjkd.plus.forward.rule.batch.add

    Parameters:
        package_id (Number, required): 套餐ID
        protocol (Number, required): 协议 1 tcp 2 udp
        source_type (Number, required): 源类型 1 IP 2 域名
        protocol_port (String[], required): 端口号
        loading (Number, required): 负载均衡 1 轮询 2 ip哈希
        source_ip (String[], required): 源IP
        backup (String[], required): 主备 1主 2备
        remark (String, required): 备注
    """
    API_NAME = 'TjkdPlusForwardRule_batchAddPlusForwardRule'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/Tjkd.plus.forward.rule.batch.add'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'package_id', 'required': True, 'default': None, 'description': '套餐ID'}, {'in': 'body', 'type': 'Number', 'name': 'protocol', 'required': True, 'default': None, 'description': '协议 1 tcp 2 udp'}, {'in': 'body', 'type': 'Number', 'name': 'source_type', 'required': True, 'default': None, 'description': '源类型 1 IP 2 域名'}, {'in': 'body', 'type': 'String[]', 'name': 'protocol_port', 'required': True, 'default': None, 'description': '端口号'}, {'in': 'body', 'type': 'Number', 'name': 'loading', 'required': True, 'default': None, 'description': '负载均衡 1 轮询 2 ip哈希'}, {'in': 'body', 'type': 'String[]', 'name': 'source_ip', 'required': True, 'default': None, 'description': '源IP'}, {'in': 'body', 'type': 'String[]', 'name': 'backup', 'required': True, 'default': None, 'description': '主备 1主 2备'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': True, 'default': None, 'description': '备注'})

    def __init__(self, package_id=_UNSET, protocol=_UNSET, source_type=_UNSET, protocol_port=_UNSET, loading=_UNSET, source_ip=_UNSET, backup=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if package_id is not _UNSET:
            self.body['package_id'] = package_id
        if protocol is not _UNSET:
            self.body['protocol'] = protocol
        if source_type is not _UNSET:
            self.body['source_type'] = source_type
        if protocol_port is not _UNSET:
            self.body['protocol_port'] = protocol_port
        if loading is not _UNSET:
            self.body['loading'] = loading
        if source_ip is not _UNSET:
            self.body['source_ip'] = source_ip
        if backup is not _UNSET:
            self.body['backup'] = backup
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdPlusForwardRuleBatchSavePlusForwardRuleRequest(BaseRequest):
    """修改转发规则(批量).

    API: POST /api/v5/Tjkd.plus.forward.rule.batch.save

    Parameters:
        package_id (Number, required): 套餐ID
        protocol (Number, required): 协议 1 tcp 2 udp
        source_type (Number, required): 源类型 1 IP 2 域名
        protocol_port (String[], required): 端口号
        loading (Number, required): 负载均衡 1 轮询 2 ip哈希
        source_ip (String[], required): 源IP
        backup (String[], required): 主备 1 主2 备
        protocol_port_old (String[], required): 旧端口号
        remark (String, required): 备注
    """
    API_NAME = 'TjkdPlusForwardRule_batchSavePlusForwardRule'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/Tjkd.plus.forward.rule.batch.save'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'package_id', 'required': True, 'default': None, 'description': '套餐ID'}, {'in': 'body', 'type': 'Number', 'name': 'protocol', 'required': True, 'default': None, 'description': '协议 1 tcp 2 udp'}, {'in': 'body', 'type': 'Number', 'name': 'source_type', 'required': True, 'default': None, 'description': '源类型 1 IP 2 域名'}, {'in': 'body', 'type': 'String[]', 'name': 'protocol_port', 'required': True, 'default': None, 'description': '端口号'}, {'in': 'body', 'type': 'Number', 'name': 'loading', 'required': True, 'default': None, 'description': '负载均衡 1 轮询 2 ip哈希'}, {'in': 'body', 'type': 'String[]', 'name': 'source_ip', 'required': True, 'default': None, 'description': '源IP'}, {'in': 'body', 'type': 'String[]', 'name': 'backup', 'required': True, 'default': None, 'description': '主备 1 主2 备'}, {'in': 'body', 'type': 'String[]', 'name': 'protocol_port_old', 'required': True, 'default': None, 'description': '旧端口号'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': True, 'default': None, 'description': '备注'})

    def __init__(self, package_id=_UNSET, protocol=_UNSET, source_type=_UNSET, protocol_port=_UNSET, loading=_UNSET, source_ip=_UNSET, backup=_UNSET, protocol_port_old=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if package_id is not _UNSET:
            self.body['package_id'] = package_id
        if protocol is not _UNSET:
            self.body['protocol'] = protocol
        if source_type is not _UNSET:
            self.body['source_type'] = source_type
        if protocol_port is not _UNSET:
            self.body['protocol_port'] = protocol_port
        if loading is not _UNSET:
            self.body['loading'] = loading
        if source_ip is not _UNSET:
            self.body['source_ip'] = source_ip
        if backup is not _UNSET:
            self.body['backup'] = backup
        if protocol_port_old is not _UNSET:
            self.body['protocol_port_old'] = protocol_port_old
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdPlusForwardRuleDelPlusForwardRuleRequest(BaseRequest):
    """删除转发规则.

    API: DELETE /api/v5/Tjkd.plus.forward.rule.del

    Parameters:
        ids (Number[], required): 
    """
    API_NAME = 'TjkdPlusForwardRule_delPlusForwardRule'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/Tjkd.plus.forward.rule.del'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'ids', 'required': True, 'default': None, 'description': ''},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdPlusForwardRuleGetPlusForwardRuleListRequest(BaseRequest):
    """查询转发规则列表.

    API: GET /api/v5/Tjkd.plus.forward.rule.list
    """
    API_NAME = 'TjkdPlusForwardRule_getPlusForwardRuleList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Tjkd.plus.forward.rule.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class TjkdPlusForwardRuleGetBatchPlusForwardRuleInfoRequest(BaseRequest):
    """查询转发规则列表.

    API: POST /api/v5/Tjkd.plus.forward.rule.batch.info

    Parameters:
        ids (Number[], required): 规则ID 数组
    """
    API_NAME = 'TjkdPlusForwardRule_getBatchPlusForwardRuleInfo'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/Tjkd.plus.forward.rule.batch.info'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'ids', 'required': True, 'default': None, 'description': '规则ID 数组'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdPlusPackageGetPackageDomainListRequest(BaseRequest):
    """查询使用独享IP资源包的域名列表(简).

    API: GET /api/v5/Tjkd.plus.package.domain.list
    """
    API_NAME = 'TjkdPlusPackage_getPackageDomainList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Tjkd.plus.package.domain.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class TjkdPlusDomainGetTjkdPlusDomainListRequest(BaseRequest):
    """查询使用独享IP资源包的域名列表.

    API: GET /api/v5/Tjkd.plus.domain.list
    """
    API_NAME = 'TjkdPlusDomain_getTjkdPlusDomainList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/Tjkd.plus.domain.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class TjkdPlusDomainAddTjkdPlusDomainRequest(BaseRequest):
    """域名绑定独享IP资源包.

    API: POST /api/v5/Tjkd.plus.domain.add

    Parameters:
        package_id (Number, required): 套餐ID
        domain_id (Number, required): 域名ID
    """
    API_NAME = 'TjkdPlusDomain_addTjkdPlusDomain'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/Tjkd.plus.domain.add'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'package_id', 'required': True, 'default': None, 'description': '套餐ID'}, {'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': True, 'default': None, 'description': '域名ID'})

    def __init__(self, package_id=_UNSET, domain_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if package_id is not _UNSET:
            self.body['package_id'] = package_id
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdPlusDomainDelTjkdPlusDomainRequest(BaseRequest):
    """域名解绑独享IP资源包.

    API: DELETE /api/v5/Tjkd.plus.domain.del

    Parameters:
        package_domain_ids (String[], required): 域名ID数组
        package_domains (String[], required): 域名数组，与package_domain_ids二选一，如果同时存在，只取package_domain_ids的值
        ignore_not_exists_domain (String, required): 是否忽略不存在的域名：on/off(默认)，与package_domains配合使用
    """
    API_NAME = 'TjkdPlusDomain_delTjkdPlusDomain'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/Tjkd.plus.domain.del'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'package_domain_ids', 'required': True, 'default': None, 'description': '域名ID数组'}, {'in': 'body', 'type': 'String[]', 'name': 'package_domains', 'required': True, 'default': None, 'description': '域名数组，与package_domain_ids二选一，如果同时存在，只取package_domain_ids的值'}, {'in': 'body', 'type': 'String', 'name': 'ignore_not_exists_domain', 'required': True, 'default': None, 'description': '是否忽略不存在的域名：on/off(默认)，与package_domains配合使用'})

    def __init__(self, package_domain_ids=_UNSET, package_domains=_UNSET, ignore_not_exists_domain=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if package_domain_ids is not _UNSET:
            self.body['package_domain_ids'] = package_domain_ids
        if package_domains is not _UNSET:
            self.body['package_domains'] = package_domains
        if ignore_not_exists_domain is not _UNSET:
            self.body['ignore_not_exists_domain'] = ignore_not_exists_domain
        for key, value in kwargs.items():
            self.body[key] = value


class NetworkSpeedGetCacheRuleListRequest(BaseRequest):
    """获取缓存规则列表.

    API: GET /api/v5/ruletpl/cache/rules
    """
    API_NAME = 'NetworkSpeedGetCacheRuleList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/ruletpl/cache/rules'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class NetworkSpeedCreateCacheRuleRequest(BaseRequest):
    """创建缓存规则.

    API: POST /api/v5/ruletpl/cache/rules

    Parameters:
        business_id (Number, required): 业务ID
        business_type (String="domain","tpl", required): 业务类型 (domain 域名, tpl 模版)
        name (String, required): 规则名称
        expr (String, required): wirefilter 规则
        remark (String, optional): 规则备注
        conf (Object, required): 配置信息
        conf.nocache (Boolean, required): 缓存资格 (true:绕过缓存, false:缓存)
        conf.cache_rule (Object, optional): 边缘TTL缓存
        conf.cache_rule.cachetime (Number, required): 缓存时间
        conf.cache_rule.action (String="default" "nocache" "cachetime" "force", optional): 缓存动作
        conf.browser_cache_rule (Object, optional): 浏览器缓存
        conf.browser_cache_rule.cachetime (Number, required): 缓存时间
        conf.browser_cache_rule.ignore_cache_time (Boolean, required): 忽略源站缓存时间(cache-control)
        conf.browser_cache_rule.nocache (Boolean, required): 是否缓存
        conf.cache_errstatus (Array, optional): 状态码缓存配置
        conf.cache_errstatus.cachetime (Number, required): 状态码缓存时间
        conf.cache_errstatus.err_status (Number[], required): 状态码数组
        conf.cache_url_rewrite (Object, optional): 自定义 cache key
        conf.cache_url_rewrite.sort_args (Boolean, required): 参数排序
        conf.cache_url_rewrite.ignore_case (Boolean, required): 忽略大小写
        conf.cache_url_rewrite.queries (Object, optional): 查询字符串处理
        conf.cache_url_rewrite.queries.args_method (String="SAVE","DEL","IGNORE","CUT", required): 动作
        conf.cache_url_rewrite.queries.items (String[], required): 参数key
        conf.cache_url_rewrite.cookies (Object, optional): Cookie处理
        conf.cache_url_rewrite.cookies.args_method (String="SAVE","DEL","IGNORE","CUT", required): 动作
        conf.cache_url_rewrite.cookies.items (String[], required): Cookie key
        conf.cache_share (Object, required): 缓存共用
        conf.cache_share.scheme (String="http","https", required): HTTP/HTTPS缓存共用方式
    """
    API_NAME = 'NetworkSpeedCreateCacheRule'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/ruletpl/cache/rules'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '业务ID'}, {'in': 'body', 'type': 'String="domain","tpl"', 'name': 'business_type', 'required': True, 'default': None, 'description': '业务类型 (domain 域名, tpl 模版)'}, {'in': 'body', 'type': 'String', 'name': 'name', 'required': True, 'default': None, 'description': '规则名称'}, {'in': 'body', 'type': 'String', 'name': 'expr', 'required': True, 'default': None, 'description': 'wirefilter 规则'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '规则备注'}, {'in': 'body', 'type': 'Object', 'name': 'conf', 'required': True, 'default': None, 'description': '配置信息'}, {'in': 'body', 'type': 'Boolean', 'name': 'conf.nocache', 'required': True, 'default': None, 'description': '缓存资格 (true:绕过缓存, false:缓存)'}, {'in': 'body', 'type': 'Object', 'name': 'conf.cache_rule', 'required': False, 'default': None, 'description': '边缘TTL缓存'}, {'in': 'body', 'type': 'Number', 'name': 'conf.cache_rule.cachetime', 'required': True, 'default': None, 'description': '缓存时间'}, {'in': 'body', 'type': 'String="default" "nocache" "cachetime" "force"', 'name': 'conf.cache_rule.action', 'required': False, 'default': None, 'description': '缓存动作'}, {'in': 'body', 'type': 'Object', 'name': 'conf.browser_cache_rule', 'required': False, 'default': None, 'description': '浏览器缓存'}, {'in': 'body', 'type': 'Number', 'name': 'conf.browser_cache_rule.cachetime', 'required': True, 'default': None, 'description': '缓存时间'}, {'in': 'body', 'type': 'Boolean', 'name': 'conf.browser_cache_rule.ignore_cache_time', 'required': True, 'default': None, 'description': '忽略源站缓存时间(cache-control)'}, {'in': 'body', 'type': 'Boolean', 'name': 'conf.browser_cache_rule.nocache', 'required': True, 'default': None, 'description': '是否缓存'}, {'in': 'body', 'type': 'Array', 'name': 'conf.cache_errstatus', 'required': False, 'default': None, 'description': '状态码缓存配置'}, {'in': 'body', 'type': 'Number', 'name': 'conf.cache_errstatus.cachetime', 'required': True, 'default': None, 'description': '状态码缓存时间'}, {'in': 'body', 'type': 'Number[]', 'name': 'conf.cache_errstatus.err_status', 'required': True, 'default': None, 'description': '状态码数组'}, {'in': 'body', 'type': 'Object', 'name': 'conf.cache_url_rewrite', 'required': False, 'default': None, 'description': '自定义 cache key'}, {'in': 'body', 'type': 'Boolean', 'name': 'conf.cache_url_rewrite.sort_args', 'required': True, 'default': None, 'description': '参数排序'}, {'in': 'body', 'type': 'Boolean', 'name': 'conf.cache_url_rewrite.ignore_case', 'required': True, 'default': None, 'description': '忽略大小写'}, {'in': 'body', 'type': 'Object', 'name': 'conf.cache_url_rewrite.queries', 'required': False, 'default': None, 'description': '查询字符串处理'}, {'in': 'body', 'type': 'String="SAVE","DEL","IGNORE","CUT"', 'name': 'conf.cache_url_rewrite.queries.args_method', 'required': True, 'default': None, 'description': '动作'}, {'in': 'body', 'type': 'String[]', 'name': 'conf.cache_url_rewrite.queries.items', 'required': True, 'default': None, 'description': '参数key'}, {'in': 'body', 'type': 'Object', 'name': 'conf.cache_url_rewrite.cookies', 'required': False, 'default': None, 'description': 'Cookie处理'}, {'in': 'body', 'type': 'String="SAVE","DEL","IGNORE","CUT"', 'name': 'conf.cache_url_rewrite.cookies.args_method', 'required': True, 'default': None, 'description': '动作'}, {'in': 'body', 'type': 'String[]', 'name': 'conf.cache_url_rewrite.cookies.items', 'required': True, 'default': None, 'description': 'Cookie key'}, {'in': 'body', 'type': 'Object', 'name': 'conf.cache_share', 'required': True, 'default': None, 'description': '缓存共用'}, {'in': 'body', 'type': 'String="http","https"', 'name': 'conf.cache_share.scheme', 'required': True, 'default': None, 'description': 'HTTP/HTTPS缓存共用方式'})

    def __init__(self, business_id=_UNSET, business_type=_UNSET, name=_UNSET, expr=_UNSET, conf=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if business_type is not _UNSET:
            self.body['business_type'] = business_type
        if name is not _UNSET:
            self.body['name'] = name
        if expr is not _UNSET:
            self.body['expr'] = expr
        if conf is not _UNSET:
            self.body['conf'] = conf
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class NetworkSpeedUpdateCacheRuleRequest(BaseRequest):
    """编辑缓存规则.

    API: PUT /api/v5/ruletpl/cache/rule

    Parameters:
        id (Number, required): 规则ID
        name (String, optional): 规则名称
        remark (String, optional): 规则备注
    """
    API_NAME = 'NetworkSpeedUpdateCacheRule'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/ruletpl/cache/rule'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '规则ID'}, {'in': 'body', 'type': 'String', 'name': 'name', 'required': False, 'default': None, 'description': '规则名称'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '规则备注'})

    def __init__(self, id=_UNSET, name=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if name is not _UNSET:
            self.body['name'] = name
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class NetworkSpeedUpdateCacheRuleConfigRequest(BaseRequest):
    """编辑缓存规则配置.

    API: PUT /api/v5/ruletpl/cache/rule/conf

    Parameters:
        id (Number, required): 规则ID
        name (String, optional): 规则名称
        remark (String, optional): 规则备注
        expr (String, optional): wirefilter规则
        conf (Object, required): 配置信息
        conf.nocache (Boolean, required): 是否绕过缓存 (true:不缓存, false:缓存)
        conf.cache_rule (Object, optional): 边缘TTL缓存
        conf.cache_rule.cachetime (Number, required): 缓存时间
        conf.cache_rule.action (String="default" "nocache" "cachetime" "force", optional): 缓存动作
        conf.browser_cache_rule (Object, optional): 浏览器缓存设置
        conf.browser_cache_rule.cachetime (Number, required): 缓存时间 (秒)
        conf.browser_cache_rule.ignore_cache_time (Boolean, required): 忽略源站缓存时间(cache-control)
        conf.browser_cache_rule.nocache (Boolean, required): 是否缓存 (true:不缓存, false:缓存)
        conf.cache_errstatus (Array, optional): 状态码缓存配置数组
        conf.cache_errstatus.cachetime (Number, required): 状态码缓存时间
        conf.cache_errstatus.err_status (Number[], required): 状态码集合
        conf.cache_url_rewrite (Object, optional): 自定义 cache key 设置
        conf.cache_url_rewrite.sort_args (Boolean, required): 是否对参数排序
        conf.cache_url_rewrite.ignore_case (Boolean, required): 是否忽略大小写
        conf.cache_url_rewrite.queries (Object, required): 查询字符串处理
        conf.cache_url_rewrite.queries.args_method (String="SAVE","DEL","IGNORE","CUT", required): 动作类型
        conf.cache_url_rewrite.queries.items (String[], optional): 参数 key 列表
        conf.cache_url_rewrite.cookies (Object, required): Cookie 处理
        conf.cache_url_rewrite.cookies.args_method (String="SAVE","DEL","IGNORE","CUT", required): 动作类型
        conf.cache_url_rewrite.cookies.items (String[], optional): cookie key 列表
        conf.cache_share (Object, required): 缓存共用设置
        conf.cache_share.scheme (String="http","https", required): 缓存共用协议类型
    """
    API_NAME = 'NetworkSpeedUpdateCacheRuleConfig'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/ruletpl/cache/rule/conf'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '规则ID'}, {'in': 'body', 'type': 'String', 'name': 'name', 'required': False, 'default': None, 'description': '规则名称'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '规则备注'}, {'in': 'body', 'type': 'String', 'name': 'expr', 'required': False, 'default': None, 'description': 'wirefilter规则'}, {'in': 'body', 'type': 'Object', 'name': 'conf', 'required': True, 'default': None, 'description': '配置信息'}, {'in': 'body', 'type': 'Boolean', 'name': 'conf.nocache', 'required': True, 'default': None, 'description': '是否绕过缓存 (true:不缓存, false:缓存)'}, {'in': 'body', 'type': 'Object', 'name': 'conf.cache_rule', 'required': False, 'default': None, 'description': '边缘TTL缓存'}, {'in': 'body', 'type': 'Number', 'name': 'conf.cache_rule.cachetime', 'required': True, 'default': None, 'description': '缓存时间'}, {'in': 'body', 'type': 'String="default" "nocache" "cachetime" "force"', 'name': 'conf.cache_rule.action', 'required': False, 'default': None, 'description': '缓存动作'}, {'in': 'body', 'type': 'Object', 'name': 'conf.browser_cache_rule', 'required': False, 'default': None, 'description': '浏览器缓存设置'}, {'in': 'body', 'type': 'Number', 'name': 'conf.browser_cache_rule.cachetime', 'required': True, 'default': None, 'description': '缓存时间 (秒)'}, {'in': 'body', 'type': 'Boolean', 'name': 'conf.browser_cache_rule.ignore_cache_time', 'required': True, 'default': None, 'description': '忽略源站缓存时间(cache-control)'}, {'in': 'body', 'type': 'Boolean', 'name': 'conf.browser_cache_rule.nocache', 'required': True, 'default': None, 'description': '是否缓存 (true:不缓存, false:缓存)'}, {'in': 'body', 'type': 'Array', 'name': 'conf.cache_errstatus', 'required': False, 'default': None, 'description': '状态码缓存配置数组'}, {'in': 'body', 'type': 'Number', 'name': 'conf.cache_errstatus.cachetime', 'required': True, 'default': None, 'description': '状态码缓存时间'}, {'in': 'body', 'type': 'Number[]', 'name': 'conf.cache_errstatus.err_status', 'required': True, 'default': None, 'description': '状态码集合'}, {'in': 'body', 'type': 'Object', 'name': 'conf.cache_url_rewrite', 'required': False, 'default': None, 'description': '自定义 cache key 设置'}, {'in': 'body', 'type': 'Boolean', 'name': 'conf.cache_url_rewrite.sort_args', 'required': True, 'default': None, 'description': '是否对参数排序'}, {'in': 'body', 'type': 'Boolean', 'name': 'conf.cache_url_rewrite.ignore_case', 'required': True, 'default': None, 'description': '是否忽略大小写'}, {'in': 'body', 'type': 'Object', 'name': 'conf.cache_url_rewrite.queries', 'required': True, 'default': None, 'description': '查询字符串处理'}, {'in': 'body', 'type': 'String="SAVE","DEL","IGNORE","CUT"', 'name': 'conf.cache_url_rewrite.queries.args_method', 'required': True, 'default': None, 'description': '动作类型'}, {'in': 'body', 'type': 'String[]', 'name': 'conf.cache_url_rewrite.queries.items', 'required': False, 'default': None, 'description': '参数 key 列表'}, {'in': 'body', 'type': 'Object', 'name': 'conf.cache_url_rewrite.cookies', 'required': True, 'default': None, 'description': 'Cookie 处理'}, {'in': 'body', 'type': 'String="SAVE","DEL","IGNORE","CUT"', 'name': 'conf.cache_url_rewrite.cookies.args_method', 'required': True, 'default': None, 'description': '动作类型'}, {'in': 'body', 'type': 'String[]', 'name': 'conf.cache_url_rewrite.cookies.items', 'required': False, 'default': None, 'description': 'cookie key 列表'}, {'in': 'body', 'type': 'Object', 'name': 'conf.cache_share', 'required': True, 'default': None, 'description': '缓存共用设置'}, {'in': 'body', 'type': 'String="http","https"', 'name': 'conf.cache_share.scheme', 'required': True, 'default': None, 'description': '缓存共用协议类型'})

    def __init__(self, id=_UNSET, conf=_UNSET, name=_UNSET, remark=_UNSET, expr=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if conf is not _UNSET:
            self.body['conf'] = conf
        if name is not _UNSET:
            self.body['name'] = name
        if remark is not _UNSET:
            self.body['remark'] = remark
        if expr is not _UNSET:
            self.body['expr'] = expr
        for key, value in kwargs.items():
            self.body[key] = value


class NetworkSpeedUpdateCacheRuleStatusRequest(BaseRequest):
    """启用或禁用缓存规则.

    API: PUT /api/v5/ruletpl/cache/rule_status

    Parameters:
        business_id (Number, required): 业务ID (域名ID)
        business_type (String="domain","tpl", required): 业务类型 (domain域名 / tpl模版)
        ids (Number[], required): 规则ID数组
        status (Number=1,2, required): 状态: 1表示启用, 2表示禁用
    """
    API_NAME = 'NetworkSpeedUpdateCacheRuleStatus'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/ruletpl/cache/rule_status'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '业务ID (域名ID)'}, {'in': 'body', 'type': 'String="domain","tpl"', 'name': 'business_type', 'required': True, 'default': None, 'description': '业务类型 (domain域名 / tpl模版)'}, {'in': 'body', 'type': 'Number[]', 'name': 'ids', 'required': True, 'default': None, 'description': '规则ID数组'}, {'in': 'body', 'type': 'Number=1,2', 'name': 'status', 'required': True, 'default': None, 'description': '状态: 1表示启用, 2表示禁用'})

    def __init__(self, business_id=_UNSET, business_type=_UNSET, ids=_UNSET, status=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if business_type is not _UNSET:
            self.body['business_type'] = business_type
        if ids is not _UNSET:
            self.body['ids'] = ids
        if status is not _UNSET:
            self.body['status'] = status
        for key, value in kwargs.items():
            self.body[key] = value


class NetworkSpeedSortCacheRulesRequest(BaseRequest):
    """缓存规则排序.

    API: PUT /api/v5/ruletpl/cache/rule_sort

    Parameters:
        business_id (Number, required): 业务ID
        business_type (String="domain","tpl", required): 业务类型 (domain: 域名, tpl: 模版)
        ids (Number[], required): 排序后的规则ID数组 (顺序即为新排序)
    """
    API_NAME = 'NetworkSpeedSortCacheRules'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/ruletpl/cache/rule_sort'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '业务ID'}, {'in': 'body', 'type': 'String="domain","tpl"', 'name': 'business_type', 'required': True, 'default': None, 'description': '业务类型 (domain: 域名, tpl: 模版)'}, {'in': 'body', 'type': 'Number[]', 'name': 'ids', 'required': True, 'default': None, 'description': '排序后的规则ID数组 (顺序即为新排序)'})

    def __init__(self, business_id=_UNSET, business_type=_UNSET, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if business_type is not _UNSET:
            self.body['business_type'] = business_type
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class NetworkSpeedGetGlobalCacheConfigRequest(BaseRequest):
    """获取默认全局缓存配置.

    API: GET /api/v5/ruletpl/cache/global/conf
    """
    API_NAME = 'NetworkSpeedGetGlobalCacheConfig'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/ruletpl/cache/global/conf'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class NetworkSpeedDeleteCacheRuleRequest(BaseRequest):
    """删除缓存规则.

    API: DELETE /api/v5/ruletpl/cache/rule

    Parameters:
        business_id (Number, required): 业务ID
        business_type (String="domain","tpl", required): 业务类型 (domain 域名, tpl 模版)
        ids (Number[], required): 规则ID列表
    """
    API_NAME = 'NetworkSpeedDeleteCacheRule'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/ruletpl/cache/rule'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '业务ID'}, {'in': 'body', 'type': 'String="domain","tpl"', 'name': 'business_type', 'required': True, 'default': None, 'description': '业务类型 (domain 域名, tpl 模版)'}, {'in': 'body', 'type': 'Number[]', 'name': 'ids', 'required': True, 'default': None, 'description': '规则ID列表'})

    def __init__(self, business_id=_UNSET, business_type=_UNSET, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if business_type is not _UNSET:
            self.body['business_type'] = business_type
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class NetworkSpeedGetTemplateConfigRequest(BaseRequest):
    """获取模版配置.

    API: POST /api/v5/ruletpl/network_speed/get_conf

    Parameters:
        business_id (String, required): 业务ID
        business_type (String="tpl","global", required): 业务类型 (tpl模版, 全局)
        config_groups (String[], required): 配置项名称数组, 例如:
        upstream_check (Object, optional): 源站探测
        upstream_check.fails (Number, required): 连续不可用次数
        upstream_check.intval (Number, required): 探测频率 (秒)
        upstream_check.rise (Number, required): 连续可用次数
        upstream_check.status (String="on","off", required): 开关
        upstream_check.timeout (Number, required): TCP连接超时时间
        upstream_check.type (String="http","tcp", required): 探测类型 (如: http、tcp)
        upstream_check.op (String="HEAD","GET","AUTO", required): HTTP请求方法 (如: HEAD、GET、AUTO)
        upstream_check.path (String, required): HTTP请求路径 (如: /testpath
    """
    API_NAME = 'NetworkSpeedGetTemplateConfig'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/ruletpl/network_speed/get_conf'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'business_id', 'required': True, 'default': None, 'description': '业务ID'}, {'in': 'body', 'type': 'String="tpl","global"', 'name': 'business_type', 'required': True, 'default': None, 'description': '业务类型 (tpl模版, 全局)'}, {'in': 'body', 'type': 'String[]', 'name': 'config_groups', 'required': True, 'default': None, 'description': '配置项名称数组, 例如:'}, {'in': 'body', 'type': 'Object', 'name': 'upstream_check', 'required': False, 'default': None, 'description': '源站探测'}, {'in': 'body', 'type': 'Number', 'name': 'upstream_check.fails', 'required': True, 'default': None, 'description': '连续不可用次数'}, {'in': 'body', 'type': 'Number', 'name': 'upstream_check.intval', 'required': True, 'default': None, 'description': '探测频率 (秒)'}, {'in': 'body', 'type': 'Number', 'name': 'upstream_check.rise', 'required': True, 'default': None, 'description': '连续可用次数'}, {'in': 'body', 'type': 'String="on","off"', 'name': 'upstream_check.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'Number', 'name': 'upstream_check.timeout', 'required': True, 'default': None, 'description': 'TCP连接超时时间'}, {'in': 'body', 'type': 'String="http","tcp"', 'name': 'upstream_check.type', 'required': True, 'default': None, 'description': '探测类型 (如: http、tcp)'}, {'in': 'body', 'type': 'String="HEAD","GET","AUTO"', 'name': 'upstream_check.op', 'required': True, 'default': None, 'description': 'HTTP请求方法 (如: HEAD、GET、AUTO)'}, {'in': 'body', 'type': 'String', 'name': 'upstream_check.path', 'required': True, 'default': None, 'description': 'HTTP请求路径 (如: /testpath'})

    def __init__(self, business_id=_UNSET, business_type=_UNSET, config_groups=_UNSET, upstream_check=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if business_type is not _UNSET:
            self.body['business_type'] = business_type
        if config_groups is not _UNSET:
            self.body['config_groups'] = config_groups
        if upstream_check is not _UNSET:
            self.body['upstream_check'] = upstream_check
        for key, value in kwargs.items():
            self.body[key] = value


class NetworkSpeedUpdateTemplateConfigRequest(BaseRequest):
    """修改模版配置.

    API: PUT /api/v5/ruletpl/network_speed/conf

    Parameters:
        business_id (Number, required): 业务id
        business_type (String="tpl","global", required): 业务类型 (tpl模版, global全局)
        domain_proxy_conf (Object, optional): 回源配置
        domain_proxy_conf.proxy_connect_timeout (Number, required): 节点与源建连超时时间
        domain_proxy_conf.fails_timeout (Number, required): 回源失败统计时间间隔
        domain_proxy_conf.keep_new_src_time (Number, required): 回源失败禁用不可用IP时间
        domain_proxy_conf.max_fails (Number, required): 回源失败次数
        domain_proxy_conf.proxy_keepalive (Number, required): 回源保持长连接
        upstream_redirect (Object, optional): 回源跟随301/302配置
        upstream_redirect.status (String="on","off", required): 状态
        customized_req_headers (Object, optional): 自定义HTTP回源请求头
        customized_req_headers.status (String, required): 开关
        source_site_protect (Object, optional): 源站保护
        source_site_protect.num (Number, required): 次数
        source_site_protect.second (Number, required): 时间
        source_site_protect.status (String, required): 开关
        slice (Object, optional): Range回源
        slice.status (String, required): 开关
        https (Object, optional): HTTPS配置
        https.status (String, required): 开关
        https.http2https (String="off","all","special", required): HTTP跳转HTTPS策略
        https.http2 (String, required): HTTP2 开关
        https.min_version (String="SSLv3","TLSv1.0","TLSv1.1","TLSv1.2","TLSv1.3", required): 最小版本
        https.ocsp_stapling (String, required): OCSP状态
        https.http2https_port (Number, required): 跳转端口
        https.ciphers_preset (String="default","strong","custom", required): 加密套件预设
        https.custom_encrypt_algorithm (String[], required): 自定义算法套件
        https.hsts (String, required): HSTS
        page_gzip (Object, optional): Gzip压缩
        page_gzip.status (String, required): 开关
        webp (Object, optional): WebP压缩
        webp.status (String, required): 开关
        upload_file (Object, optional): 文件上传限制
        upload_file.upload_size (Number, required): 最大文件上传大小
        upload_file.upload_size_unit (String, required): 单位 (如: MB)
        websocket (Object, optional): WebSocket配置
        websocket.status (String, required): 开关
        mobile_jump (Object, optional): 移动端跳转
        mobile_jump.jump_url (String, required): 跳转地址
        mobile_jump.status (String, required): 开关
        custom_page (Object, optional): 错误页面定制
        custom_page.status (String, required): 开关
        upstream_uri_change (Object, optional): 回源URI改写
        upstream_uri_change.status (String, required): 开关
        resp_headers (Object, optional): 自定义HTTP响应头
        resp_headers.status (String, required): 开关
        upstream_check (Object, optional): 源站探测
        upstream_check.fails (Number, required): 连续不可用次数
        upstream_check.intval (Number, required): 探测频率 (秒)
        upstream_check.rise (Number, required): 连续可用次数
        upstream_check.status (String="on","off", required): 开关
        upstream_check.timeout (Number, required): TCP连接超时时间
        upstream_check.type (String="http","tcp", required): 探测类型 (如: http、tcp)
        upstream_check.op (String="HEAD","GET","AUTO", required): HTTP请求方法 (如: HEAD、GET、AUTO)
        upstream_check.path (String, required): HTTP请求路径 (如: /testpath
    """
    API_NAME = 'NetworkSpeedUpdateTemplateConfig'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/ruletpl/network_speed/conf'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '业务id'}, {'in': 'body', 'type': 'String="tpl","global"', 'name': 'business_type', 'required': True, 'default': None, 'description': '业务类型 (tpl模版, global全局)'}, {'in': 'body', 'type': 'Object', 'name': 'domain_proxy_conf', 'required': False, 'default': None, 'description': '回源配置'}, {'in': 'body', 'type': 'Number', 'name': 'domain_proxy_conf.proxy_connect_timeout', 'required': True, 'default': None, 'description': '节点与源建连超时时间'}, {'in': 'body', 'type': 'Number', 'name': 'domain_proxy_conf.fails_timeout', 'required': True, 'default': None, 'description': '回源失败统计时间间隔'}, {'in': 'body', 'type': 'Number', 'name': 'domain_proxy_conf.keep_new_src_time', 'required': True, 'default': None, 'description': '回源失败禁用不可用IP时间'}, {'in': 'body', 'type': 'Number', 'name': 'domain_proxy_conf.max_fails', 'required': True, 'default': None, 'description': '回源失败次数'}, {'in': 'body', 'type': 'Number', 'name': 'domain_proxy_conf.proxy_keepalive', 'required': True, 'default': None, 'description': '回源保持长连接'}, {'in': 'body', 'type': 'Object', 'name': 'upstream_redirect', 'required': False, 'default': None, 'description': '回源跟随301/302配置'}, {'in': 'body', 'type': 'String="on","off"', 'name': 'upstream_redirect.status', 'required': True, 'default': None, 'description': '状态'}, {'in': 'body', 'type': 'Object', 'name': 'customized_req_headers', 'required': False, 'default': None, 'description': '自定义HTTP回源请求头'}, {'in': 'body', 'type': 'String', 'name': 'customized_req_headers.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'Object', 'name': 'source_site_protect', 'required': False, 'default': None, 'description': '源站保护'}, {'in': 'body', 'type': 'Number', 'name': 'source_site_protect.num', 'required': True, 'default': None, 'description': '次数'}, {'in': 'body', 'type': 'Number', 'name': 'source_site_protect.second', 'required': True, 'default': None, 'description': '时间'}, {'in': 'body', 'type': 'String', 'name': 'source_site_protect.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'Object', 'name': 'slice', 'required': False, 'default': None, 'description': 'Range回源'}, {'in': 'body', 'type': 'String', 'name': 'slice.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'Object', 'name': 'https', 'required': False, 'default': None, 'description': 'HTTPS配置'}, {'in': 'body', 'type': 'String', 'name': 'https.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'String="off","all","special"', 'name': 'https.http2https', 'required': True, 'default': None, 'description': 'HTTP跳转HTTPS策略'}, {'in': 'body', 'type': 'String', 'name': 'https.http2', 'required': True, 'default': None, 'description': 'HTTP2 开关'}, {'in': 'body', 'type': 'String="SSLv3","TLSv1.0","TLSv1.1","TLSv1.2","TLSv1.3"', 'name': 'https.min_version', 'required': True, 'default': None, 'description': '最小版本'}, {'in': 'body', 'type': 'String', 'name': 'https.ocsp_stapling', 'required': True, 'default': None, 'description': 'OCSP状态'}, {'in': 'body', 'type': 'Number', 'name': 'https.http2https_port', 'required': True, 'default': None, 'description': '跳转端口'}, {'in': 'body', 'type': 'String="default","strong","custom"', 'name': 'https.ciphers_preset', 'required': True, 'default': None, 'description': '加密套件预设'}, {'in': 'body', 'type': 'String[]', 'name': 'https.custom_encrypt_algorithm', 'required': True, 'default': None, 'description': '自定义算法套件'}, {'in': 'body', 'type': 'String', 'name': 'https.hsts', 'required': True, 'default': None, 'description': 'HSTS'}, {'in': 'body', 'type': 'Object', 'name': 'page_gzip', 'required': False, 'default': None, 'description': 'Gzip压缩'}, {'in': 'body', 'type': 'String', 'name': 'page_gzip.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'Object', 'name': 'webp', 'required': False, 'default': None, 'description': 'WebP压缩'}, {'in': 'body', 'type': 'String', 'name': 'webp.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'Object', 'name': 'upload_file', 'required': False, 'default': None, 'description': '文件上传限制'}, {'in': 'body', 'type': 'Number', 'name': 'upload_file.upload_size', 'required': True, 'default': None, 'description': '最大文件上传大小'}, {'in': 'body', 'type': 'String', 'name': 'upload_file.upload_size_unit', 'required': True, 'default': None, 'description': '单位 (如: MB)'}, {'in': 'body', 'type': 'Object', 'name': 'websocket', 'required': False, 'default': None, 'description': 'WebSocket配置'}, {'in': 'body', 'type': 'String', 'name': 'websocket.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'Object', 'name': 'mobile_jump', 'required': False, 'default': None, 'description': '移动端跳转'}, {'in': 'body', 'type': 'String', 'name': 'mobile_jump.jump_url', 'required': True, 'default': None, 'description': '跳转地址'}, {'in': 'body', 'type': 'String', 'name': 'mobile_jump.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'Object', 'name': 'custom_page', 'required': False, 'default': None, 'description': '错误页面定制'}, {'in': 'body', 'type': 'String', 'name': 'custom_page.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'Object', 'name': 'upstream_uri_change', 'required': False, 'default': None, 'description': '回源URI改写'}, {'in': 'body', 'type': 'String', 'name': 'upstream_uri_change.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'Object', 'name': 'resp_headers', 'required': False, 'default': None, 'description': '自定义HTTP响应头'}, {'in': 'body', 'type': 'String', 'name': 'resp_headers.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'Object', 'name': 'upstream_check', 'required': False, 'default': None, 'description': '源站探测'}, {'in': 'body', 'type': 'Number', 'name': 'upstream_check.fails', 'required': True, 'default': None, 'description': '连续不可用次数'}, {'in': 'body', 'type': 'Number', 'name': 'upstream_check.intval', 'required': True, 'default': None, 'description': '探测频率 (秒)'}, {'in': 'body', 'type': 'Number', 'name': 'upstream_check.rise', 'required': True, 'default': None, 'description': '连续可用次数'}, {'in': 'body', 'type': 'String="on","off"', 'name': 'upstream_check.status', 'required': True, 'default': None, 'description': '开关'}, {'in': 'body', 'type': 'Number', 'name': 'upstream_check.timeout', 'required': True, 'default': None, 'description': 'TCP连接超时时间'}, {'in': 'body', 'type': 'String="http","tcp"', 'name': 'upstream_check.type', 'required': True, 'default': None, 'description': '探测类型 (如: http、tcp)'}, {'in': 'body', 'type': 'String="HEAD","GET","AUTO"', 'name': 'upstream_check.op', 'required': True, 'default': None, 'description': 'HTTP请求方法 (如: HEAD、GET、AUTO)'}, {'in': 'body', 'type': 'String', 'name': 'upstream_check.path', 'required': True, 'default': None, 'description': 'HTTP请求路径 (如: /testpath'})

    def __init__(self, business_id=_UNSET, business_type=_UNSET, domain_proxy_conf=_UNSET, upstream_redirect=_UNSET, customized_req_headers=_UNSET, source_site_protect=_UNSET, slice=_UNSET, https=_UNSET, page_gzip=_UNSET, webp=_UNSET, upload_file=_UNSET, websocket=_UNSET, mobile_jump=_UNSET, custom_page=_UNSET, upstream_uri_change=_UNSET, resp_headers=_UNSET, upstream_check=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if business_type is not _UNSET:
            self.body['business_type'] = business_type
        if domain_proxy_conf is not _UNSET:
            self.body['domain_proxy_conf'] = domain_proxy_conf
        if upstream_redirect is not _UNSET:
            self.body['upstream_redirect'] = upstream_redirect
        if customized_req_headers is not _UNSET:
            self.body['customized_req_headers'] = customized_req_headers
        if source_site_protect is not _UNSET:
            self.body['source_site_protect'] = source_site_protect
        if slice is not _UNSET:
            self.body['slice'] = slice
        if https is not _UNSET:
            self.body['https'] = https
        if page_gzip is not _UNSET:
            self.body['page_gzip'] = page_gzip
        if webp is not _UNSET:
            self.body['webp'] = webp
        if upload_file is not _UNSET:
            self.body['upload_file'] = upload_file
        if websocket is not _UNSET:
            self.body['websocket'] = websocket
        if mobile_jump is not _UNSET:
            self.body['mobile_jump'] = mobile_jump
        if custom_page is not _UNSET:
            self.body['custom_page'] = custom_page
        if upstream_uri_change is not _UNSET:
            self.body['upstream_uri_change'] = upstream_uri_change
        if resp_headers is not _UNSET:
            self.body['resp_headers'] = resp_headers
        if upstream_check is not _UNSET:
            self.body['upstream_check'] = upstream_check
        for key, value in kwargs.items():
            self.body[key] = value


class NetworkSpeedGetRulesRequest(BaseRequest):
    """获取配置规则列表.

    API: GET /api/v5/ruletpl/network_speed/rules
    """
    API_NAME = 'NetworkSpeedGetRules'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/ruletpl/network_speed/rules'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class NetworkSpeedCreateRuleRequest(BaseRequest):
    """创建配置规则.

    API: POST /api/v5/ruletpl/network_speed/rules

    Parameters:
        business_id (Number, required): 业务ID
        business_type (String, required): 业务类型
        config_group (String="custom_page","upstream_uri_change_rule","resp_headers_rule","customized_req_headers_rule", required): 规则分组
        custom_page (Object, optional): 错误页面定制
        upstream_uri_change_rule (Object, optional): 回源URI改写
        upstream_uri_change_rule.typ (String, required): 类型
        upstream_uri_change_rule.action (String, required): 动作
        upstream_uri_change_rule.match (String, required): 匹配值
        upstream_uri_change_rule.target (String, required): 目标值
        resp_headers_rule (Object, optional): 自定义响应头
        resp_headers_rule.type (String, required): 类型
        resp_headers_rule.content (String, required): 内容
        customized_req_headers_rule (Object, optional): 自定义回源请求头
        customized_req_headers_rule.type (String, required): 类型
        customized_req_headers_rule.content (String, required): 内容
    """
    API_NAME = 'NetworkSpeedCreateRule'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/ruletpl/network_speed/rules'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '业务ID'}, {'in': 'body', 'type': 'String', 'name': 'business_type', 'required': True, 'default': None, 'description': '业务类型'}, {'in': 'body', 'type': 'String="custom_page","upstream_uri_change_rule","resp_headers_rule","customized_req_headers_rule"', 'name': 'config_group', 'required': True, 'default': None, 'description': '规则分组'}, {'in': 'body', 'type': 'Object', 'name': 'custom_page', 'required': False, 'default': None, 'description': '错误页面定制'}, {'in': 'body', 'type': 'Object', 'name': 'upstream_uri_change_rule', 'required': False, 'default': None, 'description': '回源URI改写'}, {'in': 'body', 'type': 'String', 'name': 'upstream_uri_change_rule.typ', 'required': True, 'default': None, 'description': '类型'}, {'in': 'body', 'type': 'String', 'name': 'upstream_uri_change_rule.action', 'required': True, 'default': None, 'description': '动作'}, {'in': 'body', 'type': 'String', 'name': 'upstream_uri_change_rule.match', 'required': True, 'default': None, 'description': '匹配值'}, {'in': 'body', 'type': 'String', 'name': 'upstream_uri_change_rule.target', 'required': True, 'default': None, 'description': '目标值'}, {'in': 'body', 'type': 'Object', 'name': 'resp_headers_rule', 'required': False, 'default': None, 'description': '自定义响应头'}, {'in': 'body', 'type': 'String', 'name': 'resp_headers_rule.type', 'required': True, 'default': None, 'description': '类型'}, {'in': 'body', 'type': 'String', 'name': 'resp_headers_rule.content', 'required': True, 'default': None, 'description': '内容'}, {'in': 'body', 'type': 'Object', 'name': 'customized_req_headers_rule', 'required': False, 'default': None, 'description': '自定义回源请求头'}, {'in': 'body', 'type': 'String', 'name': 'customized_req_headers_rule.type', 'required': True, 'default': None, 'description': '类型'}, {'in': 'body', 'type': 'String', 'name': 'customized_req_headers_rule.content', 'required': True, 'default': None, 'description': '内容'})

    def __init__(self, business_id=_UNSET, business_type=_UNSET, config_group=_UNSET, upstream_uri_change_rule=_UNSET, resp_headers_rule=_UNSET, customized_req_headers_rule=_UNSET, custom_page=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if business_type is not _UNSET:
            self.body['business_type'] = business_type
        if config_group is not _UNSET:
            self.body['config_group'] = config_group
        if upstream_uri_change_rule is not _UNSET:
            self.body['upstream_uri_change_rule'] = upstream_uri_change_rule
        if resp_headers_rule is not _UNSET:
            self.body['resp_headers_rule'] = resp_headers_rule
        if customized_req_headers_rule is not _UNSET:
            self.body['customized_req_headers_rule'] = customized_req_headers_rule
        if custom_page is not _UNSET:
            self.body['custom_page'] = custom_page
        for key, value in kwargs.items():
            self.body[key] = value


class NetworkSpeedDeleteRuleRequest(BaseRequest):
    """删除配置规则.

    API: DELETE /api/v5/ruletpl/network_speed/rule

    Parameters:
        business_id (Number, required): 业务ID
        business_type (String, required): 业务类型
        config_group (String, required): 规则分组
        ids (Number[], required): 要删除的规则ID数组
    """
    API_NAME = 'NetworkSpeedDeleteRule'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/ruletpl/network_speed/rule'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '业务ID'}, {'in': 'body', 'type': 'String', 'name': 'business_type', 'required': True, 'default': None, 'description': '业务类型'}, {'in': 'body', 'type': 'String', 'name': 'config_group', 'required': True, 'default': None, 'description': '规则分组'}, {'in': 'body', 'type': 'Number[]', 'name': 'ids', 'required': True, 'default': None, 'description': '要删除的规则ID数组'})

    def __init__(self, business_id=_UNSET, business_type=_UNSET, config_group=_UNSET, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if business_type is not _UNSET:
            self.body['business_type'] = business_type
        if config_group is not _UNSET:
            self.body['config_group'] = config_group
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class NetworkSpeedSortRulesRequest(BaseRequest):
    """配置规则集排序.

    API: PUT /api/v5/ruletpl/network_speed/rule_sort

    Parameters:
        business_id (Number, required): 业务ID
        business_type (String, required): 业务类型
        config_group (String="custom_page","upstream_uri_change_rule","resp_headers_rule","customized_req_headers_rule", required): 规则分组标识
        ids (Number[], required): 排序后的规则ID数组
    """
    API_NAME = 'NetworkSpeedSortRules'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/ruletpl/network_speed/rule_sort'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '业务ID'}, {'in': 'body', 'type': 'String', 'name': 'business_type', 'required': True, 'default': None, 'description': '业务类型'}, {'in': 'body', 'type': 'String="custom_page","upstream_uri_change_rule","resp_headers_rule","customized_req_headers_rule"', 'name': 'config_group', 'required': True, 'default': None, 'description': '规则分组标识'}, {'in': 'body', 'type': 'Number[]', 'name': 'ids', 'required': True, 'default': None, 'description': '排序后的规则ID数组'})

    def __init__(self, business_id=_UNSET, business_type=_UNSET, config_group=_UNSET, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if business_type is not _UNSET:
            self.body['business_type'] = business_type
        if config_group is not _UNSET:
            self.body['config_group'] = config_group
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class NetworkSpeedUpdateRuleRequest(BaseRequest):
    """编辑配置规则.

    API: PUT /api/v5/ruletpl/network_speed/rule

    Parameters:
        id (Number, required): 记录ID
        config_group (String="custom_page","upstream_uri_change_rule","resp_headers_rule","customized_req_headers_rule", required): 规则分组
        custom_page (Object, optional): 错误页面定制
        upstream_uri_change_rule (Object, optional): 回源URI改写
        upstream_uri_change_rule.typ (String, required): 类型
        upstream_uri_change_rule.action (String, required): 动作
        upstream_uri_change_rule.match (String, required): 匹配值
        upstream_uri_change_rule.target (String, required): 目标值
        resp_headers_rule (Object, optional): 自定义响应头
        resp_headers_rule.type (String, required): 类型
        resp_headers_rule.content (String, required): 内容
        customized_req_headers_rule (Object, optional): 自定义回源请求头
        customized_req_headers_rule.type (String, required): 类型
        customized_req_headers_rule.content (String, required): 内容
    """
    API_NAME = 'NetworkSpeedUpdateRule'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/ruletpl/network_speed/rule'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '记录ID'}, {'in': 'body', 'type': 'String="custom_page","upstream_uri_change_rule","resp_headers_rule","customized_req_headers_rule"', 'name': 'config_group', 'required': True, 'default': None, 'description': '规则分组'}, {'in': 'body', 'type': 'Object', 'name': 'custom_page', 'required': False, 'default': None, 'description': '错误页面定制'}, {'in': 'body', 'type': 'Object', 'name': 'upstream_uri_change_rule', 'required': False, 'default': None, 'description': '回源URI改写'}, {'in': 'body', 'type': 'String', 'name': 'upstream_uri_change_rule.typ', 'required': True, 'default': None, 'description': '类型'}, {'in': 'body', 'type': 'String', 'name': 'upstream_uri_change_rule.action', 'required': True, 'default': None, 'description': '动作'}, {'in': 'body', 'type': 'String', 'name': 'upstream_uri_change_rule.match', 'required': True, 'default': None, 'description': '匹配值'}, {'in': 'body', 'type': 'String', 'name': 'upstream_uri_change_rule.target', 'required': True, 'default': None, 'description': '目标值'}, {'in': 'body', 'type': 'Object', 'name': 'resp_headers_rule', 'required': False, 'default': None, 'description': '自定义响应头'}, {'in': 'body', 'type': 'String', 'name': 'resp_headers_rule.type', 'required': True, 'default': None, 'description': '类型'}, {'in': 'body', 'type': 'String', 'name': 'resp_headers_rule.content', 'required': True, 'default': None, 'description': '内容'}, {'in': 'body', 'type': 'Object', 'name': 'customized_req_headers_rule', 'required': False, 'default': None, 'description': '自定义回源请求头'}, {'in': 'body', 'type': 'String', 'name': 'customized_req_headers_rule.type', 'required': True, 'default': None, 'description': '类型'}, {'in': 'body', 'type': 'String', 'name': 'customized_req_headers_rule.content', 'required': True, 'default': None, 'description': '内容'})

    def __init__(self, id=_UNSET, config_group=_UNSET, upstream_uri_change_rule=_UNSET, resp_headers_rule=_UNSET, customized_req_headers_rule=_UNSET, custom_page=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if config_group is not _UNSET:
            self.body['config_group'] = config_group
        if upstream_uri_change_rule is not _UNSET:
            self.body['upstream_uri_change_rule'] = upstream_uri_change_rule
        if resp_headers_rule is not _UNSET:
            self.body['resp_headers_rule'] = resp_headers_rule
        if customized_req_headers_rule is not _UNSET:
            self.body['customized_req_headers_rule'] = customized_req_headers_rule
        if custom_page is not _UNSET:
            self.body['custom_page'] = custom_page
        for key, value in kwargs.items():
            self.body[key] = value


class UpdateRuleTemplateRequest(BaseRequest):
    """更新模版.

    API: PUT /api/v5/ruletpls

    Parameters:
        id (Number, required): 要更新规则模版的ID。
        name (String, optional): 规则模版的新名称。
        description (String, optional): 规则模版的新描述。
    """
    API_NAME = 'UpdateRuleTemplate'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/ruletpls'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '要更新规则模版的ID。'}, {'in': 'body', 'type': 'String', 'name': 'name', 'required': False, 'default': None, 'description': '规则模版的新名称。'}, {'in': 'body', 'type': 'String', 'name': 'description', 'required': False, 'default': None, 'description': '规则模版的新描述。'})

    def __init__(self, id=_UNSET, name=_UNSET, description=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if name is not _UNSET:
            self.body['name'] = name
        if description is not _UNSET:
            self.body['description'] = description
        for key, value in kwargs.items():
            self.body[key] = value


class DeleteRuleTemplateRequest(BaseRequest):
    """删除模版.

    API: DELETE /api/v5/ruletpls

    Parameters:
        id (Number, required): 要删除规则模版的ID。
    """
    API_NAME = 'DeleteRuleTemplate'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/ruletpls'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '要删除规则模版的ID。'},)

    def __init__(self, id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        for key, value in kwargs.items():
            self.body[key] = value


class GetRuleTemplateListRequest(BaseRequest):
    """获取模版列表.

    API: GET /api/v5/ruletpls
    """
    API_NAME = 'GetRuleTemplateList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/ruletpls'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class UnbindRuleTemplateRequest(BaseRequest):
    """域名解绑模版.

    API: PUT /api/v5/ruletpls/unbind_domain

    Parameters:
        id (Number, required): 规则模版的ID。
        domain_ids (Number[], required): 要从模版解绑的域名ID列表。
    """
    API_NAME = 'UnbindRuleTemplate'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/ruletpls/unbind_domain'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '规则模版的ID。'}, {'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '要从模版解绑的域名ID列表。'})

    def __init__(self, id=_UNSET, domain_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        for key, value in kwargs.items():
            self.body[key] = value


class BindRuleTemplateRequest(BaseRequest):
    """域名绑定模版.

    API: PUT /api/v5/ruletpls/bind_domain

    Parameters:
        id (Number, required): 规则模版的ID。
        domain_ids (Number[], required): 要绑定到模版的域名ID列表。
    """
    API_NAME = 'BindRuleTemplate'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/ruletpls/bind_domain'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '规则模版的ID。'}, {'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '要绑定到模版的域名ID列表。'})

    def __init__(self, id=_UNSET, domain_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        for key, value in kwargs.items():
            self.body[key] = value


class ListRuleTpsDomainsRequest(BaseRequest):
    """获取模版绑定的域名.

    API: GET /api/v5/ruletpls/domains
    """
    API_NAME = 'ListRuleTpsDomains'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/ruletpls/domains'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class CreateRuleTemplateRequest(BaseRequest):
    """创建模版.

    API: POST /api/v5/ruletpls

    Parameters:
        name (String, required): 模版名称。
        description (String, optional): 模版描述。
        app_type (String=network_speed, optional, default=network_speed): 模版适用的应用类型。
        tpl_type (String=only_domain,more_domain, required): 模版类型，only_domain=域名级加速配置，more_domain=域名加速模板配置。
        domain_id (Number, optional): 域名ID，tpl_type=only_domain时，必填。
        from_tpl_id (Number, optional): 要复制的现有模版ID，from_tpl_type=global时，传0
        from_tpl_type (String=only_domain,more_domain,global, optional): 要复制的现有模版类型，global=全局模板。
        bind_domain (Object, required): 绑定域名的信息。
        bind_domain.all_domain (Boolean, required): 如果为 true，则绑定到所有域名。
        bind_domain.domain_ids (Number[], optional): 要绑定的域名ID列表。
        bind_domain.domain_group_ids (Number[], optional): 要绑定的域名组ID列表。
        bind_domain.domains (String[], optional): 要绑定的域名列表。
        bind_domain.is_bind (Boolean, required): 指示是否应绑定域名。
    """
    API_NAME = 'CreateRuleTemplate'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/ruletpls'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'name', 'required': True, 'default': None, 'description': '模版名称。'}, {'in': 'body', 'type': 'String', 'name': 'description', 'required': False, 'default': None, 'description': '模版描述。'}, {'in': 'body', 'type': 'String=network_speed', 'name': 'app_type', 'required': False, 'default': 'network_speed', 'description': '模版适用的应用类型。'}, {'in': 'body', 'type': 'String=only_domain,more_domain', 'name': 'tpl_type', 'required': True, 'default': None, 'description': '模版类型，only_domain=域名级加速配置，more_domain=域名加速模板配置。'}, {'in': 'body', 'type': 'Number', 'name': 'domain_id', 'required': False, 'default': None, 'description': '域名ID，tpl_type=only_domain时，必填。'}, {'in': 'body', 'type': 'Number', 'name': 'from_tpl_id', 'required': False, 'default': None, 'description': '要复制的现有模版ID，from_tpl_type=global时，传0'}, {'in': 'body', 'type': 'String=only_domain,more_domain,global', 'name': 'from_tpl_type', 'required': False, 'default': None, 'description': '要复制的现有模版类型，global=全局模板。'}, {'in': 'body', 'type': 'Object', 'name': 'bind_domain', 'required': True, 'default': None, 'description': '绑定域名的信息。'}, {'in': 'body', 'type': 'Boolean', 'name': 'bind_domain.all_domain', 'required': True, 'default': None, 'description': '如果为 true，则绑定到所有域名。'}, {'in': 'body', 'type': 'Number[]', 'name': 'bind_domain.domain_ids', 'required': False, 'default': None, 'description': '要绑定的域名ID列表。'}, {'in': 'body', 'type': 'Number[]', 'name': 'bind_domain.domain_group_ids', 'required': False, 'default': None, 'description': '要绑定的域名组ID列表。'}, {'in': 'body', 'type': 'String[]', 'name': 'bind_domain.domains', 'required': False, 'default': None, 'description': '要绑定的域名列表。'}, {'in': 'body', 'type': 'Boolean', 'name': 'bind_domain.is_bind', 'required': True, 'default': None, 'description': '指示是否应绑定域名。'})

    def __init__(self, name=_UNSET, tpl_type=_UNSET, bind_domain=_UNSET, description=_UNSET, app_type='network_speed', domain_id=_UNSET, from_tpl_id=_UNSET, from_tpl_type=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if name is not _UNSET:
            self.body['name'] = name
        if tpl_type is not _UNSET:
            self.body['tpl_type'] = tpl_type
        if bind_domain is not _UNSET:
            self.body['bind_domain'] = bind_domain
        if description is not _UNSET:
            self.body['description'] = description
        self.body['app_type'] = app_type
        if domain_id is not _UNSET:
            self.body['domain_id'] = domain_id
        if from_tpl_id is not _UNSET:
            self.body['from_tpl_id'] = from_tpl_id
        if from_tpl_type is not _UNSET:
            self.body['from_tpl_type'] = from_tpl_type
        for key, value in kwargs.items():
            self.body[key] = value


class SwitchDomainTemplateRequest(BaseRequest):
    """切换域名模版.

    API: PUT /api/v5/ruletpls/domain/switch_tpl

    Parameters:
        app_type (String, optional, default=network_speed): 模版应用类型。
        domain_ids (Number[], required): 要切换模版的域名ID列表。
        new_tpl_id (Number, required): 要切换到的新模版ID，new_tpl_type=global时，传0
        new_tpl_type (String=only_domain,more_domain,global, required): 新模版类型。
    """
    API_NAME = 'SwitchDomainTemplate'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/ruletpls/domain/switch_tpl'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'app_type', 'required': False, 'default': 'network_speed', 'description': '模版应用类型。'}, {'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '要切换模版的域名ID列表。'}, {'in': 'body', 'type': 'Number', 'name': 'new_tpl_id', 'required': True, 'default': None, 'description': '要切换到的新模版ID，new_tpl_type=global时，传0'}, {'in': 'body', 'type': 'String=only_domain,more_domain,global', 'name': 'new_tpl_type', 'required': True, 'default': None, 'description': '新模版类型。'})

    def __init__(self, domain_ids=_UNSET, new_tpl_id=_UNSET, new_tpl_type=_UNSET, app_type='network_speed', query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        if new_tpl_id is not _UNSET:
            self.body['new_tpl_id'] = new_tpl_id
        if new_tpl_type is not _UNSET:
            self.body['new_tpl_type'] = new_tpl_type
        self.body['app_type'] = app_type
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallPageCfgRequest(BaseRequest):
    """获取可用策略规则.

    API: GET /api/v5/firewall.pagecfg
    """
    API_NAME = 'Firewall_pageCfg'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.pagecfg'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class FirewallPageCfgHwwsRequest(BaseRequest):
    """获取可用策略规则通过模板ID.

    API: GET /api/v5/firewall.pagecfg.hwws
    """
    API_NAME = 'Firewall_pageCfgHwws'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.pagecfg.hwws'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class FirewallSavePolicyRequest(BaseRequest):
    """保存策略.

    API: POST /api/v5/firewall.policy.save

    Parameters:
        id (Number, required): 策略ID, 针对更新
        business_id (Number, required): 模板ID
        package_id (Number, required): 套餐ID, 仅针对 type=tcp
        product_flag (String=tcp,app,ssl,plus, optional, default=plus): 产品标识
        group_id (Number, required): 策略集ID
        tjkd_app_id (Number, required): 抗D APP ID, 仅针对 type=app, tjkd_app_id是前端传参数的名字, 对应的字段是app_id, app_id与框架的key冲突
        from (String, required): 来源：aR防倒链 zL区域屏蔽 sP源站保护 cc防CC botBot管理 diy自定义 batch批量配置; 常规添加的策略来源只能是diy
        remark (String, required): 备注
        type (String, required): 策略类型：cdn(云加速)/plus(抗D，红网)/tcp(四层转发)/ssl(https防护)
        use_type (String, required): 实际使用的规则类型：cdn(云加速)/plus(抗D，红网)/tcp(四层转发)
        action (String, required): 处理⽅式: anticc(通用)/block(封禁)/deny(阻断)/pass(放行)/watch(观察); anticc只针对cdn/plus; 抗D APP只有deny/pass/watch三种，且无action_data
        action_data (Object, required): 处理⽅式, 对应的数据
        action_data.level (String, required): CC防护等级，针对 通用 处理方式，: default(默认)/normal(普通)/strict(严格)/captcha(验证码)
        action_data.next_rules (Number, required): 是否继续执行下一规则集，针对 观察/放行/人机验证/蜜网牵引 处理方式：0否 1是
        action_data.interval (Number, required): 有效期，针对 封禁/加白 处理方式
        action_data.time_unit (String, required): 封禁时间单位: day(天)/hour(时)/minute(分)/second(秒)，针对 封禁 处理方式；注意：加白处理方式没有时间单位，加白只支持秒
        action_data.type (String, required): 验证类型，针对 人机验证 处理方式：cookie(Cookie验证)/js(JS验证)/captcha(智能验证码)
        action_data.cc (Number, required): 是否继续执行CC，针对 放行/蜜网牵引 处理方式：0不执行  1执行
        action_data.waf (Number, required): 是否执行WAF，针对 放行/加白/蜜网牵引 处理方式：0不执行  1执行
        action_data.group_ids (String[], required): 域名组ID，相同的处置方式应用于域名组内的所有域名，针对 加白 处理方式
        action_data.protocol (String, required): 请求蜜网服务器的协议，针对 蜜网牵引 处理方式：http/https
        action_data.ip (String, required): 蜜网服务器的IP，针对 蜜网牵引 处理方式
        action_data.port (String, required): 蜜网服务器的端口，针对 蜜网牵引 处理方式
        action_data.redirect_url (String, required): 重定向URL，针对 重定向 处理方式
        rules (Object, required): 规则数据，关于规则的各种定义及描述，请查看 获取可用规则(firewall.pagecfg)接口
        rules.rule_type (String, required): 规则类型, 根据业务而不同，关于规则的各种定义及描述，请查看 获取可用规则(firewall.pagecfg)接口
        rules.logic (String, required): 罗辑运算，每个规则能用的逻辑操作，请查看 获取可用规则(firewall.pagecfg) 接口
        rules.data (Object, required): 规则运算对应的数据，示例中已给出所有 规则-逻辑-数据 的对应关系；请根据自己的需要复制示例参数。
    """
    API_NAME = 'Firewall_savePolicy'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policy.save'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '策略ID, 针对更新'}, {'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '模板ID'}, {'in': 'body', 'type': 'Number', 'name': 'package_id', 'required': True, 'default': None, 'description': '套餐ID, 仅针对 type=tcp'}, {'in': 'body', 'type': 'String=tcp,app,ssl,plus', 'name': 'product_flag', 'required': False, 'default': 'plus', 'description': '产品标识'}, {'in': 'body', 'type': 'Number', 'name': 'group_id', 'required': True, 'default': None, 'description': '策略集ID'}, {'in': 'body', 'type': 'Number', 'name': 'tjkd_app_id', 'required': True, 'default': None, 'description': '抗D APP ID, 仅针对 type=app, tjkd_app_id是前端传参数的名字, 对应的字段是app_id, app_id与框架的key冲突'}, {'in': 'body', 'type': 'String', 'name': 'from', 'required': True, 'default': None, 'description': '来源：aR防倒链 zL区域屏蔽 sP源站保护 cc防CC botBot管理 diy自定义 batch批量配置; 常规添加的策略来源只能是diy'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': True, 'default': None, 'description': '备注'}, {'in': 'body', 'type': 'String', 'name': 'type', 'required': True, 'default': None, 'description': '策略类型：cdn(云加速)/plus(抗D，红网)/tcp(四层转发)/ssl(https防护)'}, {'in': 'body', 'type': 'String', 'name': 'use_type', 'required': True, 'default': None, 'description': '实际使用的规则类型：cdn(云加速)/plus(抗D，红网)/tcp(四层转发)'}, {'in': 'body', 'type': 'String', 'name': 'action', 'required': True, 'default': None, 'description': '处理⽅式: anticc(通用)/block(封禁)/deny(阻断)/pass(放行)/watch(观察); anticc只针对cdn/plus; 抗D APP只有deny/pass/watch三种，且无action_data'}, {'in': 'body', 'type': 'Object', 'name': 'action_data', 'required': True, 'default': None, 'description': '处理⽅式, 对应的数据'}, {'in': 'body', 'type': 'String', 'name': 'action_data.level', 'required': True, 'default': None, 'description': 'CC防护等级，针对 通用 处理方式，: default(默认)/normal(普通)/strict(严格)/captcha(验证码)'}, {'in': 'body', 'type': 'Number', 'name': 'action_data.next_rules', 'required': True, 'default': None, 'description': '是否继续执行下一规则集，针对 观察/放行/人机验证/蜜网牵引 处理方式：0否 1是'}, {'in': 'body', 'type': 'Number', 'name': 'action_data.interval', 'required': True, 'default': None, 'description': '有效期，针对 封禁/加白 处理方式'}, {'in': 'body', 'type': 'String', 'name': 'action_data.time_unit', 'required': True, 'default': None, 'description': '封禁时间单位: day(天)/hour(时)/minute(分)/second(秒)，针对 封禁 处理方式；注意：加白处理方式没有时间单位，加白只支持秒'}, {'in': 'body', 'type': 'String', 'name': 'action_data.type', 'required': True, 'default': None, 'description': '验证类型，针对 人机验证 处理方式：cookie(Cookie验证)/js(JS验证)/captcha(智能验证码)'}, {'in': 'body', 'type': 'Number', 'name': 'action_data.cc', 'required': True, 'default': None, 'description': '是否继续执行CC，针对 放行/蜜网牵引 处理方式：0不执行  1执行'}, {'in': 'body', 'type': 'Number', 'name': 'action_data.waf', 'required': True, 'default': None, 'description': '是否执行WAF，针对 放行/加白/蜜网牵引 处理方式：0不执行  1执行'}, {'in': 'body', 'type': 'String[]', 'name': 'action_data.group_ids', 'required': True, 'default': None, 'description': '域名组ID，相同的处置方式应用于域名组内的所有域名，针对 加白 处理方式'}, {'in': 'body', 'type': 'String', 'name': 'action_data.protocol', 'required': True, 'default': None, 'description': '请求蜜网服务器的协议，针对 蜜网牵引 处理方式：http/https'}, {'in': 'body', 'type': 'String', 'name': 'action_data.ip', 'required': True, 'default': None, 'description': '蜜网服务器的IP，针对 蜜网牵引 处理方式'}, {'in': 'body', 'type': 'String', 'name': 'action_data.port', 'required': True, 'default': None, 'description': '蜜网服务器的端口，针对 蜜网牵引 处理方式'}, {'in': 'body', 'type': 'String', 'name': 'action_data.redirect_url', 'required': True, 'default': None, 'description': '重定向URL，针对 重定向 处理方式'}, {'in': 'body', 'type': 'Object', 'name': 'rules', 'required': True, 'default': None, 'description': '规则数据，关于规则的各种定义及描述，请查看 获取可用规则(firewall.pagecfg)接口'}, {'in': 'body', 'type': 'String', 'name': 'rules.rule_type', 'required': True, 'default': None, 'description': '规则类型, 根据业务而不同，关于规则的各种定义及描述，请查看 获取可用规则(firewall.pagecfg)接口'}, {'in': 'body', 'type': 'String', 'name': 'rules.logic', 'required': True, 'default': None, 'description': '罗辑运算，每个规则能用的逻辑操作，请查看 获取可用规则(firewall.pagecfg) 接口'}, {'in': 'body', 'type': 'Object', 'name': 'rules.data', 'required': True, 'default': None, 'description': '规则运算对应的数据，示例中已给出所有 规则-逻辑-数据 的对应关系；请根据自己的需要复制示例参数。'})

    def __init__(self, id=_UNSET, business_id=_UNSET, package_id=_UNSET, group_id=_UNSET, tjkd_app_id=_UNSET, from=_UNSET, remark=_UNSET, type=_UNSET, use_type=_UNSET, action=_UNSET, action_data=_UNSET, rules=_UNSET, product_flag='plus', query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if package_id is not _UNSET:
            self.body['package_id'] = package_id
        if group_id is not _UNSET:
            self.body['group_id'] = group_id
        if tjkd_app_id is not _UNSET:
            self.body['tjkd_app_id'] = tjkd_app_id
        if from is not _UNSET:
            self.body['from'] = from
        if remark is not _UNSET:
            self.body['remark'] = remark
        if type is not _UNSET:
            self.body['type'] = type
        if use_type is not _UNSET:
            self.body['use_type'] = use_type
        if action is not _UNSET:
            self.body['action'] = action
        if action_data is not _UNSET:
            self.body['action_data'] = action_data
        if rules is not _UNSET:
            self.body['rules'] = rules
        self.body['product_flag'] = product_flag
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallGetPolicyRequest(BaseRequest):
    """查询策略通过策略ID.

    API: GET /api/v5/firewall.policy.get_id
    """
    API_NAME = 'Firewall_getPolicy'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.policy.get_id'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class FirewallGetPolicyByCodeRequest(BaseRequest):
    """查询策略通过策略CODE.

    API: GET /api/v5/firewall.policy.get_code
    """
    API_NAME = 'Firewall_getPolicyByCode'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.policy.get_code'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class FirewallStatsPolicyRequest(BaseRequest):
    """统计策略.

    API: GET /api/v5/firewall.policy.stats_domainid
    """
    API_NAME = 'Firewall_statsPolicy'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.policy.stats_domainid'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class FirewallOpenRequest(BaseRequest):
    """启用策略.

    API: POST /api/v5/firewall.policy.open
    """
    API_NAME = 'Firewall_open'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policy.open'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallStopRequest(BaseRequest):
    """暂停策略.

    API: POST /api/v5/firewall.policy.stop

    Parameters:
        ids (String[], required): 策略ID数组
    """
    API_NAME = 'Firewall_stop'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policy.stop'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'ids', 'required': True, 'default': None, 'description': '策略ID数组'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallDeleteRequest(BaseRequest):
    """删除策略.

    API: POST /api/v5/firewall.policy.delete

    Parameters:
        ids (String[], required): 策略ID数组
    """
    API_NAME = 'Firewall_delete'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policy.delete'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'ids', 'required': True, 'default': None, 'description': '策略ID数组'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallSortRequest(BaseRequest):
    """策略排序.

    API: POST /api/v5/firewall.policy.sort

    Parameters:
        new_sorts (Object, required): 新的排序, 格式为：{id: index}, id为策略ID， index为行的索引号, 如：{3: 0, 4: 1, 5: 2}
    """
    API_NAME = 'Firewall_sort'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policy.sort'
    PARAMS = ({'in': 'body', 'type': 'Object', 'name': 'new_sorts', 'required': True, 'default': None, 'description': '新的排序, 格式为：{id: index}, id为策略ID， index为行的索引号, 如：{3: 0, 4: 1, 5: 2}'},)

    def __init__(self, new_sorts=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if new_sorts is not _UNSET:
            self.body['new_sorts'] = new_sorts
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallGetsPolicyByMainidRequest(BaseRequest):
    """查询策略历史.

    API: GET /api/v5/firewall.policy.get_mainid
    """
    API_NAME = 'Firewall_getsPolicyByMainid'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.policy.get_mainid'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class FirewallGetsPolicyByPackageidRequest(BaseRequest):
    """查询策略通过独享资源包ID.

    API: GET /api/v5/firewall.policy.get_packageid
    """
    API_NAME = 'Firewall_getsPolicyByPackageid'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.policy.get_packageid'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class FirewallSavePolicyGroupRequest(BaseRequest):
    """保存策略集.

    API: POST /api/v5/firewall.policyGroup.save

    Parameters:
        id (Number, required): 策略集ID, 针对更新
        business_id (Number, required): 模板ID
        from (String, optional, default=diy): 策略集来源：aR防倒链 zL区域屏蔽 sP源站保护 cc防CC botBot管理 diy自定义 batch批量配置
        remark (String, required): 备注
        name (String, required): 名称
    """
    API_NAME = 'Firewall_savePolicyGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policyGroup.save'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '策略集ID, 针对更新'}, {'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '模板ID'}, {'in': 'body', 'type': 'String', 'name': 'from', 'required': False, 'default': 'diy', 'description': '策略集来源：aR防倒链 zL区域屏蔽 sP源站保护 cc防CC botBot管理 diy自定义 batch批量配置'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': True, 'default': None, 'description': '备注'}, {'in': 'body', 'type': 'String', 'name': 'name', 'required': True, 'default': None, 'description': '名称'})

    def __init__(self, id=_UNSET, business_id=_UNSET, remark=_UNSET, name=_UNSET, from='diy', query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if remark is not _UNSET:
            self.body['remark'] = remark
        if name is not _UNSET:
            self.body['name'] = name
        self.body['from'] = from
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallGetsPolicyGroupByDomainidRequest(BaseRequest):
    """查询策略集通过模版ID.

    API: GET /api/v5/firewall.policyGroup.get_domainid
    """
    API_NAME = 'Firewall_getsPolicyGroupByDomainid'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.policyGroup.get_domainid'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class FirewallStopGroupRequest(BaseRequest):
    """暂停策略集.

    API: POST /api/v5/firewall.policyGroup.stop

    Parameters:
        ids (String[], required): 策略集ID数组
    """
    API_NAME = 'Firewall_stopGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policyGroup.stop'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'ids', 'required': True, 'default': None, 'description': '策略集ID数组'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallOpenGroupRequest(BaseRequest):
    """启用策略集.

    API: POST /api/v5/firewall.policyGroup.open

    Parameters:
        ids (String[], required): 策略ID数组
    """
    API_NAME = 'Firewall_openGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policyGroup.open'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'ids', 'required': True, 'default': None, 'description': '策略ID数组'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallDeleteGroupRequest(BaseRequest):
    """删除策略集.

    API: POST /api/v5/firewall.policyGroup.delete

    Parameters:
        ids (String[], required): 策略ID数组
    """
    API_NAME = 'Firewall_deleteGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policyGroup.delete'
    PARAMS = ({'in': 'body', 'type': 'String[]', 'name': 'ids', 'required': True, 'default': None, 'description': '策略ID数组'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallSortGroupRequest(BaseRequest):
    """策略集排序.

    API: POST /api/v5/firewall.policyGroup.sort

    Parameters:
        new_sorts (Object, required): 新的排序, 格式为：{id: index}, id为策略ID， index为行的索引号, 如：{3: 0, 4: 1, 5: 2}
    """
    API_NAME = 'Firewall_sortGroup'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policyGroup.sort'
    PARAMS = ({'in': 'body', 'type': 'Object', 'name': 'new_sorts', 'required': True, 'default': None, 'description': '新的排序, 格式为：{id: index}, id为策略ID， index为行的索引号, 如：{3: 0, 4: 1, 5: 2}'},)

    def __init__(self, new_sorts=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if new_sorts is not _UNSET:
            self.body['new_sorts'] = new_sorts
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallGetsPolicyByGroupIdRequest(BaseRequest):
    """查询策略集.

    API: GET /api/v5/firewall.policy.get_groupId
    """
    API_NAME = 'Firewall_getsPolicyByGroupId'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.policy.get_groupId'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class GetPolicyGroupTplRequest(BaseRequest):
    """查询引用规则集列表.

    API: GET /api/v5/firewall.policyGroup.tpl.get
    """
    API_NAME = 'getPolicyGroupTPL'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.policyGroup.tpl.get'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class GetDdosProtectionConfigRequest(BaseRequest):
    """获取DDoS防护配置.

    API: GET /api/v5/security_protection/ddos/configs
    """
    API_NAME = 'GetDdosProtectionConfig'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/security_protection/ddos/configs'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class UpdateDdosProtectionConfigRequest(BaseRequest):
    """更新DDoS防护配置.

    API: PUT /api/v5/security_protection/ddos/configs

    Parameters:
        business_id (Number, required): 模板ID
        application_ddos_protection (Object, optional): 应用层DDoS配置
        application_ddos_protection.status (String=on,off,keep, required): 状态
        application_ddos_protection.ai_cc_status (String=on,off, required): AI防护状态
        application_ddos_protection.type (String=default,normal,strict,captcha,keep, required): 防护类型
        application_ddos_protection.need_attack_detection (Number, optional, default=1): 攻击检测开关
        application_ddos_protection.ai_status (String=on,off, optional, default=1): AI状态
        visitor_authentication (Object, optional): 访客鉴权配置
        visitor_authentication.status (String=on,off, required): 状态
        visitor_authentication.auth_token (String, optional): 鉴权令牌
        visitor_authentication.pass_still_check (Number, optional): 通过后检查
    """
    API_NAME = 'UpdateDdosProtectionConfig'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/security_protection/ddos/configs'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '模板ID'}, {'in': 'body', 'type': 'Object', 'name': 'application_ddos_protection', 'required': False, 'default': None, 'description': '应用层DDoS配置'}, {'in': 'body', 'type': 'String=on,off,keep', 'name': 'application_ddos_protection.status', 'required': True, 'default': None, 'description': '状态'}, {'in': 'body', 'type': 'String=on,off', 'name': 'application_ddos_protection.ai_cc_status', 'required': True, 'default': None, 'description': 'AI防护状态'}, {'in': 'body', 'type': 'String=default,normal,strict,captcha,keep', 'name': 'application_ddos_protection.type', 'required': True, 'default': None, 'description': '防护类型'}, {'in': 'body', 'type': 'Number', 'name': 'application_ddos_protection.need_attack_detection', 'required': False, 'default': '1', 'description': '攻击检测开关'}, {'in': 'body', 'type': 'String=on,off', 'name': 'application_ddos_protection.ai_status', 'required': False, 'default': '1', 'description': 'AI状态'}, {'in': 'body', 'type': 'Object', 'name': 'visitor_authentication', 'required': False, 'default': None, 'description': '访客鉴权配置'}, {'in': 'body', 'type': 'String=on,off', 'name': 'visitor_authentication.status', 'required': True, 'default': None, 'description': '状态'}, {'in': 'body', 'type': 'String', 'name': 'visitor_authentication.auth_token', 'required': False, 'default': None, 'description': '鉴权令牌'}, {'in': 'body', 'type': 'Number', 'name': 'visitor_authentication.pass_still_check', 'required': False, 'default': None, 'description': '通过后检查'})

    def __init__(self, business_id=_UNSET, application_ddos_protection=_UNSET, visitor_authentication=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if application_ddos_protection is not _UNSET:
            self.body['application_ddos_protection'] = application_ddos_protection
        if visitor_authentication is not _UNSET:
            self.body['visitor_authentication'] = visitor_authentication
        for key, value in kwargs.items():
            self.body[key] = value


class GetWafRuleConfigRequest(BaseRequest):
    """获取WAF规则配置.

    API: GET /api/v5/security_protection/waf/rules
    """
    API_NAME = 'GetWafRuleConfig'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/security_protection/waf/rules'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class UpdateWafRuleConfigRequest(BaseRequest):
    """更新WAF规则配置.

    API: PUT /api/v5/security_protection/waf/rules

    Parameters:
        business_id (Number, required): 模板ID
        waf_rule_config (Object, optional): WAF规则配置
        waf_rule_config.status (String=on,off,keep, required): 状态
        waf_rule_config.ai_status (String=on,off, required): AI状态
        waf_rule_config.waf_level (String=general,strict,keep, required): 防护级别
        waf_rule_config.waf_mode (String=off,active,block,ban,keep, required): 防护模式
        waf_intercept_page (Object, optional): 拦截页面配置
        waf_intercept_page.status (String=on,off, required): 状态
        waf_intercept_page.type (String=custom,default,keep, required): 页面类型
        waf_intercept_page.content (String, optional): 自定义内容
        replay_attack_protection (Object, optional): 重放攻击防护
        csrf_protection (Object, optional): CSRF防护
        web_shell_protection (Object, optional): WebShell防护
    """
    API_NAME = 'UpdateWafRuleConfig'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/security_protection/waf/rules'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '模板ID'}, {'in': 'body', 'type': 'Object', 'name': 'waf_rule_config', 'required': False, 'default': None, 'description': 'WAF规则配置'}, {'in': 'body', 'type': 'String=on,off,keep', 'name': 'waf_rule_config.status', 'required': True, 'default': None, 'description': '状态'}, {'in': 'body', 'type': 'String=on,off', 'name': 'waf_rule_config.ai_status', 'required': True, 'default': None, 'description': 'AI状态'}, {'in': 'body', 'type': 'String=general,strict,keep', 'name': 'waf_rule_config.waf_level', 'required': True, 'default': None, 'description': '防护级别'}, {'in': 'body', 'type': 'String=off,active,block,ban,keep', 'name': 'waf_rule_config.waf_mode', 'required': True, 'default': None, 'description': '防护模式'}, {'in': 'body', 'type': 'Object', 'name': 'waf_intercept_page', 'required': False, 'default': None, 'description': '拦截页面配置'}, {'in': 'body', 'type': 'String=on,off', 'name': 'waf_intercept_page.status', 'required': True, 'default': None, 'description': '状态'}, {'in': 'body', 'type': 'String=custom,default,keep', 'name': 'waf_intercept_page.type', 'required': True, 'default': None, 'description': '页面类型'}, {'in': 'body', 'type': 'String', 'name': 'waf_intercept_page.content', 'required': False, 'default': None, 'description': '自定义内容'}, {'in': 'body', 'type': 'Object', 'name': 'replay_attack_protection', 'required': False, 'default': None, 'description': '重放攻击防护'}, {'in': 'body', 'type': 'Object', 'name': 'csrf_protection', 'required': False, 'default': None, 'description': 'CSRF防护'}, {'in': 'body', 'type': 'Object', 'name': 'web_shell_protection', 'required': False, 'default': None, 'description': 'WebShell防护'})

    def __init__(self, business_id=_UNSET, waf_rule_config=_UNSET, waf_intercept_page=_UNSET, replay_attack_protection=_UNSET, csrf_protection=_UNSET, web_shell_protection=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if waf_rule_config is not _UNSET:
            self.body['waf_rule_config'] = waf_rule_config
        if waf_intercept_page is not _UNSET:
            self.body['waf_intercept_page'] = waf_intercept_page
        if replay_attack_protection is not _UNSET:
            self.body['replay_attack_protection'] = replay_attack_protection
        if csrf_protection is not _UNSET:
            self.body['csrf_protection'] = csrf_protection
        if web_shell_protection is not _UNSET:
            self.body['web_shell_protection'] = web_shell_protection
        for key, value in kwargs.items():
            self.body[key] = value


class GetMemberGlobalTemplateRequest(BaseRequest):
    """获取用户全局模板.

    API: GET /api/v5/security_protection/template/member/global
    """
    API_NAME = 'GetMemberGlobalTemplate'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/security_protection/template/member/global'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class CreateTemplateRequest(BaseRequest):
    """创建模板.

    API: POST /api/v5/security_protection/template

    Parameters:
        name (String, required): 模板名称
        remark (String, optional): 备注
        template_source_id (Number, optional): 源模板ID
        domain_ids (Number[], optional): 域名ID列表
        group_ids (Number[], optional): 分组ID列表
        domains (String[], optional): 域名列表
        bind_all (Boolean, optional): 是否绑定全部
    """
    API_NAME = 'CreateTemplate'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/security_protection/template'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'name', 'required': True, 'default': None, 'description': '模板名称'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '备注'}, {'in': 'body', 'type': 'Number', 'name': 'template_source_id', 'required': False, 'default': None, 'description': '源模板ID'}, {'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': False, 'default': None, 'description': '域名ID列表'}, {'in': 'body', 'type': 'Number[]', 'name': 'group_ids', 'required': False, 'default': None, 'description': '分组ID列表'}, {'in': 'body', 'type': 'String[]', 'name': 'domains', 'required': False, 'default': None, 'description': '域名列表'}, {'in': 'body', 'type': 'Boolean', 'name': 'bind_all', 'required': False, 'default': None, 'description': '是否绑定全部'})

    def __init__(self, name=_UNSET, remark=_UNSET, template_source_id=_UNSET, domain_ids=_UNSET, group_ids=_UNSET, domains=_UNSET, bind_all=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if name is not _UNSET:
            self.body['name'] = name
        if remark is not _UNSET:
            self.body['remark'] = remark
        if template_source_id is not _UNSET:
            self.body['template_source_id'] = template_source_id
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        if group_ids is not _UNSET:
            self.body['group_ids'] = group_ids
        if domains is not _UNSET:
            self.body['domains'] = domains
        if bind_all is not _UNSET:
            self.body['bind_all'] = bind_all
        for key, value in kwargs.items():
            self.body[key] = value


class CreateDomainTemplateRequest(BaseRequest):
    """创建域名模板.

    API: POST /api/v5/security_protection/template/domain

    Parameters:
        domain_ids (Number[], required): 域名ID列表
        template_source_id (Number, optional): 源模板ID，不传默认引用全局模版
    """
    API_NAME = 'CreateDomainTemplate'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/security_protection/template/domain'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': True, 'default': None, 'description': '域名ID列表'}, {'in': 'body', 'type': 'Number', 'name': 'template_source_id', 'required': False, 'default': None, 'description': '源模板ID，不传默认引用全局模版'})

    def __init__(self, domain_ids=_UNSET, template_source_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        if template_source_id is not _UNSET:
            self.body['template_source_id'] = template_source_id
        for key, value in kwargs.items():
            self.body[key] = value


class GetTemplateListRequest(BaseRequest):
    """获取模板列表.

    API: POST /api/v5/security_protection/template/search

    Parameters:
        tpl_type (String=global,only_domain,more_domain, required): 模板类型
        search_type (String, optional): 搜索类型
        search_key (String, optional): 搜索关键字
        page (Number, required): 页码
        page_size (Number, required): 每页数量
    """
    API_NAME = 'GetTemplateList'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/security_protection/template/search'
    PARAMS = ({'in': 'body', 'type': 'String=global,only_domain,more_domain', 'name': 'tpl_type', 'required': True, 'default': None, 'description': '模板类型'}, {'in': 'body', 'type': 'String', 'name': 'search_type', 'required': False, 'default': None, 'description': '搜索类型'}, {'in': 'body', 'type': 'String', 'name': 'search_key', 'required': False, 'default': None, 'description': '搜索关键字'}, {'in': 'body', 'type': 'Number', 'name': 'page', 'required': True, 'default': None, 'description': '页码'}, {'in': 'body', 'type': 'Number', 'name': 'page_size', 'required': True, 'default': None, 'description': '每页数量'})

    def __init__(self, tpl_type=_UNSET, page=_UNSET, page_size=_UNSET, search_type=_UNSET, search_key=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if tpl_type is not _UNSET:
            self.body['tpl_type'] = tpl_type
        if page is not _UNSET:
            self.body['page'] = page
        if page_size is not _UNSET:
            self.body['page_size'] = page_size
        if search_type is not _UNSET:
            self.body['search_type'] = search_type
        if search_key is not _UNSET:
            self.body['search_key'] = search_key
        for key, value in kwargs.items():
            self.body[key] = value


class GetTemplateBindDomainListRequest(BaseRequest):
    """获取模板绑定域名.

    API: POST /api/v5/security_protection/template/domain/bind/search

    Parameters:
        business_id (Number, required): 模板ID
        page (Number, required): 页码
        page_size (Number, required): 每页数量
        domain (String, optional): 域名
        tpl_type (String=global,only_domain,more_domain, optional): 模板类型
    """
    API_NAME = 'GetTemplateBindDomainList'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/security_protection/template/domain/bind/search'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '模板ID'}, {'in': 'body', 'type': 'Number', 'name': 'page', 'required': True, 'default': None, 'description': '页码'}, {'in': 'body', 'type': 'Number', 'name': 'page_size', 'required': True, 'default': None, 'description': '每页数量'}, {'in': 'body', 'type': 'String', 'name': 'domain', 'required': False, 'default': None, 'description': '域名'}, {'in': 'body', 'type': 'String=global,only_domain,more_domain', 'name': 'tpl_type', 'required': False, 'default': None, 'description': '模板类型'})

    def __init__(self, business_id=_UNSET, page=_UNSET, page_size=_UNSET, domain=_UNSET, tpl_type=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if page is not _UNSET:
            self.body['page'] = page
        if page_size is not _UNSET:
            self.body['page_size'] = page_size
        if domain is not _UNSET:
            self.body['domain'] = domain
        if tpl_type is not _UNSET:
            self.body['tpl_type'] = tpl_type
        for key, value in kwargs.items():
            self.body[key] = value


class BindTemplateDomainRequest(BaseRequest):
    """模板绑定域名.

    API: POST /api/v5/security_protection/template/domain/bind

    Parameters:
        business_id (Number, required): 模板ID
        domain_ids (Number[], optional): 域名ID列表
        bind_business_ids (Number[], optional): 绑定模板ID列表
    """
    API_NAME = 'BindTemplateDomain'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/security_protection/template/domain/bind'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '模板ID'}, {'in': 'body', 'type': 'Number[]', 'name': 'domain_ids', 'required': False, 'default': None, 'description': '域名ID列表'}, {'in': 'body', 'type': 'Number[]', 'name': 'bind_business_ids', 'required': False, 'default': None, 'description': '绑定模板ID列表'})

    def __init__(self, business_id=_UNSET, domain_ids=_UNSET, bind_business_ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if domain_ids is not _UNSET:
            self.body['domain_ids'] = domain_ids
        if bind_business_ids is not _UNSET:
            self.body['bind_business_ids'] = bind_business_ids
        for key, value in kwargs.items():
            self.body[key] = value


class DeleteTemplateRequest(BaseRequest):
    """删除模板.

    API: DELETE /api/v5/security_protection/template

    Parameters:
        business_id (Number, required): 模板ID
    """
    API_NAME = 'DeleteTemplate'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/security_protection/template'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '模板ID'},)

    def __init__(self, business_id=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        for key, value in kwargs.items():
            self.body[key] = value


class BatchConfigTemplateRequest(BaseRequest):
    """模板批量配置.

    API: POST /api/v5/security_protection/template/batch/config

    Parameters:
        template_ids (Number[], required): 模板ID列表
        ddos_config (Object, optional): DDoS配置
        precise_access_control_config (Object, optional): 精准访问控制配置
        waf_rule_config (Object, optional): WAF规则配置
        bot_management_config (Object, optional): Bot管理配置
    """
    API_NAME = 'BatchConfigTemplate'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/security_protection/template/batch/config'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'template_ids', 'required': True, 'default': None, 'description': '模板ID列表'}, {'in': 'body', 'type': 'Object', 'name': 'ddos_config', 'required': False, 'default': None, 'description': 'DDoS配置'}, {'in': 'body', 'type': 'Object', 'name': 'precise_access_control_config', 'required': False, 'default': None, 'description': '精准访问控制配置'}, {'in': 'body', 'type': 'Object', 'name': 'waf_rule_config', 'required': False, 'default': None, 'description': 'WAF规则配置'}, {'in': 'body', 'type': 'Object', 'name': 'bot_management_config', 'required': False, 'default': None, 'description': 'Bot管理配置'})

    def __init__(self, template_ids=_UNSET, ddos_config=_UNSET, precise_access_control_config=_UNSET, waf_rule_config=_UNSET, bot_management_config=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if template_ids is not _UNSET:
            self.body['template_ids'] = template_ids
        if ddos_config is not _UNSET:
            self.body['ddos_config'] = ddos_config
        if precise_access_control_config is not _UNSET:
            self.body['precise_access_control_config'] = precise_access_control_config
        if waf_rule_config is not _UNSET:
            self.body['waf_rule_config'] = waf_rule_config
        if bot_management_config is not _UNSET:
            self.body['bot_management_config'] = bot_management_config
        for key, value in kwargs.items():
            self.body[key] = value


class IotaRequest(BaseRequest):
    """获取枚举值.

    API: GET /api/v5/security_protection/template/iota
    """
    API_NAME = 'Iota'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/security_protection/template/iota'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class GetUnboundTemplateDomainListRequest(BaseRequest):
    """获取未绑定模板域名.

    API: POST /api/v5/security_protection/template/domain/unbound/search
    """
    API_NAME = 'GetUnboundTemplateDomainList'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/security_protection/template/domain/unbound/search'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.body[key] = value


class EditTemplateRequest(BaseRequest):
    """编辑模板.

    API: PUT /api/v5/security_protection/template

    Parameters:
        business_id (Number, required): 模板ID
        name (String, required): 模板名称
        remark (String, optional): 备注
    """
    API_NAME = 'EditTemplate'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/security_protection/template'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '模板ID'}, {'in': 'body', 'type': 'String', 'name': 'name', 'required': True, 'default': None, 'description': '模板名称'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': False, 'default': None, 'description': '备注'})

    def __init__(self, business_id=_UNSET, name=_UNSET, remark=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if name is not _UNSET:
            self.body['name'] = name
        if remark is not _UNSET:
            self.body['remark'] = remark
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallSavePolicyGroupRegionalShieldingRequest(BaseRequest):
    """开启区域屏蔽.

    API: POST /api/v5/firewall.policyGroup.save

    Parameters:
        business_id (Number, required): 模板ID
        from (String=zL, required): 策略集来源，固定为zL（区域屏蔽）
        name (String=zL, required): 名称，固定为zL（区域屏蔽）
    """
    API_NAME = 'Firewall_savePolicyGroupRegionalShielding'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policyGroup.save'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '模板ID'}, {'in': 'body', 'type': 'String=zL', 'name': 'from', 'required': True, 'default': None, 'description': '策略集来源，固定为zL（区域屏蔽）'}, {'in': 'body', 'type': 'String=zL', 'name': 'name', 'required': True, 'default': None, 'description': '名称，固定为zL（区域屏蔽）'})

    def __init__(self, business_id=_UNSET, from=_UNSET, name=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if from is not _UNSET:
            self.body['from'] = from
        if name is not _UNSET:
            self.body['name'] = name
        for key, value in kwargs.items():
            self.body[key] = value


class FirewallSavePolicyGroupAntiLeechRequest(BaseRequest):
    """开启防盗链.

    API: POST /api/v5/firewall.policyGroup.save

    Parameters:
        business_id (Number, required): 模板ID
        from (String=aR, required): 策略集来源，固定为aR（防盗链）
        name (String=aR, required): 名称，固定为aR（防盗链）
    """
    API_NAME = 'Firewall_savePolicyGroupAntiLeech'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policyGroup.save'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'business_id', 'required': True, 'default': None, 'description': '模板ID'}, {'in': 'body', 'type': 'String=aR', 'name': 'from', 'required': True, 'default': None, 'description': '策略集来源，固定为aR（防盗链）'}, {'in': 'body', 'type': 'String=aR', 'name': 'name', 'required': True, 'default': None, 'description': '名称，固定为aR（防盗链）'})

    def __init__(self, business_id=_UNSET, from=_UNSET, name=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if business_id is not _UNSET:
            self.body['business_id'] = business_id
        if from is not _UNSET:
            self.body['from'] = from
        if name is not _UNSET:
            self.body['name'] = name
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdappsaveFirewallPolicyRequest(BaseRequest):
    """保存精准访问控制策略.

    API: POST /api/v5/firewall.policy.save

    Parameters:
        id (String, optional): 策略ID. 针对更新策略时使用
        tjkd_app_id (String, required): 套餐的package_id.
        type (String, required): 类型 app.
        rules (Array, required): 规则列表.
        rules.rule_type (String, required): 规则类型 ip/cpu_arch.
        rules.logic (String, required): 罗辑运算，每个规则能用的逻辑操作，请查看 获取可用规则(firewall.pagecfg) 接口
        rules.data (Array, required): 规则数据.
        rules.data_type (String, optional): 数据类型.
        action (String, required): 处理⽅式: deny(阻断)/pass(放行)/watch(观察)/block(封禁)
        action_data.interval (Number, optional): 有效期，针对 封禁 处理方式
        action_data.time_unit (String, optional): 封禁时间单位: day(天)/hour(时)/minute(分)/second(秒)，针对 封禁 处理方式
        remark (String, required): 备注.
        status (String, required): 状态.
    """
    API_NAME = 'TjkdappsaveFirewallPolicy'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policy.save'
    PARAMS = ({'in': 'body', 'type': 'String', 'name': 'id', 'required': False, 'default': None, 'description': '策略ID. 针对更新策略时使用'}, {'in': 'body', 'type': 'String', 'name': 'tjkd_app_id', 'required': True, 'default': None, 'description': '套餐的package_id.'}, {'in': 'body', 'type': 'String', 'name': 'type', 'required': True, 'default': None, 'description': '类型 app.'}, {'in': 'body', 'type': 'Array', 'name': 'rules', 'required': True, 'default': None, 'description': '规则列表.'}, {'in': 'body', 'type': 'String', 'name': 'rules.rule_type', 'required': True, 'default': None, 'description': '规则类型 ip/cpu_arch.'}, {'in': 'body', 'type': 'String', 'name': 'rules.logic', 'required': True, 'default': None, 'description': '罗辑运算，每个规则能用的逻辑操作，请查看 获取可用规则(firewall.pagecfg) 接口'}, {'in': 'body', 'type': 'Array', 'name': 'rules.data', 'required': True, 'default': None, 'description': '规则数据.'}, {'in': 'body', 'type': 'String', 'name': 'rules.data_type', 'required': False, 'default': None, 'description': '数据类型.'}, {'in': 'body', 'type': 'String', 'name': 'action', 'required': True, 'default': None, 'description': '处理⽅式: deny(阻断)/pass(放行)/watch(观察)/block(封禁)'}, {'in': 'body', 'type': 'Number', 'name': 'action_data.interval', 'required': False, 'default': None, 'description': '有效期，针对 封禁 处理方式'}, {'in': 'body', 'type': 'String', 'name': 'action_data.time_unit', 'required': False, 'default': None, 'description': '封禁时间单位: day(天)/hour(时)/minute(分)/second(秒)，针对 封禁 处理方式'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': True, 'default': None, 'description': '备注.'}, {'in': 'body', 'type': 'String', 'name': 'status', 'required': True, 'default': None, 'description': '状态.'})

    def __init__(self, tjkd_app_id=_UNSET, type=_UNSET, rules=_UNSET, action=_UNSET, remark=_UNSET, status=_UNSET, id=_UNSET, action_data=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if tjkd_app_id is not _UNSET:
            self.body['tjkd_app_id'] = tjkd_app_id
        if type is not _UNSET:
            self.body['type'] = type
        if rules is not _UNSET:
            self.body['rules'] = rules
        if action is not _UNSET:
            self.body['action'] = action
        if remark is not _UNSET:
            self.body['remark'] = remark
        if status is not _UNSET:
            self.body['status'] = status
        if id is not _UNSET:
            self.body['id'] = id
        if action_data is not _UNSET:
            self.body['action_data'] = action_data
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdappsortFirewallPolicyRequest(BaseRequest):
    """排序精准访问控制策略.

    API: POST /api/v5/firewall.policy.sort

    Parameters:
        new_sorts (Object, required): 新的排序映射.
    """
    API_NAME = 'TjkdappsortFirewallPolicy'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policy.sort'
    PARAMS = ({'in': 'body', 'type': 'Object', 'name': 'new_sorts', 'required': True, 'default': None, 'description': '新的排序映射.'},)

    def __init__(self, new_sorts=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if new_sorts is not _UNSET:
            self.body['new_sorts'] = new_sorts
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdappopenFirewallPolicyRequest(BaseRequest):
    """启动精准访问控制策略.

    API: POST /api/v5/firewall.policy.open

    Parameters:
        ids (Array, required): 策略ID列表.
    """
    API_NAME = 'TjkdappopenFirewallPolicy'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policy.open'
    PARAMS = ({'in': 'body', 'type': 'Array', 'name': 'ids', 'required': True, 'default': None, 'description': '策略ID列表.'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdappstopFirewallPolicyRequest(BaseRequest):
    """暂停精准访问控制策略.

    API: POST /api/v5/firewall.policy.stop

    Parameters:
        ids (Array, required): 策略ID列表.
    """
    API_NAME = 'TjkdappstopFirewallPolicy'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policy.stop'
    PARAMS = ({'in': 'body', 'type': 'Array', 'name': 'ids', 'required': True, 'default': None, 'description': '策略ID列表.'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class TjkdappgetFirewallPolicyRequest(BaseRequest):
    """获取精准访问控制策略列表.

    API: GET /api/v5/firewall.policy.get_tjkdappid
    """
    API_NAME = 'TjkdappgetFirewallPolicy'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/firewall.policy.get_tjkdappid'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class TjkdappdeleteFirewallPolicyRequest(BaseRequest):
    """删除精准访问控制策略.

    API: POST /api/v5/firewall.policy.delete

    Parameters:
        ids (Array, required): 策略ID列表.
    """
    API_NAME = 'TjkdappdeleteFirewallPolicy'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/firewall.policy.delete'
    PARAMS = ({'in': 'body', 'type': 'Array', 'name': 'ids', 'required': True, 'default': None, 'description': '策略ID列表.'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class AddForwardRuleRequest(BaseRequest):
    """添加转发规则.

    API: POST /api/v5/tjkd.app.domain.add

    Parameters:
        package_id (Number, required): 套餐ID.
        domain (String, required): 域名.
        protocol (Number, required): 协议 1 tcp
        port (String, required): 端口号.
        loading (Number, required): 负载均衡 1 轮询 2 ip哈希.
        remark (String, required): 备注信息.
        source_type (Number, required): 源类型 1 IP 2 域名.
        source_list (Array, required): 源站列表.
        source_list.ip (String, required): 源站IP地址.
        source_list.port (String, required): 源站端口.
        source_list.backup (Number, required): 主备 1是主 2是备
        channel_status (Number, required): 加速通道是否开启 1 开启 0 关闭.
        channel_loading (Number, optional): 加速通道负载均衡 1 轮询 2 ip哈希.
        channel_source_list (Array, optional): 加速通道源数据列表.
        channel_source_list.id (Number, optional): 加速通道ID.
        channel_source_list.backup (Number, optional): 主备 1是主 2是备
    """
    API_NAME = 'addForwardRule'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/tjkd.app.domain.add'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'package_id', 'required': True, 'default': None, 'description': '套餐ID.'}, {'in': 'body', 'type': 'String', 'name': 'domain', 'required': True, 'default': None, 'description': '域名.'}, {'in': 'body', 'type': 'Number', 'name': 'protocol', 'required': True, 'default': None, 'description': '协议 1 tcp'}, {'in': 'body', 'type': 'String', 'name': 'port', 'required': True, 'default': None, 'description': '端口号.'}, {'in': 'body', 'type': 'Number', 'name': 'loading', 'required': True, 'default': None, 'description': '负载均衡 1 轮询 2 ip哈希.'}, {'in': 'body', 'type': 'String', 'name': 'remark', 'required': True, 'default': None, 'description': '备注信息.'}, {'in': 'body', 'type': 'Number', 'name': 'source_type', 'required': True, 'default': None, 'description': '源类型 1 IP 2 域名.'}, {'in': 'body', 'type': 'Array', 'name': 'source_list', 'required': True, 'default': None, 'description': '源站列表.'}, {'in': 'body', 'type': 'String', 'name': 'source_list.ip', 'required': True, 'default': None, 'description': '源站IP地址.'}, {'in': 'body', 'type': 'String', 'name': 'source_list.port', 'required': True, 'default': None, 'description': '源站端口.'}, {'in': 'body', 'type': 'Number', 'name': 'source_list.backup', 'required': True, 'default': None, 'description': '主备 1是主 2是备'}, {'in': 'body', 'type': 'Number', 'name': 'channel_status', 'required': True, 'default': None, 'description': '加速通道是否开启 1 开启 0 关闭.'}, {'in': 'body', 'type': 'Number', 'name': 'channel_loading', 'required': False, 'default': None, 'description': '加速通道负载均衡 1 轮询 2 ip哈希.'}, {'in': 'body', 'type': 'Array', 'name': 'channel_source_list', 'required': False, 'default': None, 'description': '加速通道源数据列表.'}, {'in': 'body', 'type': 'Number', 'name': 'channel_source_list.id', 'required': False, 'default': None, 'description': '加速通道ID.'}, {'in': 'body', 'type': 'Number', 'name': 'channel_source_list.backup', 'required': False, 'default': None, 'description': '主备 1是主 2是备'})

    def __init__(self, package_id=_UNSET, domain=_UNSET, protocol=_UNSET, port=_UNSET, loading=_UNSET, remark=_UNSET, source_type=_UNSET, source_list=_UNSET, channel_status=_UNSET, channel_loading=_UNSET, channel_source_list=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if package_id is not _UNSET:
            self.body['package_id'] = package_id
        if domain is not _UNSET:
            self.body['domain'] = domain
        if protocol is not _UNSET:
            self.body['protocol'] = protocol
        if port is not _UNSET:
            self.body['port'] = port
        if loading is not _UNSET:
            self.body['loading'] = loading
        if remark is not _UNSET:
            self.body['remark'] = remark
        if source_type is not _UNSET:
            self.body['source_type'] = source_type
        if source_list is not _UNSET:
            self.body['source_list'] = source_list
        if channel_status is not _UNSET:
            self.body['channel_status'] = channel_status
        if channel_loading is not _UNSET:
            self.body['channel_loading'] = channel_loading
        if channel_source_list is not _UNSET:
            self.body['channel_source_list'] = channel_source_list
        for key, value in kwargs.items():
            self.body[key] = value


class DeleteForwardRuleRequest(BaseRequest):
    """删除转发规则.

    API: DELETE /api/v5/tjkd.app.domain.del

    Parameters:
        ids (Number[], required): 要删除的转发规则ID
    """
    API_NAME = 'deleteForwardRule'
    METHOD = 'DELETE'
    METHODS = ('DELETE',)
    PATH = '/api/v5/tjkd.app.domain.del'
    PARAMS = ({'in': 'body', 'type': 'Number[]', 'name': 'ids', 'required': True, 'default': None, 'description': '要删除的转发规则ID'},)

    def __init__(self, ids=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if ids is not _UNSET:
            self.body['ids'] = ids
        for key, value in kwargs.items():
            self.body[key] = value


class EditRuleRequest(BaseRequest):
    """修改规则.

    API: POST /api/v5/tjkd.app.domain.edit

    Parameters:
        id (Number, required): 规则ID.
        package_id (Number, required): 套餐ID.
        protocol (Number, required): 协议 1 tcp
        domain (String, required): 域名.
        port (Number, required): 端口号.
        loading (Number, required): 负载均衡 1 轮询 2 ip哈希.
        source_type (Number, required): 源类型 1 IP2 域名.
        source_list (Array, required): 源数据.
        source_list.ip (String, required): 源站IP地址.
        source_list.port (String, required): 源站端口.
        source_list.backup (Number, required): 主备 1是主 2是备
        channel_status (Number, required): 加速通道是否开启 1 开启 0 关闭.
        channel_loading (Number, optional): 加速通道负载均衡 1 轮询 2 ip哈希.
        channel_source_list (Array, optional): 加速通道源数据列表.
        channel_source_list.id (Number, optional): 加速通道ID.
        channel_source_list.backup (Number, optional): 主备 1是主 2是备
    """
    API_NAME = 'editRule'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/tjkd.app.domain.edit'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'id', 'required': True, 'default': None, 'description': '规则ID.'}, {'in': 'body', 'type': 'Number', 'name': 'package_id', 'required': True, 'default': None, 'description': '套餐ID.'}, {'in': 'body', 'type': 'Number', 'name': 'protocol', 'required': True, 'default': None, 'description': '协议 1 tcp'}, {'in': 'body', 'type': 'String', 'name': 'domain', 'required': True, 'default': None, 'description': '域名.'}, {'in': 'body', 'type': 'Number', 'name': 'port', 'required': True, 'default': None, 'description': '端口号.'}, {'in': 'body', 'type': 'Number', 'name': 'loading', 'required': True, 'default': None, 'description': '负载均衡 1 轮询 2 ip哈希.'}, {'in': 'body', 'type': 'Number', 'name': 'source_type', 'required': True, 'default': None, 'description': '源类型 1 IP2 域名.'}, {'in': 'body', 'type': 'Array', 'name': 'source_list', 'required': True, 'default': None, 'description': '源数据.'}, {'in': 'body', 'type': 'String', 'name': 'source_list.ip', 'required': True, 'default': None, 'description': '源站IP地址.'}, {'in': 'body', 'type': 'String', 'name': 'source_list.port', 'required': True, 'default': None, 'description': '源站端口.'}, {'in': 'body', 'type': 'Number', 'name': 'source_list.backup', 'required': True, 'default': None, 'description': '主备 1是主 2是备'}, {'in': 'body', 'type': 'Number', 'name': 'channel_status', 'required': True, 'default': None, 'description': '加速通道是否开启 1 开启 0 关闭.'}, {'in': 'body', 'type': 'Number', 'name': 'channel_loading', 'required': False, 'default': None, 'description': '加速通道负载均衡 1 轮询 2 ip哈希.'}, {'in': 'body', 'type': 'Array', 'name': 'channel_source_list', 'required': False, 'default': None, 'description': '加速通道源数据列表.'}, {'in': 'body', 'type': 'Number', 'name': 'channel_source_list.id', 'required': False, 'default': None, 'description': '加速通道ID.'}, {'in': 'body', 'type': 'Number', 'name': 'channel_source_list.backup', 'required': False, 'default': None, 'description': '主备 1是主 2是备'})

    def __init__(self, id=_UNSET, package_id=_UNSET, protocol=_UNSET, domain=_UNSET, port=_UNSET, loading=_UNSET, source_type=_UNSET, source_list=_UNSET, channel_status=_UNSET, channel_loading=_UNSET, channel_source_list=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if id is not _UNSET:
            self.body['id'] = id
        if package_id is not _UNSET:
            self.body['package_id'] = package_id
        if protocol is not _UNSET:
            self.body['protocol'] = protocol
        if domain is not _UNSET:
            self.body['domain'] = domain
        if port is not _UNSET:
            self.body['port'] = port
        if loading is not _UNSET:
            self.body['loading'] = loading
        if source_type is not _UNSET:
            self.body['source_type'] = source_type
        if source_list is not _UNSET:
            self.body['source_list'] = source_list
        if channel_status is not _UNSET:
            self.body['channel_status'] = channel_status
        if channel_loading is not _UNSET:
            self.body['channel_loading'] = channel_loading
        if channel_source_list is not _UNSET:
            self.body['channel_source_list'] = channel_source_list
        for key, value in kwargs.items():
            self.body[key] = value


class RuleListRequest(BaseRequest):
    """规则列表.

    API: GET/POST /api/v5/tjkd.app.domain.list

    Parameters:
        page (Number, optional): 页数.
        pre_page (Number, optional): 分页大小.
        order (String="id desc", optional): 排序.
        package_id (Number, required): 套餐ID
    """
    API_NAME = 'ruleList'
    METHOD = 'GET'
    METHODS = ('GET', 'POST')
    PATH = '/api/v5/tjkd.app.domain.list'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'page', 'required': False, 'default': None, 'description': '页数.'}, {'in': 'body', 'type': 'Number', 'name': 'pre_page', 'required': False, 'default': None, 'description': '分页大小.'}, {'in': 'body', 'type': 'String="id desc"', 'name': 'order', 'required': False, 'default': None, 'description': '排序.'}, {'in': 'body', 'type': 'Number', 'name': 'package_id', 'required': True, 'default': None, 'description': '套餐ID'})

    def __init__(self, package_id=_UNSET, page=_UNSET, pre_page=_UNSET, order=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if package_id is not _UNSET:
            self.body['package_id'] = package_id
        if page is not _UNSET:
            self.body['page'] = page
        if pre_page is not _UNSET:
            self.body['pre_page'] = pre_page
        if order is not _UNSET:
            self.body['order'] = order
        for key, value in kwargs.items():
            self.query[key] = value


class GetRuleInfoRequest(BaseRequest):
    """获取规则详情.

    API: GET /api/v5/tjkd.app.domain.info
    """
    API_NAME = 'getRuleInfo'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/tjkd.app.domain.info'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class TijkdappListPackageRequest(BaseRequest):
    """套餐列表.

    API: GET /api/v5/tjkd.app.package.list
    """
    API_NAME = 'TIJKDAPP_ListPackage'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/tjkd.app.package.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class TijkdappSavePackageRequest(BaseRequest):
    """套餐名称修改.

    API: PUT /api/v5/tjkd.app.package.save

    Parameters:
        package_id (Number, required): 套餐ID
        package_name (String, required): 套餐名称
    """
    API_NAME = 'TIJKDAPP_SavePackage'
    METHOD = 'PUT'
    METHODS = ('PUT',)
    PATH = '/api/v5/tjkd.app.package.save'
    PARAMS = ({'in': 'body', 'type': 'Number', 'name': 'package_id', 'required': True, 'default': None, 'description': '套餐ID'}, {'in': 'body', 'type': 'String', 'name': 'package_name', 'required': True, 'default': None, 'description': '套餐名称'})

    def __init__(self, package_id=_UNSET, package_name=_UNSET, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        if package_id is not _UNSET:
            self.body['package_id'] = package_id
        if package_name is not _UNSET:
            self.body['package_name'] = package_name
        for key, value in kwargs.items():
            self.body[key] = value


class GetChannelListRequest(BaseRequest):
    """套餐加速通道列表.

    API: GET /api/v5/tjkd.app.package.channel.list
    """
    API_NAME = 'getChannelList'
    METHOD = 'GET'
    METHODS = ('GET',)
    PATH = '/api/v5/tjkd.app.package.channel.list'
    PARAMS = ()

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.query[key] = value


class ApiNameV5Request(BaseRequest):
    """SDK API 5.0.0示例.

    API: POST /api/v5/api对应路由NAME

    Parameters:
        x-lang (String=zh,en, optional, default=zh): 设置api使用的语言.
    """
    API_NAME = 'api_name_v5'
    METHOD = 'POST'
    METHODS = ('POST',)
    PATH = '/api/v5/api对应路由NAME'
    PARAMS = ({'in': 'header', 'type': 'String=zh,en', 'name': 'x-lang', 'required': False, 'default': 'zh', 'description': '设置api使用的语言.'},)

    def __init__(self, query=None, body=None, headers=None, **kwargs):
        super().__init__(query=query, body=body, headers=headers)
        for key, value in kwargs.items():
            self.body[key] = value


__all__ = ["BaseRequest", "CdnHighDefenseIpGetArticleIpRequest", "DnsDomainGetDomainListRequest", "DnsDomainAddDomainRequest", "DnsDomainBatchAddDomainsRequest", "DnsDomainBatchDeleteDomainsRequest", "DnsDomainGetDomainStatRequest", "DnsDomainGetDomainServersRequest", "DnsDomainGetTasksListRequest", "DnsDomainGetTaskDetailRequest", "CloudDnsDomainGroupGetGroupListRequest", "CloudDnsDomainGroupAddGroupRequest", "CloudDnsDomainGroupUpdateGroupRequest", "CloudDnsDomainGroupDeleteGroupRequest", "CloudDnsDomainGroupGetGroupRecordListRequest", "CloudDnsDomainGroupSaveDomainToGroupRequest", "CloudDnsDomainGroupGetGroupDomainListRequest", "CloudDnsDomainGroupGetGroupUndistributedDomainListRequest", "DnsDomainRecordsGetRecordTypesRequest", "DnsDomainRecordsGetRecordListRequest", "DnsDomainRecordsAddRecordRequest", "DnsDomainRecordsBatchAddRecordsRequest", "DnsDomainRecordsEditRecordRequest", "DnsDomainRecordsBatchPauseRecordsRequest", "DnsDomainRecordsBatchEnableRecordsRequest", "DnsDomainRecordsDeleteRecordRequest", "DnsDomainRecordsImportRecordsRequest", "DnsDomainRecordsExportRecordsRequest", "DnsDomainRecordsGetLinesRequest", "DnsDomainRecordsBatchDeleteRecordsRequest", "DnsDomainRecordsGetRecordGroupsListRequest", "DnsDomainRecordsAddRecordGroupRequest", "DnsDomainRecordsAddRecordGroupRelationsRequest", "DnsDomainRecordsDeleteRecordGroupRequest", "UserIpUserIpListRequest", "UserIpUserIpAddRequest", "UserIpUserIpSaveRequest", "UserIpUserIpDelRequest", "UserIpListUserIpItemRequest", "UserIpAddUserIpItemRequest", "UserIpUpdateUserIpItemRequest", "UserIpBatchDeleteUserIpItemRequest", "UserIpDeleteAllUserIpItemRequest", "UserIpCopyUserIpRequest", "UserIpFileSaveIpItemRequest", "ServiceBatchListTaskRequest", "ServiceBatchListSubTaskRequest", "WebCdnCleanCacheGetCacheListRequest", "WebCdnCleanCacheSaveCacheRequest", "WebCdnCleanCacheGetTaskListRequest", "WebCdnCleanCacheGetTaskDetailRequest", "WebCdnPreheatCacheGetPreheatCacheQuotaRequest", "WebCdnPreheatCacheGetPreheatCacheListRequest", "WebCdnPreheatCacheSavePreheatCacheRequest", "OplogInfoRequest", "OplogMapRequest", "OplogGetOplogsRequest", "CaCertificateSelfAddCaRequest", "BatchCaListRequest", "CaCertificateSelfSaveTextCaInfoRequest", "CaCertificateSelfEditCaInfoRequest", "CaCertificateSelfListCaRequest", "CaCertificateSelfCaExportRequest", "CaCertificateSelfBatchOperatSslRequest", "CaCertificateSelfDelCaRequest", "CaCertificateSelfGetCaDetailRequest", "CaCertificateSelfEditCaNameRequest", "CaCertificateApplyAddApplyCaRequest", "CaCertificateApplyGetAddByNsSettingRequest", "DomainGroupSaveGroupRequest", "DomainGroupGetGroupListRequest", "DomainGroupDelGroupRequest", "DomainGroupGetGroupDomainListRequest", "DomainGroupGgtUndistributedDomainListRequest", "DomainGroupAddGroupRequest", "DomainGroupSaveDomainToGroupRequest", "DomainGroupGetGroupInfoRequest", "DomainGroupMoveDomainRequest", "ListDomainsRequest", "AddDomainsRequest", "UpdateDomainsRequest", "BindDomainCertRequest", "UnBindDomainCertRequest", "DeleteDomainsRequest", "DisableDomainsRequest", "EnableDomainsRequest", "RefreshDomainsAccessRequest", "ExportDomainsRequest", "AddOriginsRequest", "UpdateOriginsRequest", "DeleteOriginsRequest", "ListOriginsRequest", "SwitchDomainNodesRequest", "SwitchDomainAccessModeRequest", "UpdateDomainBaseSettingsRequest", "GetDomainBaseSettingsRequest", "ListBriefDomainsRequest", "GetDomainTemplatesRequest", "AccessInfoDownloadRequest", "OriginGroupGetOriginGroupListRequest", "OriginGroupGetOriginGroupInfoRequest", "OriginGroupAddOriginGroupRequest", "OriginGroupUpdateOriginGroupRequest", "OriginGroupDelOriginGroupRequest", "OriginGroupBindOriginGroupToDomainsRequest", "OriginGroupGetAllOriginGroupsRequest", "OriginGroupCopyOriginGroupRequest", "FireWallReportGetBlockListRequest", "FireWallReportGetBlockDetailsRequest", "FireWallReportGetPackageBlockListRequest", "FireWallReportGetPackageBlockDetailsRequest", "CcQpsMaxRequest", "CcAttackTimesRequest", "CcTimesLineRequest", "CcReportStatsRequest", "CdnDomainUaispDistributeRequest", "CdnDomainCountryDistributeRequest", "CdnDomainProvinceDistributeRequest", "CdnDomainStatusDistributeRequest", "CdnDomainNodeFlowBandwidthRequest", "CdnDomainNodeFlowBandwidthCn2Request", "CdnDomainNodeFlowBandwidthNodeRequest", "DomainTimesRequest", "DomainQpsRequest", "CdnDomainFlowLineRequest", "CdnDomainBandwidthLineRequest", "CdnDomainBandwidth95Request", "CdnDomainPvtimesRequest", "CdnDomainFlowTopRequest", "CdnDomainBandwidthTopRequest", "CdnDomainTimesTopRequest", "CdnDomainTimesTopEsRequest", "CdnDomainUrlTopRequest", "CdnDomainRefererTopRequest", "CdnDomainStatusTopDownloadRequest", "CdnDomainBandwidthDownloadRequest", "CdnDomainFlowDownloadRequest", "TcpBandwidthRequest", "TcpCcFlawRequest", "WafAttackTimesRequest", "WafReportStatsRequest", "WafWebshellEventListRequest", "WafWebshellEventDetailRequest", "WafAttackEventListRequest", "WafAttackEventDetailRequest", "WafScanEventListRequest", "WafScanEventDetailRequest", "WafTypeLineRequest", "LogDownloadTaskTaskListRequest", "LogDownloadTaskAddTaskRequest", "LogDownloadTaskCancelTaskRequest", "LogDownloadTaskBatchCancelTaskRequest", "LogDownloadTaskDeleteTaskRequest", "LogDownloadTaskBatchDeleteTaskRequest", "LogDownloadTaskRegenerateTaskRequest", "LogDownloadFieldConfDownloadFieldsRequest", "LogDownloadTemplateTemplateListRequest", "LogDownloadTemplateGetTemplateDomainListRequest", "LogDownloadTemplateAddTemplateRequest", "LogDownloadTemplateSaveTemplateRequest", "LogDownloadTemplateDelTemplateRequest", "LogDownloadTemplateBatchDelTemplateRequest", "LogDownloadTemplateChangeStatusRequest", "LogDownloadTemplateBatchChangeStatusRequest", "LogDownloadTemplateAllTemplateRequest", "LogDownloadTemplateAllTemplateGroupRequest", "TjkdPlusPackageGetMemberPackageListRequest", "TjkdPlusPackageGetAllPackageRequest", "TjkdPlusPackageGetPackageInfoRequest", "TjkdPlusPackageGetPackageIpListRequest", "TjkdPlusPackageGetPackageOverviewRequest", "TjkdPlusPackageGetPackagePortListRequest", "TjkdPlusPackageSavePackageRequest", "TjkdPlusPackageSavePackageHealthyConfRequest", "TjkdPlusForwardRuleSavePlusForwardRuleRequest", "TjkdPlusForwardRuleBatchAddPlusForwardRuleRequest", "TjkdPlusForwardRuleBatchSavePlusForwardRuleRequest", "TjkdPlusForwardRuleDelPlusForwardRuleRequest", "TjkdPlusForwardRuleGetPlusForwardRuleListRequest", "TjkdPlusForwardRuleGetBatchPlusForwardRuleInfoRequest", "TjkdPlusPackageGetPackageDomainListRequest", "TjkdPlusDomainGetTjkdPlusDomainListRequest", "TjkdPlusDomainAddTjkdPlusDomainRequest", "TjkdPlusDomainDelTjkdPlusDomainRequest", "NetworkSpeedGetCacheRuleListRequest", "NetworkSpeedCreateCacheRuleRequest", "NetworkSpeedUpdateCacheRuleRequest", "NetworkSpeedUpdateCacheRuleConfigRequest", "NetworkSpeedUpdateCacheRuleStatusRequest", "NetworkSpeedSortCacheRulesRequest", "NetworkSpeedGetGlobalCacheConfigRequest", "NetworkSpeedDeleteCacheRuleRequest", "NetworkSpeedGetTemplateConfigRequest", "NetworkSpeedUpdateTemplateConfigRequest", "NetworkSpeedGetRulesRequest", "NetworkSpeedCreateRuleRequest", "NetworkSpeedDeleteRuleRequest", "NetworkSpeedSortRulesRequest", "NetworkSpeedUpdateRuleRequest", "UpdateRuleTemplateRequest", "DeleteRuleTemplateRequest", "GetRuleTemplateListRequest", "UnbindRuleTemplateRequest", "BindRuleTemplateRequest", "ListRuleTpsDomainsRequest", "CreateRuleTemplateRequest", "SwitchDomainTemplateRequest", "FirewallPageCfgRequest", "FirewallPageCfgHwwsRequest", "FirewallSavePolicyRequest", "FirewallGetPolicyRequest", "FirewallGetPolicyByCodeRequest", "FirewallStatsPolicyRequest", "FirewallOpenRequest", "FirewallStopRequest", "FirewallDeleteRequest", "FirewallSortRequest", "FirewallGetsPolicyByMainidRequest", "FirewallGetsPolicyByPackageidRequest", "FirewallSavePolicyGroupRequest", "FirewallGetsPolicyGroupByDomainidRequest", "FirewallStopGroupRequest", "FirewallOpenGroupRequest", "FirewallDeleteGroupRequest", "FirewallSortGroupRequest", "FirewallGetsPolicyByGroupIdRequest", "GetPolicyGroupTplRequest", "GetDdosProtectionConfigRequest", "UpdateDdosProtectionConfigRequest", "GetWafRuleConfigRequest", "UpdateWafRuleConfigRequest", "GetMemberGlobalTemplateRequest", "CreateTemplateRequest", "CreateDomainTemplateRequest", "GetTemplateListRequest", "GetTemplateBindDomainListRequest", "BindTemplateDomainRequest", "DeleteTemplateRequest", "BatchConfigTemplateRequest", "IotaRequest", "GetUnboundTemplateDomainListRequest", "EditTemplateRequest", "FirewallSavePolicyGroupRegionalShieldingRequest", "FirewallSavePolicyGroupAntiLeechRequest", "TjkdappsaveFirewallPolicyRequest", "TjkdappsortFirewallPolicyRequest", "TjkdappopenFirewallPolicyRequest", "TjkdappstopFirewallPolicyRequest", "TjkdappgetFirewallPolicyRequest", "TjkdappdeleteFirewallPolicyRequest", "AddForwardRuleRequest", "DeleteForwardRuleRequest", "EditRuleRequest", "RuleListRequest", "GetRuleInfoRequest", "TijkdappListPackageRequest", "TijkdappSavePackageRequest", "GetChannelListRequest", "ApiNameV5Request"]
