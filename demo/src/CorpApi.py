# https://qyapi.weixin.qq.com/cgi-bin/gettoken?
from demo.src.AbstractApi import AbstractApi

CORP_API_TYPE = {
    "GET_ACCESS_TOKEN": ['/cgi-bin/gettoken', 'GET'],
}


class CorpApi(AbstractApi):
    def __init__(self, corpid, corp_secret):
        self.corpid = corpid
        self.corp_secret = corp_secret
        self.access_token = None

    # 获取access_token
    def getAccessToken(self):
        if self.access_token is None:
            self.refreshAccesstoken()
        return self.access_token

    def refreshAccesstoken(self):
        response = self.httpCall(
            CORP_API_TYPE['GET_ACCESS_TOKEN'],
            {
                'corpid': self.corpid,
                'corpsecret': self.corp_secret
            }
        )
        self.access_token = response.get('access_token')
