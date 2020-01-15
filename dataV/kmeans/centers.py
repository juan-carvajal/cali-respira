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


df.dropna(inplace=True)
kmeans = KMeans(n_clusters=10)
x = pd.DataFrame({'x': df['Longitud'], 'y': df['Latitud']})
kmeans.fit(x)
centers = kmeans.cluster_centers_
# for index, row in df.iterrows():
#     if index%1000==0:
#         print(index)
#     row['Indice_Centro'] = kmeans.predict([[row['Longitud'], row['Latitud']]])
#     row['Latitud_Centro'] = centers[row['Indice_Centro']][0][1]
#     row['Longitud_Centro'] = centers[row['Indice_Centro']][0][0]
arr=list(zip(df['Longitud'], df['Latitud']))
# arr=arr.reshape(2,-1)


df['Indice_Centro']=kmeans.predict(arr)
# print(centers[df['Indice_Centro'].to_numpy()][:,0])
# print(centers[df['Indice_Centro'].to_numpy()][:,1])
df['Latitud_Centro']=centers[df['Indice_Centro'].to_numpy()][:,1]
df['Longitud_Centro']=centers[df['Indice_Centro'].to_numpy()][:,0]

df.to_csv('centers.csv', index=None, header=True)
