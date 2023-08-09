# python 3.8
import base64
import hashlib
import hmac

from flask import current_app


# 获取签名值
def get_sign(timestamp):
    app_secret = current_app.config.get('ROBOT_APP_SECRET')
    app_secret_enc = app_secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, app_secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(app_secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = base64.b64encode(hmac_code).decode('utf-8')
    return sign


def check_content(content):
    # 删除多余空格, 避免对后续判断造成影响
    content = content.strip()
    if content in '功能列表' or content in '帮助':
        return {
            "msgtype": "markdown",
            "markdown": {
                "title": "功能列表",
                "text": "1. 告警列表 2. 屏蔽告警列表 3. 用户列表"
            },
        }
    else:
        return {
            "msgtype": "text",
            "text": {
                "content": "暂时不能理解你的请求，请@我并输入'帮助'获取功能列表"
            }
        }
