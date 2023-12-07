import pymysql
import pandas as pd
from sqlalchemy import create_engine


conncetion = pymysql.connect(host='localhost',user='bigred',password='bigred',db='finace',charset='utf8')

engine = create_engine('mysql+pymysql://bigred:bigred@localhost/finace?charset=utf8',echo=False)

df = pd.read_csv('./dataset/0050.csv',dtype={'stock_id': str})
df.drop(['Unnamed: 0'],axis=1,inplace=True)
print(df)

conncetion.close()