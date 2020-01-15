from sklearn.cluster import KMeans
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from cycler import cycler
import numpy as np
from salem import get_demo_file, DataLevels, GoogleVisibleMap, Map
import geopy.distance


# df = pd.DataFrame({
#     'x':  [random.randint(0,100) for i in range(500)],
#     'y': [random.randint(0,100) for i in range(500)]
# })

def color(x):
    if x <= 12:
        return 'green'
    elif x > 12 and x <= 35:
        return 'yellow'
    elif x > 35 and x < 55:
        return 'orange'
    else:
        return 'red'


def to_arrs(x):
    x1 = []
    y = []
    for i in x:
        x1.append(i[0])
        y.append(i[1])
    return x1, y


full = pd.read_csv('../../datos/movil/movil.csv')
cleaned = pd.read_csv('../../datos/movil/cleaned.csv')
centers = pd.read_csv('../../datos/movil/centers.csv')

g = GoogleVisibleMap(x=[-76.533, -76.525], y=[3.340, 3.375],
                     scale=2,  # scale is for more details
                     maptype='roadmap')

f, ax = plt.subplots(1,2, figsize=(5, 5))
ggl_img = g.get_vardata()

sm = Map(g.grid, factor=1, countries=False)
sm.set_rgb(ggl_img)
sm.visualize(ax=ax[0])

sm2 = Map(g.grid, factor=1, countries=False)
sm2.set_rgb(ggl_img)
sm2.visualize(ax=ax[1])
ax[0].set_title('Datos Crudos')
ax[1].set_title('Datos Limpios')

full_size=len(full.index)
cleaned_size=len(cleaned.index)

cols=[]
for index, row in full.iterrows():
    if index%1000==0:
        print('Full:',index/full_size)
    cols.append(color(row['PM2.5']))

x, y = sm.grid.transform(full['Longitud'], full['Latitud'])
ax[0].scatter(x, y, c=cols, s=0.1, alpha=0.3)

cols=[]

for index, row in cleaned.iterrows():
    if index%1000==0:
        print('Cleaned:',index/cleaned_size)
    cols.append(color(row['PM2.5']))

x, y = sm2.grid.transform(cleaned['Longitud'], cleaned['Latitud'])
ax[1].scatter(x, y, c=cols, s=0.1, alpha=0.3)

plt.tight_layout()
plt.savefig('graph.png', dpi=300)
plt.show()

