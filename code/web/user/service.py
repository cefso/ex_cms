from web import db
from .models import User


# 获取用户列表orm
def get_user_list(page=1, page_size=10):
    user_pagination = db.paginate(db.select(User), page=page, per_page=page_size, max_per_page=100, error_out=False)
    user_list = []
    for user in user_pagination.items:
        user_list.append(user.to_json())
    return user_pagination, user_list


# 获取用户id orm
def get_user_id(user_name):
    user_data = db.session.execute(db.select(User).where(User.userName == user_name)).scalar_one_or_none()
    if user_data is None:
        return None
    else:
        user_id = user_data.to_json()['userId']
        return user_id
