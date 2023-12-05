from FinMind.data import DataLoader
import pandas as pd
from .FinMind_token import token

class scrapingStockInformation():
    def __init__(self):
        self.start_date = '2015-01-01'
        self.end_date = '2023-11-30'
        self.api = DataLoader()
    
    def scraping(self,number):
        self.api.login_by_token(api_token=token)
        for number in number:
            try:
                dataset = self.api.taiwan_stock_daily(number, self.start_date , self.end_date)
            except Exception as e:
                    print(f"Error scraping data for stock {number} : {e}")
                    continue
            dataset.to_csv(f'./dataset/{number}.csv')
            print(f'{number} stock scraping done')

