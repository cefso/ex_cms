from web import db
from .models import User


# 获取用户列表orm
def get_user_list(page=1, page_size=1):
    user_pagination = db.paginate(db.select(User), page=page, per_page=page_size, max_per_page=100, error_out=False)
    user_list = []
    for user in user_pagination.items:
        user_list.append(user.to_json())
    return user_list
