from flask import Blueprint, request, current_app

from web import siwa
from .models import AliyunAuthSchema
from .service import check_cms_all

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/check', methods=['post'])
@siwa.doc(form=AliyunAuthSchema, tags=["cms"])
def check_cms(form: AliyunAuthSchema):
    headers = request.headers
    current_app.logger.debug('请求的headers: {}'.format(headers))
    auth =form.dict()
    check_info = check_cms_all(auth)
    return check_info
