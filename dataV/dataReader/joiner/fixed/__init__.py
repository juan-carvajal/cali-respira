import pandas as pd
from pandas import read_csv, DataFrame
from matplotlib import pyplot
from datetime import timedelta
from pandas import Grouper
import seaborn as sns

dfs = []
for i in range(1, 3):
    series = read_csv('F-DMR-' + str(i) + '.csv', parse_dates=True, skiprows=9,
                      names=['t', 'sesion', 'time', 'lat', 'lon', 'F', 'PM1', 'PM10', 'PM2.5', 'RH'])
    series['time'] = pd.to_datetime(series['time'])
    series['time'] = series['time'] - timedelta(hours=1)
    series['weekday'] = series['time'].dt.dayofweek
    df = DataFrame({'Sesion': series['sesion'], 'Timestamp': series['time'], 'Latitud': series['lat'],
                    'Longitud': series['lon'], 'PM2.5': series['PM2.5'], 'Temperatura':series['F'],'Humedad':series['RH']})
    dfs.append(df)

df_dmr=pd.concat(dfs)
df_dmr.dropna(how='any', inplace=True)
df_dmr=df_dmr.sort_values(by=['Timestamp'])
df_dmr=df_dmr.reset_index(drop=True)
df_dmr.to_csv('DMR.csv', index=None, header=True)

dfs=[]
for i in range(1, 3):
    series = read_csv('F-KOM-' + str(i) + '.csv', parse_dates=True, skiprows=9,
                      names=['t', 'sesion', 'time', 'lat', 'lon', 'F', 'PM1', 'PM10', 'PM2.5', 'RH'])
    series['time'] = pd.to_datetime(series['time'])
    series['time'] = series['time'] - timedelta(hours=1)
    series['weekday'] = series['time'].dt.dayofweek
    df = DataFrame({'Sesion': series['sesion'], 'Timestamp': series['time'], 'Latitud': series['lat'],
                    'Longitud': series['lon'], 'PM2.5': series['PM2.5'], 'Temperatura':series['F'],'Humedad':series['RH']})
    dfs.append(df)

df_kom = pd.concat(dfs)
df_kom.dropna(how='any', inplace=True)
df_kom = df_kom.sort_values(by=['Timestamp'])
df_kom = df_kom.reset_index(drop=True)
df_kom.to_csv('KOM.csv', index=None, header=True)
