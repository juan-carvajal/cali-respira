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

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# series = read_csv('DMR.csv', parse_dates=True, skiprows=1,
#                   names=['Sesion', 'Timestamp', 'Latitud', 'Longitud', 'PM2.5'])
sesion = 'DMR'
series = pd.read_csv("../../datos/fijo/" + sesion + ".csv", parse_dates=True)
series['Timestamp'] = pd.to_datetime(series['Timestamp'])
# series['time'] = series['time'] - timedelta(hours=1)
series['Weekday'] = series['Timestamp'].dt.dayofweek
series.dropna()
print(series)
groups = series.groupby(by=['Weekday'])
ax = sns.distplot(series['PM2.5'].dropna(), hist_kws=dict(edgecolor="k", linewidth=2))
pyplot.show()
for name, group in groups:
    day = DataFrame({'time': group['Timestamp'], 'PM2.5': group['PM2.5']})
    day['Hora'] = day['time'].dt.hour
    print(days[name] + ':', day)
    pyplot.grid(True)
    day['Hour']=day['Hora']
    ax = sns.boxplot(x="Hour", y="PM2.5", data=day, showmeans=True).set_title('F-'+sesion+' - Boxplot: ' + days[name])

    pyplot.savefig('./graficos/' + sesion+'_cajas_' + days[name] + '.png', dpi=300)
    pyplot.show()

    ax = sns.distplot(day['PM2.5'].dropna(), hist_kws=dict(edgecolor="k", linewidth=2)).set_title('F-'+sesion+' - Histogram: ' + days[name])
    pyplot.savefig('./graficos/' + sesion+'_histograma_' + days[name] + '.png', dpi=300)
    pyplot.show()



    # hour_group = day.groupby(Grouper(key='time', freq='H'))
    # print(day)
    # aux = DataFrame()
    # auxData=[]
    # for name2,group2 in hour_group:
    #     auxData.append((name2,group2['PM2.5']))
    #
    # auxData.sort(key=lambda data:data[2].size , reverse=True)
    #
    # for t in auxData:
    #     aux[t[0].hour] = pd.Series(t[2].values)
    #
    # aux = aux.reindex(columns=sorted(aux.columns))
    # print(aux)
    # plt=aux.boxplot()
    # plt.get_figure().savefig(days[name]+'.png')
    # pyplot.title(days[name])
    pyplot.show()
