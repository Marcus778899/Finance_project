from FinMind.data import DataLoader
import pandas as pd
from secret import secret
from .download_finish import stock_finish
import os

class scrapingStockInformation():
    def __init__(self):
        self.start_date = '2015-01-01'
        self.end_date = '2023-11-30'
        self.api = DataLoader()
        self.stock_info = pd.read_csv('./stock_info.csv')['stock_id'].tolist()
        self.token = secret.token

    # price of stock
    def scraping_stock_price(self,path_name:str):
        '''
        :param stock_price path_name output location,format is str
        '''
        folder_name = os.path.join(f'./dataset/{path_name}')
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        stock_list = list(set(self.stock_info) - set(stock_finish(path_name)))
        self.api.login_by_token(api_token=self.token)
        for number in stock_list:
            print(f'start download : {number}.csv')
            try:
                dataset = self.api.taiwan_stock_daily(number, self.start_date , self.end_date)
            except Exception as e:
                    print(f"Error scraping data for stock {number} : {e}")
                    break
            dataset.to_csv(f'./dataset/stock_price/{number}.csv',index=False)
            print(f'{number} stock scraping done')
            print('='* 25)
        print('DONE')

    # some indicator need to add into data(not finish)
    def scraping_stock_value_indicator(self,path_name:str):
        '''
        :param stock_value path_name output location,format is str
        '''
        folder_name = os.path.join(f'./dataset/{path_name}')
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        stock_list = list(set(self.stock_info) - set(stock_finish(path_name)))
        self.api.login_by_token(api_token=self.token)
        for number in stock_list:
            print(f'start download : {number}.csv')
            try:
                 dataset = self.api.taiwan_stock_per_pbr(number, self.start_date , self.end_date)
            except Exception as e:
                 print(f"Error scraping data for stock {number} : {e}")
                 break 
            dataset.to_csv(f'./dataset/stock_value/{number}.csv',index=False)
            print(f'{number} stock scraping done')
            print('='* 25)
        print('DONE')

    # financial statements abot stock
    def scraping_financial_statements(self,path_name:str) -> list:
        '''
        :param financial_statements path_name output location,format is str
        '''
        folder_name = os.path.join(f'./dataset/{path_name}')
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        stock_list = list(set(self.stock_info) - set(stock_finish(path_name)))
        self.api.login_by_token(api_token=self.token)
        for number in stock_list:
            print(f'start download : {number}.csv')
            try:
                 dataset = self.api.taiwan_stock_financial_statement(number, self.start_date , self.end_date)
            except Exception as e:
                 print(f"Error scraping data for stock {number} : {e}")
                 break 
            dataset.to_csv(f'./dataset/financial_statements/{number}.csv',index=False)
            print(f'{number} stock scraping done')
            print('='* 25)
        print('DONE')

    # BalanceSheet about stock
    def scraping_balance_sheet(self,path_name:str):
        '''
        :param balance_sheet path_name output location,format is str
        '''
        folder_name = os.path.join(f'./dataset/{path_name}')
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        stock_list = list(set(self.stock_info) - set(stock_finish(path_name)))
        self.api.login_by_token(api_token=self.token)
        for number in stock_list:
            print(f'start download : {number}.csv')
            try:
                 dataset = self.api.taiwan_stock_balance_sheet(number, self.start_date , self.end_date)
            except Exception as e:
                 print(f"Error scraping data for stock {number} : {e}")
                 break 
            dataset.to_csv(f'./dataset/balance_sheet/{number}.csv',index=False)
            print(f'{number} stock scraping done')
            print('='* 25)
        print('DONE')

    def scraping_cashflow_statement(self,path_name:str):
        '''
        :param cashflow_statement path_name output location,format is str
        '''
        folder_name = os.path.join(f'./dataset/{path_name}')
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        stock_list = list(set(self.stock_info) - set(stock_finish(path_name)))
        self.api.login_by_token(api_token=self.token)
        for number in stock_list:
            print(f'start download : {number}.csv')
            try:
                 dataset = self.api.taiwan_stock_cash_flows_statement(number, self.start_date , self.end_date)
            except Exception as e:
                 print(f"Error scraping data for stock {number} : {e}")
                 break 
            dataset.to_csv(f'./dataset/cashflow_statement/{number}.csv',index=False)
            print(f'{number} stock scraping done')