import json

from alibabacloud_cms20190101 import models as cms_20190101_models
from flask import current_app

from web.cms.utils.cms_connect import AliyunClient


class AliyunCMS:
    def __init__(self, access_key_id, access_key_secret, metric, endpoint='metrics.cn-hangzhou.aliyuncs.com'):
        """创建连接"""
        self.cms_client = AliyunClient(access_key_id, access_key_secret, endpoint).create_client()
        self.metric = metric
        current_app.logger.info('cms client已经创建')

    def get_metrics(self):
        """获取监控数据"""
        requests = cms_20190101_models.DescribeMetricTopRequest()
        # 设定页大小为100
        requests.page_size = 100
        # 设定基础参数
        requests.namespace = 'acs_ecs_dashboard'
        requests.orderby = 'Average'
        requests.length = '1440'
        requests.metric_name = self.metric
        current_app.logger.info('请求阿里云cms api获取监控指标')
        try:
            response = self.cms_client.describe_metric_top(requests)
        except Exception as e:
            current_app.logger.error('请求阿里云失败')
            current_app.logger.error(e)
            return []
        current_app.logger.info('请求阿里云cms api获取数据成功')
        current_app.logger.info('cms api 数据: {0}'.format(response))
        try:
            return json.loads(response.body.to_map()['Datapoints'])
        except Exception as e:
            current_app.logger.error(e)
            current_app.logger.info(json.loads(response.body.to_map()['Message']))
            return []


if __name__ == '__main__':
    # 创建链接
    client = AliyunCMS('access_key_id', 'access_key_secret', 'diskusage_used')
    # 获取监控指标
    client.get_metrics()
