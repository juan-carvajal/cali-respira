from sklearn.cluster import KMeans
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from cycler import cycler
import numpy as np
from salem import get_demo_file, DataLevels, GoogleVisibleMap, Map
import geopy.distance


def color(x):
    val = 0
    for i in x:
        val += i
    val /= float(len(x))
    #print(val)
    if val <= 12:
        return 'green'
    elif val > 12 and val <= 35:
        return 'yellow'
    elif val > 35 and val < 55:
        return 'orange'
    else:
        return 'red'

centers = pd.read_csv('../../datos/movil/centers.csv')

indexes = []
lats = []
longs = []
new_centers = []
dic = {4: 0, 9: 1, 1: 2, 6: 3, 2: 4, 5: 5, 7: 6, 0: 7, 8: 8, 3: 9}
# Indice_Centro,Latitud_Centro,Longitud_Centro
for index, row in centers.iterrows():
    center = row['Indice_Centro']
    new_centers.append(dic[center])

centers['Indice_Corregido'] = new_centers
centers.to_csv('centers_corregidos.csv', index=False)
for index, row in centers.iterrows():

    if not (row['Indice_Corregido'] in indexes):
        indexes.append(row['Indice_Corregido'])
        lats.append(row['Latitud_Centro'])
        longs.append((row['Longitud_Centro']))

new_df = pd.DataFrame({'Indice': indexes, 'Latitud': lats, 'Longitud': longs})
new_df['Ubicacion'] = new_df.agg('https://www.google.com/maps/search/?api=1&query={0[Latitud]},{0[Longitud]}'.format,
                                 axis=1)
new_df.sort_values(by=['Indice'], inplace=True)
new_df.to_csv('Indices.csv', index=False)

g = GoogleVisibleMap(x=[-76.533, -76.525], y=[3.340, 3.375],
                     scale=2,  # scale is for more details
                     maptype='roadmap')

f, ax = plt.subplots(1, figsize=(12, 12))
ggl_img = g.get_vardata()

sm = Map(g.grid, factor=1, countries=False)
sm.set_rgb(ggl_img)
sm.visualize(ax=ax)
n = new_df['Indice'].to_numpy()
x = new_df['Longitud'].to_numpy()
y = new_df['Latitud'].to_numpy()

tipo='OUTDOOR'

groups = centers.where(centers['Modo']==tipo).groupby('Indice_Corregido')
for name,group in groups:
    lat, long = group['Latitud'], group['Longitud']
    long, lat = sm.grid.transform(long, lat)
    ax.scatter(long, lat, s=0.1, c=color(group['PM2.5'].values), marker=',', alpha=1)

# ax.scatter(x, y, s=200,c='white',edgecolors='black', alpha=1)

x, y = sm.grid.transform(x, y)
for i, txt in enumerate(n):
    bbox_props = dict(boxstyle="circle,pad=0.3", fc="cyan", ec="b", lw=0.5)
    ax.text(x[i], y[i], txt, ha="center", va="center",
            size=8,
            bbox=bbox_props)
    # ax.annotate(txt, (x[i], y[i])  ,textcoords=(0,0))
ax.set_title('Concentraciones Promedio Por Centro Para Medición '+tipo)
plt.figtext(0.99, 0.01, '*Colores basados en los graficos propuestos por la plataforma Aircasting.org', horizontalalignment='right')
plt.savefig('centros_'+tipo+'.png', dpi=300)
plt.show()
