from alibabacloud_cms20190101.client import Client
from alibabacloud_tea_openapi import models as open_api_models

from flask import current_app


# #构建一个阿里云客户端, 用于发起请求。
# #构建阿里云客户端时需要设置AccessKey ID和AccessKey Secret。
# client = AcsClient('<accessKeyId>', '<accessSecret>', 'cn-hangzhou')
# #构建请求。
# request = DescribeMetricListRequest()
# request.set_accept_format('json')
# #设置请求参数。
# request.set_MetricName("cpu_total")
# request.set_Namespace("acs_ecs_dashboard")
# request.set_StartTime("1628055731050")
# request.set_EndTime("1628062931050")
# request.set_Dimensions("{\"instanceId\":\"i-0xii2bvf42iqvxbp****\"}")
# request.set_Length("10")
# #发起请求，并得到响应。
# response = client.do_action_with_exception(request)
# # python2:  print(response)
# print(str(response, encoding='utf-8'))


class AliyunClient:
    def __init__(self, access_key_id, access_key_secret, endpoint):
        self.config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )

        # 访问的域名
        self.config.endpoint = endpoint

    def create_client(self):
        """初始化阿里云连接"""
        client = Client(self.config)
        current_app.logger.info('初始化阿里云连接')
        return client
