from web import db
from .models import AliyunAlert
from sqlalchemy.orm import aliased


# 获取告警列表orm
def get_alert_list(page=1, page_size=10):
    # 定义别名
    aliyun_alert_alias = aliased(AliyunAlert)
    # 定义子查询
    subquery = db.select(1).where(AliyunAlert.ruleId == aliyun_alert_alias.ruleId,
                                  AliyunAlert.timestamp < aliyun_alert_alias.timestamp).exists()
    # 执行主查询
    alert_pagination = db.session.execute(
        db.select(AliyunAlert).where(~subquery, AliyunAlert.alertState != 'OK')).scalars()
    # TODO: 需要对数据进行进一步处理
    print(alert_pagination.all())
    alert_list = []
    for alert in alert_pagination.items:
        alert_list.append(alert.to_json())
    print(len(alert_list))
    for alert in alert_list:
        print(alert)
    return {'page': alert_pagination.page, 'page_size': alert_pagination.per_page, 'total': alert_pagination.total,
            'alerts': alert_list}

    # # 定义子查询
    # subquery = session.query(1).select_from(AliyunAlert).filter(
    #     AliyunAlert.ruleId == AliyunAlert.ruleId,
    #     AliyunAlert.timestamp > AliyunAlert.timestamp).exists()
    #
    # # 执行主查询
    # result = session.query(AliyunAlert).filter(~subquery, AliyunAlert.alertState != 'OK').all()
    #
    # for row in result:
    #     print(f"Rule ID: {row.ruleId}, Timestamp: {row.timestamp}, Alert State: {row.alertState}")
