import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

sesion = 'KOM'
dia = 0
data = pd.read_csv("../../datos/fijo/" + sesion + ".csv", parse_dates=True)

data['Timestamp'] = pd.to_datetime(data["Timestamp"])
data['Dia'] = data['Timestamp'].dt.weekday
# data=data.where(data['Dia']==dia)
data['Hora'] = data['Timestamp'].dt.hour

data['Minuto'] = data['Timestamp'].dt.minute

data['Hora_Minuto'] = data['Hora'] + (data['Minuto'] / 60)
print(data)
print(data.isnull().any())

data.to_csv(sesion + '_reg.csv', index=False)
# data = data.where(data['Dia'] == 0)
data.dropna(how='any', inplace=True)
X = data[['Temperatura', 'Humedad', 'Hora_Minuto', 'Dia']]
y = data['PM2.5'].values

regressor = LinearRegression()
regressor.fit(X, y)
pred=regressor.predict(X)
mae=np.average(np.absolute(y-pred))
print('MAE: ',mae)
print(regressor.coef_)
coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
print(coeff_df)
print('Intercept:', regressor.intercept_)
print('R2:', regressor.score(X, y))

f, ax = plt.subplots(1, figsize=(5, 5))

X = X.values
predicted = regressor.predict(X)
min_val = min(min(y), min(predicted))
max_val = max(max(y), max(predicted))
ax.set_title('F-'+sesion+' : '+'Bondad de Ajuste')
ax.set_xlabel('$y$')
ax.set_ylabel('$\u0176$')
ax.scatter(y, predicted, s=0.1, marker=',')
ax.plot([min_val, max_val], [min_val, max_val], c='red')
plt.savefig('regression_fitness.png', dpi=300)
plt.show()
