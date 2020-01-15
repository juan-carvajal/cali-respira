import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns
from cycler import cycler
import numpy as np
from salem import get_demo_file, DataLevels, GoogleVisibleMap, Map
import geopy.distance

def get_dist(coords_1 , coords_2):
    return geopy.distance.distance(coords_1, coords_2).meters

dists=[
    (-76.5297163,3.3665631),
    (-76.5307019,3.3656924),
    (-76.5314718,3.3646900),
    (-76.5319956,3.3638394),
    (-76.5316622,3.3621781),
    (-76.5311999,3.3611796),
    (-76.5308636,3.3599338),
    (-76.5306335,3.3585191),
    (-76.5304758,3.3577502),
    (-76.5303957,3.3561101),
    (-76.5302998,3.3543178),
    (-76.5302220,3.3531897),
    (-76.5302369,3.3515283),
    (-76.5303363,3.3502667),
    (-76.5305351,3.3485951),
    (-76.5306779,3.3475220),
    (-76.5308545,3.3456382),
    (-76.5307738,3.3446934),
    (-76.530618,3.3430422)
]
df = pd.read_csv('movil.csv')


for index, row in df.iterrows():
    if index%1000 ==0:
        print(index)
    mind=None
    for i in dists:
        if mind:
            d=get_dist((row['Latitud'],row['Longitud']),(i[1],i[0]))
            if d<mind:
                mind=d
        else:
            mind=get_dist((row['Latitud'],row['Longitud']),(i[1],i[0]))
    if mind>100:
        df.drop(index, inplace=True)

print(df)
df.to_csv('cleaned.csv', index=None, header=True)

g = GoogleVisibleMap(x=[-76.533, -76.525], y=[3.340, 3.375],
                     scale=2,  # scale is for more details
                     maptype='roadmap')

f,ax = plt.subplots(1, figsize=(12, 12))
ggl_img = g.get_vardata()


sm = Map(g.grid, factor=1, countries=False)
sm.set_rgb(ggl_img)
sm.visualize(ax=ax)

x, y = sm.grid.transform(df['Longitud'], df['Latitud'])
plt.scatter(x, y, s=1, alpha=0.8)
plt.tight_layout()
plt.show()