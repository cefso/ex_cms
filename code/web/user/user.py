from flask import Blueprint, request, current_app

from web import siwa, db
from web.common.schema import QuerySchema
from .models import UserSchema, User, UsersSchema
from .service import get_user_list

bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/add', methods=['POST'])
@siwa.doc(form=UserSchema, tags=["user"])
def add_user(form: UserSchema):
    headers = request.headers
    current_app.logger.debug('请求的headers: {}'.format(headers))
    user_id = form.userId
    user_name = form.userName
    # 判断用户是否存在，存在则报错，不存在则新增
    if db.session.execute(db.select(User).filter_by(userId=user_id)).scalar() is None:
        db.session.add(User(**form.dict()))
        db.session.commit()
        return {"message": "添加用户: {}({})".format(user_id, user_name)}
    else:
        return {"message": "用户已存在: {}({})".format(user_id, user_name)}


@bp.route('/list', methods=['GET'])
@siwa.doc(query=QuerySchema, resp=UsersSchema, tags=["user"])
def list_user(query: QuerySchema):
    user_pagination, user_list = get_user_list(page=query.page, page_size=query.size)
    return {'page': user_pagination.page, 'page_size': user_pagination.per_page, 'total': user_pagination.total,
            'users': user_list}
