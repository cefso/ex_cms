from flask import Blueprint, request, current_app

from web import siwa
from .models import OutGoingSchema
from .service import get_sign, check_content

bp = Blueprint('outgoing', __name__, url_prefix='/outgoing')


@bp.route('outgoing', methods=['POST'])
@siwa.doc(body=OutGoingSchema, tags=["outgoing"])
def get_msg(body: OutGoingSchema):
    headers = request.headers
    current_app.logger.debug('请求的headers: {}'.format(headers))
    current_app.logger.debug('请求的body: {}'.format(body.dict()))
    # 校验签名
    header_sign = request.headers.get('sign')
    check_sign = get_sign(request.headers.get('timestamp'))
    if header_sign != check_sign:
        return {
            "msgtype": "text",
            "text": {
                "content": "签名错误，请联系开发者"
            }
        }
    else:
        content = body.text.content
        print(body.text.content)
        return check_content(content)
        # {
        #     "msgtype": "text",
        #     "text": {
        #         "content": "回调测试"
        #     }
        # }
