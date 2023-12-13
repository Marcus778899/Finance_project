from FinMind.data import DataLoader
import pandas as pd
from secret import secret
from .download_finish import stock_finish

class scrapingStockInformation():
    def __init__(self):
        self.start_date = '2015-01-01'
        self.end_date = '2023-11-30'
        self.api = DataLoader()
        self.stock_info = pd.read_csv('./stock_info.csv')['stock_id'].tolist()
        self.stock_list = list(set(self.stock_info) - set(stock_finish()))
        self.token = secret.token

    # price of stock
    def scraping_stock_price(self):
        self.api.login_by_token(api_token=self.token)
        download_list = []
        for number in self.stock_list:
            print(f'start download : {number}.csv')
            try:
                dataset = self.api.taiwan_stock_daily(number, self.start_date , self.end_date)
                download_list.append(number)
            except Exception as e:
                    print(f"Error scraping data for stock {number} : {e}")
                    break
            dataset.to_csv(f'./dataset/stock_price/{number}.csv',index=False)
            print(f'{number} stock scraping done')
            print('='* 25)
        return download_list

    # some indicator need to add into data(not finish)
    def scraping_stock_value_indicator(self):
        self.api.login_by_token(api_token=self.token)
        download_list = []
        for number in self.stock_list:
            print(f'start download : {number}.csv')
            try:
                 dataset = self.api.taiwan_stock_per_pbr(number, self.start_date , self.end_date)
                 download_list.append(number)
            except Exception as e:
                 print(f"Error scraping data for stock {number} : {e}")
                 break 
            dataset.to_csv(f'./dataset/stock_value/{number}.csv',index=False)
            print(f'{number} stock scraping done')
            print('='* 25)
        return download_list  
