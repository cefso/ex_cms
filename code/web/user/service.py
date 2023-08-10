from web import db
from .models import User


# 获取用户列表orm
def get_user_list():
    users = db.session.execute(db.select(User)).scalars().all()
    user_list = []
    for user in users:
        user_list.append(user.to_json())
    return user_list
