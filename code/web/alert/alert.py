from flask import Blueprint, request, current_app

from web import siwa, db
from web.common.schema import QuerySchema
from .models import AliyunAlertSchema, AliyunAlert, AlertsSchema
from .service import get_alert_list

bp = Blueprint('alert', __name__, url_prefix='/alert')


@bp.route('/post', methods=['POST'])
@siwa.doc(form=AliyunAlertSchema, tags=["alert"])
def post_alert(form: AliyunAlertSchema):
    headers = request.headers
    data = AliyunAlert(**form.dict())
    current_app.logger.debug('请求的headers: {}'.format(headers))
    db.session.add(data)
    db.session.commit()
    current_app.logger.debug('接收到的内容: {}，插入到数据库'.format(data.__dict__))
    return {"message": "success"}

@bp.route('/slack', methods=['POST'])
def slack_post():
    print(request.headers)
    print(request.json)
    return {"message": "success"}



@bp.route('/list', methods=['GET'])
@siwa.doc(query=QuerySchema, resp=AlertsSchema, tags=["alert"])
def list_user(query: QuerySchema):
    user_list = get_alert_list(page=query.page, page_size=query.size)
    return user_list
