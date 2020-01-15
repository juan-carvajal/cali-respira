import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

sesiones = ['KOM', 'DMR']
export_data = []
for sesion in sesiones:
    full = pd.read_csv(sesion + '_reg' + ".csv", parse_dates=True)
    full = pd.read_csv("../../datos/fijo/" + sesion + ".csv", parse_dates=True)

    full['Timestamp'] = pd.to_datetime(full["Timestamp"])
    full['Dia'] = full['Timestamp'].dt.weekday

    full['Hora'] = full['Timestamp'].dt.hour

    full['Minuto'] = full['Timestamp'].dt.minute

    full['Hora_Minuto'] = full['Hora'] + (full['Minuto'] / 60)
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    for dia in range(7):
        data = full.where(full['Dia'] == dia)
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
                      loss='mae')

        model.fit(X, Y, epochs=2000, verbose=False)

        predicted_ml = model.predict(X).flatten()
        error_ml = np.average(np.absolute(Y - predicted_ml))

        regressor = LinearRegression()
        regressor.fit(X, Y)
        R2 = regressor.score(X, Y)

        predicted_reg = regressor.predict(X)
        error_reg = np.average(np.absolute(Y - predicted_reg))
        export_data.append([sesion, dias[dia], R2, error_reg, error_ml]+regressor.coef_.tolist()+[regressor.intercept_])
        f, ax = plt.subplots(1, 2, figsize=(12, 6))
        min_val_ml = min(min(Y), min(predicted_ml))
        max_val_ml = max(max(Y), max(predicted_ml))

        min_val_reg = min(min(Y), min(predicted_reg))
        max_val_reg = max(max(Y), max(predicted_reg))

        ax[0].set_title('Regresión Lineal')
        ax[0].set_xlabel('$y$')
        ax[0].set_ylabel('$\u0176$')
        ax[0].scatter(Y, predicted_reg, s=0.1, marker=',')
        ax[0].plot([min_val_reg, max_val_reg], [min_val_reg, max_val_reg], c='red')

        ax[1].set_title('Regresión Numérica con ML')
        ax[1].set_xlabel('$y$')
        ax[1].set_ylabel('$\u0176$')
        ax[1].scatter(Y, predicted_ml, s=0.1, marker=',')
        ax[1].plot([min_val_ml, max_val_ml], [min_val_ml, max_val_ml], c='red')
        plt.suptitle('F-' + sesion + ' : Comparación Regresiones : ' + dias[dia])
        plt.savefig('ml_vs_reg_' + sesion + '_' + dias[dia] + '.png', dpi=300)
        plt.show()

pd.DataFrame(export_data, columns=['Sesion', 'Dia', 'R2', 'MAE_REG', 'MAE_ML','COEFICIENTE_TEMPERATURA','COEFICIENTE_HUMEDAD','COEFICIENTE_HORA_MINUTO','INTERCEPTO']).to_csv('reg_vs_ml_comparacion.csv')
