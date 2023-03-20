import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Fungsi untuk mengubah data menjadi format yang sesuai untuk LSTM
def create_dataset(data, look_back):
    X, y = [], []
    for i in range(len(data) - look_back - 1):
        X.append(data[i:(i + look_back), :])
        y.append(data[i + look_back, 0])
    return np.array(X), np.array(y)

# Muat dan praproses data
data = pd.read_csv("data_mata_uang.csv") # Ganti dengan file data Anda
data = data.drop(["Date"], axis=1)
data = data.values
scaler = MinMaxScaler()
data = scaler.fit_transform(data)

# Membagi data menjadi data latih dan data uji
train_size = int(len(data) * 0.8)
train, test = data[:train_size], data[train_size:]
look_back = 7
X_train, y_train = create_dataset(train, look_back)
X_test, y_test = create_dataset(test, look_back)

# Membuat model LSTM
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))

# Kompilasi dan melatih model
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=100, batch_size=32)

# Memprediksi data uji
y_pred = model.predict(X_test)
y_pred = scaler.inverse_transform(y_pred) # Mengembalikan ke skala asli
y_test = scaler.inverse_transform(y_test.reshape(-1, 1)) # Mengembalikan ke skala asli

# Menghitung nilai RMSE
rmse = np.sqrt(np.mean(np.power((y_test - y_pred), 2)))
print("RMSE: ", rmse)

# Menampilkan hasil prediksi
plt.figure(figsize=(14, 5))
plt.plot(y_test, label='Data Sebenarnya')
plt.plot(y_pred, label='Prediksi')
plt.legend()
plt.show()

