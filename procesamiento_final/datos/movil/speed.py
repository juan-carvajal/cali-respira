from sklearn.cluster import KMeans
import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from cycler import cycler
import numpy as np
from salem import get_demo_file, DataLevels, GoogleVisibleMap, Map
import geopy.distance


def get_dist(coords_1, coords_2):
    return geopy.distance.distance(coords_1, coords_2).meters


# lat lon

data = pd.read_csv('cleaned.csv')
data['Tiempo'] = pd.to_datetime(data['Tiempo'])
data.sort_values(by=['Tiempo'])

total = len(data.index)
vel_abs = [0] * total
curr_sess = None
for i in range(len(vel_abs)-1):
    if data.loc[[i]]['Sesion'].values[0] == data.loc[[i + 1]]['Sesion'].values[0]:
        t_n = data.loc[[i]]['Tiempo'].values[0]
        t_n1 = data.loc[[i + 1]]['Tiempo'].values[0]

        lat_n = data.loc[[i]]['Latitud'].values[0]
        lat_n1 = data.loc[[i + 1]]['Latitud'].values[0]

        lon_n = data.loc[[i]]['Longitud'].values[0]
        lon_n1 = data.loc[[i + 1]]['Longitud'].values[0]

        dist = get_dist((lat_n, lon_n), (lat_n1, lon_n1))

        delta_t = t_n1 - t_n

        delta_t = delta_t.item() / 1e9

        # print(dist , delta_t)
        if delta_t == 0:
            vel = 0
        else:
            vel = dist / delta_t

        # print(vel)
        vel_abs[i + 1] = vel

    else:
        vel_abs[i + 1] = 0

data['Velocidad']=vel_abs
data.to_csv('velocities.csv')

print(data)
