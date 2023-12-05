import pandas as pd

def all_stock_number():
    data = pd.read_csv('./dataset/stock_info.csv')

    config_map = data['stock_id'].tolist()

    return config_map
