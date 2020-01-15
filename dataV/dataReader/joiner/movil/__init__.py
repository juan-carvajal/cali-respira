import pandas as pd
from pandas import read_csv, DataFrame
from datetime import timedelta
import numpy as np
import os

dfs=[]
for i in range(1,2):
    folder='./'+str(i)
    for file in os.listdir(folder):

        series = read_csv(folder+'/'+file, parse_dates=True, skiprows=9,
                          names=['t', 'sesion', 'time', 'lat', 'lon', 'F', 'PM1', 'PM10', 'PM2.5', 'RH'])
        #2019-10-08T08:09:52.073
        series['time'] = pd.to_datetime(series['time'])
        series['time'] = series['time'] - timedelta(hours=0)
        series_f = series.dropna(subset=['PM2.5'])
        df = DataFrame({'Sesion': series_f['sesion'], 'Tiempo': series_f['time'], 'Latitud': series_f['lat'],
                        'Longitud': series_f['lon'], 'PM2.5': series_f['PM2.5']})
        if file.startswith('I'):
            df['Modo']='INDOOR'
        else:
            df['Modo']='OUTDOOR'
        conditions=[(df['Tiempo'].dt.hour >=12) & (df['Tiempo'].dt.hour <24)]
        df['Hora']=np.select(conditions,['PM'],default='AM')
        df['DiaSemana']=df['Tiempo'].dt.weekday
        dfs.append(df)
full=pd.concat(dfs)
full.dropna(how='any', inplace=True)
full=full.sort_values(by=['Tiempo'])
full=full.reset_index(drop=True)
print(full)
full.to_csv('movil.csv', index=None, header=True)