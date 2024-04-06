from web.cms.utils.cms.aliyun_cms import AliyunCMS


class DiskCheck(AliyunCMS):
    """获取ecs磁盘使用率"""

    def __init__(self, access_key_id, access_key_secret, endpoint='metrics.cn-hangzhou.aliyuncs.com'):
        super().__init__(access_key_id, access_key_secret, 'diskusage_utilization', endpoint=endpoint)


class MemoryCheck(AliyunCMS):
    """获取ecs内存使用率"""

    def __init__(self, access_key_id, access_key_secret, endpoint='metrics.cn-hangzhou.aliyuncs.com'):
        super().__init__(access_key_id, access_key_secret, 'memory_usedutilization', endpoint=endpoint)


class CPUCheck(AliyunCMS):
    """获取ecsCPU使用率"""

    def __init__(self, access_key_id, access_key_secret, endpoint='metrics.cn-hangzhou.aliyuncs.com'):
        super().__init__(access_key_id, access_key_secret, 'CPUUtilization', endpoint=endpoint)


class Load5Check(AliyunCMS):
    """获取ecs load_5"""

    def __init__(self, access_key_id, access_key_secret, endpoint='metrics.cn-hangzhou.aliyuncs.com'):
        super().__init__(access_key_id, access_key_secret, 'load_5m', endpoint=endpoint)


if __name__ == '__main__':
    # 创建链接
    client = DiskCheck('***REMOVED***', '***REMOVED***')
    # 获取监控指标
    disk_metric = client.get_metrics()
    print(disk_metric)
    # 创建链接
    client = MemoryCheck('access_key_id', 'access_key_secret')
    # 获取监控指标
    disk_metric = client.get_metrics()
    print(disk_metric)
    # 创建链接
    client = CPUCheck('access_key_id', 'access_key_secret')
    # 获取监控指标
    disk_metric = client.get_metrics()
    print(disk_metric)
    # 创建链接
    client = Load5Check('access_key_id', 'access_key_secret')
    # 获取监控指标
    disk_metric = client.get_metrics()
    print(disk_metric)
