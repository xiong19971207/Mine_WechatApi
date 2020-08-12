from demo.src.CorpApi import CorpApi, CORP_API_TYPE
from demo.config.corp_config import TESTCONF

api = CorpApi(TESTCONF['CORPID'], TESTCONF['TEST_APP_CORP_SECRET'])

response = api.httpCall(
    CORP_API_TYPE['GET_ACCESS_TOKEN'],
    {
        'sp_no': 202008110001
    }
)
