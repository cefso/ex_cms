import base64
import hashlib
import hmac

from flask import current_app

from web.user.service import get_user_list


# 获取签名值
def get_sign(timestamp):
    app_secret = current_app.config.get('ROBOT_APP_SECRET')
    app_secret_enc = app_secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, app_secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(app_secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = base64.b64encode(hmac_code).decode('utf-8')
    return sign


def markdown_user_list():
    user_pagination, user_list = get_user_list()
    mk_user_list = ''
    index = 1
    for user in user_list:
        mk_user = '{}{}({})\n\n'.format(index, user['userName'], user['userId'])
        mk_user_list = mk_user_list + mk_user
        index = index + 1
    mk_user_list = mk_user_list + '> page:{}  page_size:{}  total:{}'.format(user_pagination.page,
                                                                               user_pagination.per_page,
                                                                               user_pagination.total)
    return mk_user_list


def check_content(content):
    # 删除多余空格, 避免对后续判断造成影响
    content = content.strip()
    match content:
        case content if content in '功能列表':
            return {
                "msgtype": "markdown",
                "markdown": {
                    "title": "功能列表",
                    "text": "1. 告警列表\n\n2. 屏蔽告警列表\n\n3. 用户列表\n\n"
                },
            }
        case '1':
            return {
                "msgtype": "markdown",
                "markdown": {
                    "title": "告警列表",
                    "text": "1. 告警列表\n\n2. 屏蔽告警列表\n\n3. 用户列表\n\n"
                },
            }
        case '2':
            return {
                "msgtype": "markdown",
                "markdown": {
                    "title": "屏蔽告警列表",
                    "text": "1.告警列表\n\n2.屏蔽告警列表\n\n3.用户列表\n\n"
                },
            }
        case '3':
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
