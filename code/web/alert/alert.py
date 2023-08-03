from flask import Blueprint, request, current_app
from web import siwa

bp = Blueprint('alert', __name__, url_prefix='/alert')


@bp.route('/post', methods=['POST'])
@siwa.doc(tags=["alert"])
def get_alert():
    headers = request.headers
    body = request.values.to_dict()
    current_app.logger.info('请求的headers: {}'.format(headers))
    current_app.logger.info('接收到的内容: {}'.format(body))
    return {"message": "success"}
