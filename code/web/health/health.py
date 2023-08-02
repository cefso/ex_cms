from flask import Blueprint, request, current_app

bp = Blueprint('health', __name__, url_prefix='/health')


@bp.route('/check', methods=['get'])
def check():
    headers = request.headers
    body = request.values.to_dict()
    current_app.logger.info('请求的headers: {}'.format(headers))
    current_app.logger.info('接收到的内容: {}'.format(body))
    return {"message": "success"}
