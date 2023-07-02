from flask import Blueprint, request, current_app

bp = Blueprint('alert', __name__, url_prefix='/alert')


@bp.route('/post', methods=['POST'])
def check():
    body = request.values.to_dict()
    current_app.logger.info('接收到的内容: {}'.format(body))
    return {"message": "success"}
