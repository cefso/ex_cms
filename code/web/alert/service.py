from code.web import db
from .models import AliyunAlert


# 获取用户列表orm
def get_alert_list(page=1, page_size=1):
    alert_pagination = db.paginate(db.select(AliyunAlert).order_by(AliyunAlert.timestamp), page=page,
                                   per_page=page_size, max_per_page=100, error_out=False)
    alert_list = []
    for user in alert_pagination.items:
        alert_list.append(user.to_json())
    return {'page': alert_pagination.page, 'page_size': alert_pagination.per_page, 'total': alert_pagination.total,
            'alerts': alert_list}
