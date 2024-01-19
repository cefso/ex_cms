from flask import Blueprint, request, current_app

from web import siwa

bp = Blueprint('health', __name__, url_prefix='/health')


@bp.route('/check', methods=['get'])
@siwa.doc(tags=["health"])
def health_check():
    headers = request.headers
    body = request.values.to_dict()
    current_app.logger.info('请求的headers: {}'.format(headers))
    current_app.logger.info('接收到的内容: {}'.format(body))
    return {"message": "success"}
