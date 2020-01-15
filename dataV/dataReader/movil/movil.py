import pandas as pd
from pandas import read_csv, DataFrame
from matplotlib import pyplot
from datetime import timedelta



for i in range(1,11):
    series = read_csv('data ('+str(i)+').csv', parse_dates=True, skiprows=9,
                      names=['t', 'sesion', 'time', 'lat', 'lon', 'F', 'PM1', 'PM10', 'PM2.5', 'RH'])
    series['time'] = pd.to_datetime(series['time'])
    series['time'] = series['time'] - timedelta(hours=0)
    series_f = series.dropna(subset=['PM2.5'])
    df=DataFrame({'Sesion':series_f['sesion'],'Timestamp':series_f['time'],'Latitud':series_f['lat'],'Longitud':series_f['lon'],'PM2.5':series_f['PM2.5']})
    df.to_csv('output '+str(i)+'.csv', index=None, header=True)
    print(df)


