from src.lib.DownloadData import DownloadData
import pandas as pd


class CDLData(DownloadData):
    def get_data(self):
        df = self.pro.daily(trade_date='20180810')
        daily_limit_df = df[df['pct_chg'] >= 9.9]
        daily_limit_company_info = pd.DataFrame(
            columns=['ts_code', 'main_business', 'reg_capital', 'setup_date', 'province'])
        szse_exhange_company_info_df = self.pro.stock_company(
            exchange='SZSE',
            fields='ts_code,main_business,reg_capital,setup_date,province')
        sse_exhange_company_info_df = self.pro.stock_company(
            exchange='SSE',
            fields='ts_code,main_business,reg_capital,setup_date,province')
        for ts_code in daily_limit_df['ts_code'].tolist():
            szse_company_info_df = szse_exhange_company_info_df[szse_exhange_company_info_df['ts_code'] == ts_code]
            sse_company_info_df = sse_exhange_company_info_df[sse_exhange_company_info_df['ts_code'] == ts_code]
            if szse_company_info_df.shape[0] > 0:
                daily_limit_company_info = pd.concat([daily_limit_company_info,szse_company_info_df], ignore_index=True)
            else:
                daily_limit_company_info = pd.concat([daily_limit_company_info,sse_company_info_df], ignore_index=True)

        print(daily_limit_company_info)


if __name__ == '__main__':
    CDL = CDLData()
    CDL.get_data()
