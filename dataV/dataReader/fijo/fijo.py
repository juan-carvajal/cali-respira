import pandas as pd
from pandas import read_csv, DataFrame
from matplotlib import pyplot
from datetime import timedelta
from pandas import Grouper
import seaborn as sns
"""
ESTE ES EL SCRIPT PARA CALCULAR LA VISUALIZACION DE LAS SESIONES FIJAS,
PARECE HABER UN ERROR EN EL CALCULO DE HORAS DE LAS FIJAS (HAY UNA HORA
DE MAS). SE ESTAN SALTANDO 9 LINEAS DEL CSV.



"""
for i in range(1,3):
    series = read_csv('data ('+str(i)+').csv', parse_dates=True, skiprows=9,
                      names=['t', 'sesion', 'time', 'lat', 'lon', 'F', 'PM1', 'PM10', 'PM2.5', 'RH'])
    series['time'] = pd.to_datetime(series['time'])
    series['time'] = series['time'] - timedelta(hours=1)
    series['weekday'] = series['time'].dt.dayofweek
    df = DataFrame({'Sesion': series['sesion'], 'Timestamp': series['time'], 'Latitud': series['lat'],
                    'Longitud': series['lon'], 'PM2.5': series['PM2.5']})

    df.to_csv('output '+str(i)+'.csv', index=None, header=True)