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

days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
series = read_csv('./data (1).csv', parse_dates=True, skiprows=9,
                  names=['t', 'sesion', 'time', 'lat', 'lon', 'F', 'PM1', 'PM10', 'PM2.5', 'RH'])
series['time'] = pd.to_datetime(series['time'])
series['time'] = series['time'] - timedelta(hours=1)
series['weekday'] = series['time'].dt.dayofweek
series.dropna()
print(series)
groups = series.groupby(by=['weekday'])
ax = sns.distplot(series['PM2.5'].dropna(), hist_kws=dict(edgecolor="k", linewidth=2))
pyplot.show()
for name, group in groups:

    day = DataFrame({'time': group['time'], 'PM2.5': group['PM2.5']})
    day['hour']=day['time'].dt.hour
    print(days[name] + ':', day)
    pyplot.grid(True)
    ax = sns.boxplot(x="hour", y="PM2.5", data=day,showmeans=True).set_title(days[name])

    pyplot.show()
    ax.get_figure().savefig(days[name] + '.png')
    ax = sns.distplot(day['PM2.5'].dropna(), hist_kws=dict(edgecolor="k", linewidth=2))
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



