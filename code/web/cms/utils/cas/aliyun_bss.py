import json

from alibabacloud_tea_util import models as util_models
from flask import current_app

from web.cms.utils.aliyun_connect import AliyunClient


class AliyunBSS:
    def __init__(self, access_key_id, access_key_secret, endpoint='business.aliyuncs.com'):
        """创建连接"""
        self.aliyun_client = AliyunClient(access_key_id, access_key_secret, endpoint).create_client()
        # self.metric = metric
        current_app.logger.info('cas client已经创建')

    def get_aliyun_balance(self):
        """获取账户余额数据"""
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            response = self.aliyun_client.query_account_balance_with_options(runtime)
        except Exception as e:
            current_app.logger.error('请求阿里云失败')
            current_app.logger.error(e)
            return {}
        current_app.logger.info('请求阿里云bss api获取数据成功')
        current_app.logger.info('bss api 数据: {0}'.format(response))
        try:
            return json.loads(response.body.to_map()['Data'])
        except Exception as e:
            current_app.logger.error(e)
            current_app.logger.info(json.loads(response.body.to_map()['Message']))
            return


if __name__ == '__main__':
    # 创建链接
    client = AliyunBSS('access_key_id', 'access_key_secret', 'diskusage_used')
    # 获取监控指标
    client.get_aliyun_balance()
