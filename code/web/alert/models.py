from typing import List

from pydantic import BaseModel

from web import db
from web.common.schema import PageSchema


class AliyunAlert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastTime = db.Column(db.String(255))
    rawMetricName = db.Column(db.String(255))
    expression = db.Column(db.String(255))
    metricName = db.Column(db.String(255))
    instanceName = db.Column(db.String(255))
    signature = db.Column(db.String(255))
    transId = db.Column(db.String(255))
    groupId = db.Column(db.String(255))
    regionName = db.Column(db.String(255))
    productGroupName = db.Column(db.String(255))
    metricProject = db.Column(db.String(255))
    userId = db.Column(db.String(255))
    curValue = db.Column(db.String(255))
    unit = db.Column(db.String(255))
    alertName = db.Column(db.String(255))
    regionId = db.Column(db.String(255))
    namespace = db.Column(db.String(255))
    triggerLevel = db.Column(db.String(255))
    alertState = db.Column(db.String(255))
    preTriggerLevel = db.Column(db.String(255))
    ruleId = db.Column(db.String(255))
    dimensions = db.Column(db.String(255))
    timestamp = db.Column(db.String(255))

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
            del dict["id"]
            return dict


class AliyunAlertSchema(BaseModel):
    lastTime: str
    rawMetricName: str
    expression: str
    metricName: str
    instanceName: str
    signature: str
    transId: str
    groupId: str
    regionName: str
    productGroupName: str
    metricProject: str
    userId: str
    curValue: str
    unit: str
    alertName: str
    regionId: str
    namespace: str
    triggerLevel: str
    alertState: str
    preTriggerLevel: str
    ruleId: str
    dimensions: str
    timestamp: str

    class Config:
        orm_mode = True


class AlertsSchema(PageSchema):
    alerts: List[AliyunAlertSchema]

    class Config:
        orm_mode = False
