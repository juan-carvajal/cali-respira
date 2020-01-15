import pandas as pd
from pandas import read_csv
from matplotlib import pyplot
from datetime import timedelta

"""
ESTE ES EL SCRIPT PARA CALCULAR LA VISUALIZACION DE LAS SESIONES MOVILES,
AQUI LA HORA SI SE ESTA REGISTRANDO ERRORES, PERO SE HAN DETECTADO ERRORES
INICIALES. SE SALTAN LINEAS DEPENDENDO DE LA DETECCION DE ERRORES,
EL ARCHIVO DE DRM TIENE UN ERROR EN LA PRIMERA LINEAM POR ESO SE 
SALTAN 10 EN LUGAR DE 9 LINEAS.



"""
#series = read_csv('m-i-am-07oct19-cla_102155__20191007-17721-ksgwiw.csv',parse_dates=True ,skiprows=9, names=['t','sesion','time','lat','lon','F','PM1','PM10','PM2.5','RH'])
series = read_csv('m-o-am-07oct19-dmr_102171__20191007-17721-4ry34x.csv',parse_dates=True ,skiprows=10, names=['t','sesion','time','lat','lon','F','PM1','PM10','PM2.5','RH'])
series['time'] =pd.to_datetime(series['time'])
series['time']=series['time']-timedelta(hours=0)
series_f=series.dropna(subset=['PM2.5'])
print(series_f)
plot=series_f.plot(x='time',y='PM2.5' , title="PM 1.5 vs time")
plot.get_figure().savefig('output.png')
# with PdfPages('data.pdf') as pdf:
#     fig=series.plot(x='time',y='PM2.5').getFigure()
#     pdf.savefig(fig)

pyplot.show()