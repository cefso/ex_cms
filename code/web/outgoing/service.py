import base64
import hashlib
import hmac

from flask import current_app

from web.alert.service import get_alert_list
from web.user.service import get_user_list


# 获取签名值
def get_sign(timestamp):
    # 获取应用的密钥
    app_secret = current_app.config.get('ROBOT_APP_SECRET')
    # 将密钥编码为 utf-8 格式
    app_secret_enc = app_secret.encode('utf-8')
    # 生成请求参数字符串，包括时间戳和应用密钥
    string_to_sign = '{}\n{}'.format(timestamp, app_secret)
    # 将请求参数字符串编码为 utf-8 格式
    string_to_sign_enc = string_to_sign.encode('utf-8')
    # 使用哈希算法和密钥计算签名
    hmac_code = hmac.new(app_secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    # 将哈希结果编码为 base64 格式，并解码为字符串
    sign = base64.b64encode(hmac_code).decode('utf-8')
    # 返回签名
    return sign


# 返回用户列表
def markdown_user_list():
    user_pagination, user_list = get_user_list()
    mk_user_list = ''
    index = 1
    for user in user_list:
        mk_user = '{}. {}({})\n\n'.format(index, user['userName'], user['userId'])
        mk_user_list = mk_user_list + mk_user
        index = index + 1
    mk_user_list = mk_user_list + '> page:{}  page_size:{}  total:{}'.format(user_pagination.page,
                                                                             user_pagination.per_page,
                                                                             user_pagination.total)
    return mk_user_list


# 返回告警列表
def markdown_alert_list(user_name=None):
    # 判断是否是查询特定用户告警
    if user_name is None:
        alert_pagination, alert_list = get_alert_list()
    else:
        alert_pagination, alert_list = get_alert_list(user_name)
    mk_alert_list = ''
    index = 1
    for alert in alert_list:
        # p判断unit为None，则用’ ‘填充
        if alert['unit'] is None:
            alert['unit'] = ' '
        mk_alert = '{}. {}({}), {} {},{}\n\n'.format(index, alert['alertName'], alert['ruleId'], alert['instanceName'],
                                                     alert['curValue'] + alert['unit'], alert['lastTime'])
        mk_alert_list = mk_alert_list + mk_alert
        index = index + 1
    mk_alert_list = mk_alert_list + '> page:{}  page_size:{}  total:{}'.format(alert_pagination.page,
                                                                               alert_pagination.per_page,
                                                                               alert_pagination.total)
    return mk_alert_list


def check_content(content):
    # 删除多余空格, 避免对后续判断造成影响
    content = content.split()
    match content:
        case ['功能列表'] | ['帮助']:
            return {
                "msgtype": "markdown",
                "markdown": {
                    "title": "功能列表",
                    "text": "1. 告警列表(1 用户名，可获取指定用户的告警列表)\n\n2. 屏蔽告警列表\n\n3. 用户列表\n\n"
                },
            }
        case ['1']:
            return {
                "msgtype": "markdown",
                "markdown": {
                    "title": "告警列表",
                    "text": markdown_alert_list()
                },
            }
        case ['1', user_name]:
            return {
                "msgtype": "markdown",
                "markdown": {
                    "title": "告警列表",
                    "text": markdown_alert_list(user_name)
                },
            }
        case ['2']:
            return {
                "msgtype": "markdown",
                "markdown": {
                    "title": "屏蔽告警列表",
                    "text": "1. 告警列表(1 用户名，可获取指定用户的告警列表)\n\n2. 屏蔽告警列表\n\n3. 用户列表\n\n"
                },
            }
        case ['3']:
            return {
                "msgtype": "markdown",
                "markdown": {
                    "title": "用户列表",
                    "text": markdown_user_list()
                },
            }
        case _:
            return {
                "msgtype": "text",
                "text": {
                    "title": "功能列表",
                    "content": "暂时不能理解你的请求，请@我并输入'帮助'获取功能列表"
                }
            }
