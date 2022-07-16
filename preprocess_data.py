from asyncio.base_subprocess import BaseSubprocessTransport
import pandas as pd
import numpy as np
from datetime import datetime
# Doc file csv 2019-Dec
df = pd.read_csv('2019-Dec.csv')
# Upper title
df.columns = df.columns.str.upper()
# Xoa 2 cot category_code va user_session
del df['CATEGORY_CODE']
del df['USER_SESSION']
# Dem so gia tri null o tung cot
df.isnull().any()
# print(df.isnull().sum())
# Tach cot event_time
c =0
df['DATE'] = 0
df['TIME'] = 0

for i in df.EVENT_TIME:
    date_time = datetime.strptime(i, '%Y-%m-%d %H:%M:%S UTC')
    event_date = date_time.date()
    event_time = date_time.time()
    df['DATE'][c] = event_date
    df['TIME'][c] = event_time
    c+=1
    
df = df.drop('EVENT_TIME', 1)
# Xoa cot trung lap
df = df.drop_duplicates()
# Những data có ngày > 31 = 31
lastday = '2019-12-31'
for i in df.DATE:
    if i > lastday:
        i = lastday
    else:
        continue
print(df['DATE'].max())

df.to_csv('2019_Dec_Cleaned.csv')
