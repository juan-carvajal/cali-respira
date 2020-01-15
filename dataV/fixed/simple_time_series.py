import pandas as pd
from pandas import read_csv
from matplotlib import pyplot
from datetime import timedelta

"""
ESTE ES EL SCRIPT PARA CALCULAR LA VISUALIZACION DE LAS SESIONES FIJAS,
PARECE HABER UN ERROR EN EL CALCULO DE HORAS DE LAS FIJAS (HAY UNA HORA
DE MAS). SE ESTAN SALTANDO 9 LINEAS DEL CSV.



"""


series = read_csv('data (1).csv',parse_dates=True ,skiprows=9, names=['t','sesion','time','lat','lon','F','PM1','PM10','PM2.5','RH'])
series['time'] =pd.to_datetime(series['time'])
series['time']=series['time']-timedelta(hours=1)
print(series)
plot=series.plot(x='time',y='PM2.5' , title="PM 1.5 vs time")
plot.get_figure().savefig('output.png')
# with PdfPages('data.pdf') as pdf:
#     fig=series.plot(x='time',y='PM2.5').getFigure()
#     pdf.savefig(fig)

#pyplot.show()