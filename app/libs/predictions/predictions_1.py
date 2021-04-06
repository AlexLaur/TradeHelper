import pandas as pd
import numpy as np
import yfinance as yf
from pprint import pprint
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

# https://www.youtube.com/watch?v=PuZY9q-aKLw&ab_channel=NeuralNine
class MakePrediction(object):
    def __init__(self, data):

        # pprint(data) # 4105 days

        prediction_days = 60
        _end = 3009

        # Prepare Data
        test_data = data['Close'].iloc[:_end].values
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_data = scaler.fit_transform(test_data.reshape(-1, 1))

        x_train = []
        y_train = []

        for x in range(prediction_days, len(scaled_data)):
            x_train.append(scaled_data[x - prediction_days:x, 0])
            y_train.append(scaled_data[x, 0])

        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

        # Build the Model
        model = Sequential()

        model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50, return_sequences=True))
        model.add(Dropout(0.2))
        model.add(LSTM(units=50))
        model.add(Dropout(0.2))
        model.add(Dense(units=1)) # Prediction of the next price Closing

        model.compile(optimizer="adam", loss='mean_squared_error')
        model.fit(x_train, y_train, epochs=25, batch_size=32)

        """ Test Model Accurency on Existing Data """

        # Load Test Data
        test_data = data['Close'].iloc[_end:]

        total_dataset = pd.concat((test_data, test_data), axis=0)

        model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
        model_inputs = model_inputs.reshape(-1, 1)
        model_inputs = scaler.transform(model_inputs)

        # Make Predictions on Test Data

        x_test = []

        for x in range(prediction_days, len(model_inputs)):
            x_test.append(model_inputs[x-prediction_days:x, 0])

        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

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
