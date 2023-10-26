from flask import current_app

from web.cms.utils.cms_check import DiskCheck, MemoryCheck, CPUCheck, Load5Check


# 过滤超过指定阈值的数据
def check_assess(data_list, check_type, value):
    check_list = []
    for data in data_list:
        if data['Average'] < value:
            current_app.logger.debug(
                '实例{0}, {1} average监控正常, {2}'.format(data['instanceId'], check_type, data['Average']))
        else:
            current_app.logger.debug(
                '实例{0}, {1} average监控异常, {2}'.format(data['instanceId'], check_type, data['Average']))
            check_list.append(data)
    return check_list


# 巡检CPU信息
def check_cms_cpu(auth):
    """巡检cpu信息"""
    alert_list = []
    # 获取巡检数据
    cpu_info = CPUCheck(auth['access_key_id'], auth['access_key_secret'], auth['endpoint']).get_metrics()
    current_app.logger.info('CPU信息: {0}'.format(cpu_info))
    return check_assess(cpu_info, 'cpu', 90)


# 巡检load5信息
def check_cms_load5(auth):
    """巡检LOAD5信息"""
    alert_list = []
    # 获取巡检数据
    load5_info = Load5Check(auth['access_key_id'], auth['access_key_secret'], auth['endpoint']).get_metrics()
    current_app.logger.info('LOAD5信息: {0}'.format(load5_info))
    return check_assess(load5_info, 'load5', 20)


# 巡检内存信息
def check_cms_memory(auth):
    """巡检内存信息"""
    alert_list = []
    # 获取巡检数据
    memory_info = MemoryCheck(auth['access_key_id'], auth['access_key_secret'], auth['endpoint']).get_metrics()
    current_app.logger.info('内存信息: {0}'.format(memory_info))
    return check_assess(memory_info, 'memory', 90)


# 巡检磁盘信息
def check_cms_disk(auth):
    """巡检磁盘信息"""
    alert_list = []
    # 获取巡检数据
    disk_info = DiskCheck(auth['access_key_id'], auth['access_key_secret'], auth['endpoint']).get_metrics()
    current_app.logger.info('磁盘信息: {0}'.format(disk_info))
    return check_assess(disk_info, 'disk', 2)


# 巡检所有项目
def check_cms_all(auth):
    alert = {'cpu': check_cms_cpu(auth), 'load5': check_cms_load5(auth), 'memory': check_cms_memory(auth),
             'disk': check_cms_disk(auth)}
    return alert
