from flask import Blueprint, request, current_app

from web import siwa
from .models import OutGoingSchema
from .service import get_sign

bp = Blueprint('outgoing', __name__, url_prefix='/outgoing')


@bp.route('outgoing', methods=['POST'])
# @siwa.doc(body=OutGoingSchema, tags=["outgoing"])
# def get_msg(body: OutGoingSchema):
def get_msg():
    headers = request.headers
    body = request.get_data()
    current_app.logger.debug('请求的headers: {}'.format(headers))
    current_app.logger.debug('请求的body: {}'.format(body))
    header_sign = request.headers.get('sign')
    check_sign = get_sign(request.headers.get('timestamp'))
    if header_sign != check_sign:
        return {"message": "sign check error"}
    else:
        return {"message": "success"}
