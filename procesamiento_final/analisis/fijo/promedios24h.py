import pandas as pd
from pandas import read_csv, DataFrame
from matplotlib import pyplot as plt
from datetime import timedelta
from pandas import Grouper
import seaborn as sns

sesion = 'DMR'
df = pd.read_csv("../../datos/fijo/" + sesion + ".csv", parse_dates=True)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.dropna(inplace=True)

grouped = pd.DataFrame({'Timestamp': df['Timestamp'], 'PM2.5': df['PM2.5']}).groupby(
    pd.Grouper(key='Timestamp', freq='24h')).mean()
grouped.dropna(inplace=True)
print(grouped)

grouped.to_csv(sesion+'_24h.csv')
