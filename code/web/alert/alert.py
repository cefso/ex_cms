from flask import Blueprint, request, current_app

from web import siwa, db
from .models import AliyunAlertSchema, AliyunAlert

bp = Blueprint('alert', __name__, url_prefix='/alert')


@bp.route('/post', methods=['POST'])
@siwa.doc(form=AliyunAlertSchema, tags=["alert"])
def get_alert(form: AliyunAlertSchema):
    headers = request.headers
    data = AliyunAlert(**form.dict())
    current_app.logger.debug('请求的headers: {}'.format(headers))
    db.session.add(data)
    db.session.commit()
    current_app.logger.debug('接收到的内容: {}，插入到数据库'.format(data.__dict__))
    return {"message": "success"}
