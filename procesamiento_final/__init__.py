from sklearn.cluster import KMeans
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from cycler import cycler
import numpy as np
from salem import get_demo_file, DataLevels, GoogleVisibleMap, Map
import geopy.distance

data = pd.read_csv('./datos/movil/movil.csv')

g = GoogleVisibleMap(x=[-76.533, -76.525], y=[3.340, 3.375],
                     scale=2,  # scale is for more details
                     maptype='roadmap')

f, ax = plt.subplots(1, figsize=(12, 12))
ggl_img = g.get_vardata()

sm = Map(g.grid, factor=1, countries=False)
sm.set_rgb(ggl_img)
sm.visualize(ax=ax)
ax.set_title('Datos')

x, y = sm.grid.transform(data['Longitud'], data['Latitud'])
plt.scatter(x, y,  s=1, alpha=1)
plt.show()


data = pd.read_csv('./datos/movil/cleaned.csv')

g = GoogleVisibleMap(x=[-76.533, -76.525], y=[3.340, 3.375],
                     scale=2,  # scale is for more details
                     maptype='roadmap')

f, ax = plt.subplots(1, figsize=(12, 12))
ggl_img = g.get_vardata()

sm = Map(g.grid, factor=1, countries=False)
sm.set_rgb(ggl_img)
sm.visualize(ax=ax)
ax.set_title('Datos Limpiados')

x, y = sm.grid.transform(data['Longitud'], data['Latitud'])
plt.scatter(x, y,  s=1, alpha=1)
plt.show()


data = pd.read_csv('./datos/movil/centers.csv')

g = GoogleVisibleMap(x=[-76.533, -76.525], y=[3.340, 3.375],
                     scale=2,  # scale is for more details
                     maptype='roadmap')

f, ax = plt.subplots(1, figsize=(12, 12))
ggl_img = g.get_vardata()

sm = Map(g.grid, factor=1, countries=False)
sm.set_rgb(ggl_img)
sm.visualize(ax=ax)
ax.set_title('Centros')

x, y = sm.grid.transform(data['Longitud_Centro'], data['Latitud_Centro'])
plt.scatter(x, y,  s=50, alpha=1)
plt.show()
