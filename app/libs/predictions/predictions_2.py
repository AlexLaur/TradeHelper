import pandas as pd
import numpy as np
import yfinance as yf
from pprint import pprint
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from keras.callbacks import ModelCheckpoint

# https://www.youtube.com/watch?v=PuZy9q-aKLw&ab_channel=NeuralNine
class MakePrediction(object):
    def __init__(self, data):

        # pprint(data) # 4105 days
        prices = data['Close'].values

        print(data.shape)

        prediction_days = 60

        # Prepare Data

        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(prices.reshape(-1, 1))

        # Split 80-20
        train_size = int(len(scaled_data) * 0.80)
        test_size = int(len(scaled_data) - train_size)
        train = prices[0:train_size]
        test = scaled_data[train_size:len(scaled_data)]

        # Method for create features from the time series data
        def create_features(data, window_size):
            x, y = [], []
            for i in range(len(data) - window_size - 1):
                window = data[i:(i + window_size), 0]
                x.append(window)
                y.append(data[i + window_size, 0])
            return np.array(x), np.array(y)

        # Roughly one month of trading assuming 5 trading days per week
        window_size = 20
        x_train, y_train = create_features(train, window_size)

        x_test, y_test = create_features(test, window_size)

        # Reshape to the format of [samples, time steps, features]
        x_train = np.reshape(x_train, (x_train.shape[0], 1, x_train.shape[1]))

        x_test = np.reshape(x_test, (x_test.shape[0], 1, x_test.shape[1]))

        scaled_data_shape = scaled_data.shape
        train_shape = train.shape
        test_shape = test.shape

        # Make sure that the number of rows in the dataset = train rows + test rows
        def is_leak(T_shape, train_shape, test_shape):
            return not (T_shape[0] == (train_shape[0] + test_shape[0]))

        print(is_leak(scaled_data_shape, train_shape, test_shape))

        # Building model
        model = Sequential()

        model.add(LSTM(units=50, activation='relu',  # return_sequences = True,
                       input_shape=(x_train.shape[1], window_size)))
        model.add(Dropout(0.2))

        # Output layer
        model.add(Dense(1))
        model.compile(loss='mean_squared_error', optimizer='adam')
        model.fit(x_train, y_train, epochs=25, batch_size=32)

        predicted_prices = model.predict(x_test)
        predicted_prices = scaler.inverse_transform(predicted_prices)

        # Plot Predictions
        plt.plot(data['Close'].values, color='black', label='Price')
        plt.plot(predicted_prices, color='green', label="Predict")
        plt.xlabel('Time')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

if __name__ == '__main__':
    tick = "GLE.PA"
    ticker = yf.Ticker(tick)
    data = ticker.history(period="1y", interval="1d", start="2008-01-01")
    pre = MakePrediction(data=data)
