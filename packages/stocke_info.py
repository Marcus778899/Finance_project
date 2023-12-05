from FinMind.data import DataLoader
from FinMind_token import token

api = DataLoader()
api.login_by_token(api_token=token)

df = api.taiwan_stock_info()
df.to_csv('./dataset/stock_info.csv')