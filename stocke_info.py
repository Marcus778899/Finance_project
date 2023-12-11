from FinMind.data import DataLoader
from secret import secret

api = DataLoader()
api.login_by_token(api_token=secret.token)

df = api.taiwan_stock_info()
df.to_csv('./dataset/stock_info.csv')