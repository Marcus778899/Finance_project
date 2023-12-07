from FinMind.data import DataLoader
import pandas as pd
from .secret import token
from .download_finish import stock_finish

class scrapingStockInformation():
    def __init__(self):
        self.start_date = '2015-01-01'
        self.end_date = '2023-11-30'
        self.api = DataLoader()
        self.stock_info = pd.read_csv('./stock_info.csv')['stock_id'].tolist()
        self.stock_list = list(set(self.stock_info) - set(stock_finish()))
   
    def scraping(self):
        self.api.login_by_token(api_token=token)
        download_list = []
        for number in self.stock_list:
            try:
                dataset = self.api.taiwan_stock_daily(number, self.start_date , self.end_date)
                download_list.append(number)
            except Exception as e:
                    print(f"Error scraping data for stock {number} : {e}")
                    break
            print(f'start download : {number}.csv')
            dataset.to_csv(f'./dataset/{number}.csv')
            print(f'{number} stock scraping done')
            print('='* 25)
        return download_list

