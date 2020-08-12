import requests


class ApiException(Exception):
    def __init__(self, errCode: int, errMsg: str):
        self.errCode = errCode
        self.errMsg = errMsg


class AbstractApi:
    def __init__(self):
        return

    # 给子类继承的方法，用来获取类似于审计等的access_token
    def getAccessToken(self):
        raise NotImplementedError

    def httpCall(self, urlType: list, args=None):

        shortUrl = urlType[0]
        method = urlType[1]
        response = {}

        # 所有操作之前,尝试验证token最少三次
        # for i in range(3):
        if method == 'GET':
            url = self._makeurl(shortUrl)
            url = self._appendArgs(url, args)

            # 完整的url
            whole_url = self._appendToken(url)

            # 利用requests库构造GET请求
            response = requests.get(whole_url).json()
            return response

        elif method == 'POST':
            pass
        else:
            raise ApiException(-1, '你传的参数不对哦')

    # 把access_token添加到GET请求url后面
    def _appendToken(self, url):

        if "ACCESS_TOKEN" in url:

            whole_url = url.replace("ACCESS_TOKEN", self.getAccessToken())

            return whole_url
        else:
            return url
    # 生成完整的url路径
    @staticmethod
    def _makeurl(shortUrl):
        base_url = 'https://qyapi.weixin.qq.com'
        if shortUrl[0] == '/':
            return base_url + shortUrl
        else:
            return base_url + '/' + shortUrl

    # 解析GET请求url,把参数都加到url后边
    @staticmethod
    def _appendArgs(url, args):
        if args is None:
            return url

        for key, value in args.items():
            if '?' not in url:
                url = url + ('?' + key + '=' + value)
            else:
                url = url + ('&' + key + '=' + value)
        return url
