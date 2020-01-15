from keras.models import Sequential
from keras.layers import Dense, Activation
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

sesion = 'DMR'
data = pd.read_csv(sesion + '_reg' + ".csv", parse_dates=True)
data = data.where(data['Dia'] == 0)
data.dropna(how='any', inplace=True)
data['Hora_Minuto'] = data['Hora'] + (data['Minuto'] / 60)
X = data[['Temperatura', 'Humedad', 'Hora_Minuto']].values
Y = data['PM2.5'].values

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=3))
model.add(Dense(64, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam',
              loss='mae',
              metrics=['accuracy'])

model.fit(X, Y, epochs=1000, verbose=True)

score = model.evaluate(X, Y)
print(score)

predicted=model.predict(X).flatten()
errors = Y - predicted
# errors = []
# total = len(X)
# for i in range(len(X)):
#     if i % 500 == 0:
#         print(i / total)
#     pred = model.predict(np.array([X[i], ]))
#     error = Y[i] - pred[0][0]
#     errors.append(error)
# print(errors)
avg_error = np.average(np.absolute(errors))
print("Average Error: ", avg_error)
f, ax = plt.subplots(1, 2, figsize=(12, 5))
# f.suptitle('Vertically stacked subplots')
min_val=min(min(Y),min(predicted))
max_val=max(max(Y),max(predicted))
ax[0].set_title('Goodness of fit')
ax[0].set_xlabel('$y$')
ax[0].set_ylabel('$\u0176$')
ax[0].scatter(Y,predicted , s=0.1, marker=',')
ax[0].plot([min_val,max_val],[min_val,max_val] , c='red')
# plt.show()



# f, ax = plt.subplots(1, 2, figsize=(12, 5))


# sns.distplot(errors, hist_kws=dict(edgecolor="k", linewidth=2), ax=ax[0])
# ax[0].set(xlabel='Error', ylabel='Frec. Relativa')
# sns.distplot(np.absolute(errors), hist_kws=dict(edgecolor="k", linewidth=2), ax=ax[1])
# ax[1].set(xlabel='Error Absoluto', ylabel='Frec. Relativa')
# ax[0].set_title('Distribucion del error')
# ax[1].set_title('Distribucion del error absoluto')
#
# # plt.hist(errors, normed=True)
# plt.show()

data_sorted = np.sort(np.absolute(errors))

# calculate the proportional values of samples
p = 1. * np.arange(len(errors)) / (len(errors) - 1)

# ax[1].plot(p, data_sorted)

# sns.distplot(np.absolute(errors), hist_kws=dict(edgecolor="k", linewidth=2), ax=ax[1])
# ax[1].set_title('Distribucion del error absoluto')
# ax[1].set_xlabel('$PM2.5$')
# ax[1].set_ylabel('$Frecuencia Relativa$')

ax[1].plot(data_sorted, p)
ax[1].set_xlabel('$x$')
ax[1].set_ylabel('$p$')


ax[1].set_title('Funcion de Probabilidad Acumulada')
ax[0].grid(True)
ax[1].grid(True)
# ax[2].grid(True)
plt.savefig('fitness.png' , dpi=300)
plt.show()




