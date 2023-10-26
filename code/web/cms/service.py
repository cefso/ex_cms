from flask import current_app

from web.cms.utils.cms_check import DiskCheck, MemoryCheck, CPUCheck, Load5Check

cpu_value = 90
load5_value = 10
memory_value = 90
disk_value = 90


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
    return check_assess(cpu_info, 'cpu', cpu_value)


# 巡检load5信息
def check_cms_load5(auth):
    """巡检LOAD5信息"""
    alert_list = []
    # 获取巡检数据
    load5_info = Load5Check(auth['access_key_id'], auth['access_key_secret'], auth['endpoint']).get_metrics()
    current_app.logger.info('LOAD5信息: {0}'.format(load5_info))
    return check_assess(load5_info, 'load5', load5_value)


# 巡检内存信息
def check_cms_memory(auth):
    """巡检内存信息"""
    alert_list = []
    # 获取巡检数据
    memory_info = MemoryCheck(auth['access_key_id'], auth['access_key_secret'], auth['endpoint']).get_metrics()
    current_app.logger.info('内存信息: {0}'.format(memory_info))
    return check_assess(memory_info, 'memory', memory_value)


# 巡检磁盘信息
def check_cms_disk(auth):
    """巡检磁盘信息"""
    alert_list = []
    # 获取巡检数据
    disk_info = DiskCheck(auth['access_key_id'], auth['access_key_secret'], auth['endpoint']).get_metrics()
    current_app.logger.info('磁盘信息: {0}'.format(disk_info))
    return check_assess(disk_info, 'disk', disk_value)


# 巡检所有项目
def check_cms_all(auth):
    check_info = {'cpu': check_cms_cpu(auth), 'load5': check_cms_load5(auth), 'memory': check_cms_memory(auth),
                  'disk': check_cms_disk(auth)}
    return check_info


def cover_to_markdown(check_info):
    card_markdown = '今日巡检: \n'
    card_foot = 'nihao'
    card_header = 'nihao'
    for i in ['cpu', 'load5', 'memory', 'disk']:
        if not check_info[i]:
            pass
        else:
            info_list = check_info[i]
            info_text = ''
            for info in info_list:
                if 'device' in info.keys():
                    text = '实例 {0}, {1} {2} 使用率 {3}% \n'.format(info['instanceId'], i, info['device'],
                                                                     info['Average'])
                    info_text += text
                elif i == 'load5':
                    text = '实例 {0}, {1} 当前值 {2} \n'.format(info['instanceId'], i, info['Average'])
                    info_text += text
                else:
                    text = '实例 {0}, {1} 使用率 {2}% \n'.format(info['instanceId'], i, info['Average'])
                    info_text += text
            card_markdown += info_text
    card_content = {
        'config': {
            'wide_screen_mode': 'true'
        },
        'elements': [
            {
                'tag': 'div',
                'text': {
                    'content': card_markdown,
                    'tag': 'lark_md'
                }
            },
            {
                'elements': [
                    {
                        'content': card_foot,
                        'tag': 'lark_md'
                    }
                ],
                'tag': 'note'
            }
        ],
        'header': {
            'template': 'blue',
            'title': {
                'content': card_header,
                'tag': 'plain_text'
            }
        }
    }
    return card_content
