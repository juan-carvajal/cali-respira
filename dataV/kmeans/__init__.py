'''
Created on 19/11/2019

@author: juan0
'''
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
    val = 0
    for i in x:
        val += i[2]
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


def to_arrs(x):
    x1 = []
    y = []
    for i in x:
        x1.append(i[0])
        y.append(i[1])
    return x1, y


df = pd.read_csv('cleaned.csv')

# print(df)
tipo='OUTDOOR'
f1 = df['Longitud'] > -76.536
f2 = df['Modo'] == tipo
full=df.where(f1)
full=pd.DataFrame({'x': full['Longitud'], 'y': full['Latitud']})
full.dropna(inplace=True)
df.where(f1 & f2, inplace=True)
df = pd.DataFrame({'x': df['Longitud'], 'y': df['Latitud'], 'pm': df['PM2.5']})

df.dropna(inplace=True)
kmeans = KMeans(n_clusters=10)
x = pd.DataFrame({'x': df['x'], 'y': df['y']})
kmeans.fit(full)
centers = kmeans.cluster_centers_
arr = [[] for i in range(len(centers))]
for index, row in df.iterrows():
    k = kmeans.predict([[row['x'], row['y']]])
    arr[k[0]].append((row['x'], row['y'], row['pm']))
# print(arr)
g = GoogleVisibleMap(x=[-76.533, -76.525], y=[3.340, 3.375],
                     scale=2,  # scale is for more details
                     maptype='roadmap')

f,ax = plt.subplots(1, figsize=(12, 12))
ggl_img = g.get_vardata()


sm = Map(g.grid, factor=1, countries=False)
sm.set_rgb(ggl_img)
sm.visualize(ax=ax)
ax.set_title(tipo)


for i in range(len(arr)):
    if len(arr[i])>0:
        col = color(arr[i])
        x, y = to_arrs(arr[i])
        # x=[centers[i][0]]
        # y=[centers[i][1]]
        # print(x , y)
        x, y = sm.grid.transform(x, y)
        plt.scatter(x, y, c=col, s=1, alpha=0.8)
plt.tight_layout()
plt.show()

# y_kmeans = kmeans.predict(df)
# print(arr)
# # print(y_kmeans)
# plt.scatter(df['x'], df['y'], c=y_kmeans, s=5, cmap='viridis')
#
# # plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
# plt.show()
