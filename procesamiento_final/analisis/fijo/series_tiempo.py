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


rolling_mean = df['PM2.5'].rolling(window=1440).mean()
fig, ax = plt.subplots(figsize=(12, 5))
plt.plot(df['Timestamp'], df['PM2.5'], label='PM2.5')
plt.plot(df['Timestamp'], rolling_mean, label='Media Movil (n=1440(1 dia))', color='orange')

plt.legend(loc='upper left')
ax.set_title('F-'+sesion+' : Series de Tiempo')
plt.savefig('./graficos/'+sesion+'_series.png', dpi=300)
plt.show()



# fig, ax = pyplot.subplots(figsize=(12, 5))
# rolling_mean = series['PM2.5'].rolling(window=20).mean()
# rolling_mean2 = series['PM2.5'].rolling(window=50).mean()
# sns.set(style="ticks", rc={"lines.linewidth": 0.5})
# sns.lineplot(x="Timestamp", y="PM2.5",
#              data=series, ax=ax)
#
# sns.lineplot(x="Timestamp", y="PM2.5",
#              data=series, ax=ax)
#
# sns.lineplot(x="Timestamp", y="PM2.5",
#              data=series, ax=ax)
# # pyplot.plot(series['Timestamp'], series['PM2.5'])
#
# # pyplot.scatter(series['Timestamp'],series['PM2.5'])

# pyplot.show()


