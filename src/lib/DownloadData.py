from config.token import TOKEN_API
import tushare as ts


class DownloadData(object):
    def __init__(self):
        self.pro = ts.pro_api(TOKEN_API)

    @staticmethod
    def get_data(self):
        pass
