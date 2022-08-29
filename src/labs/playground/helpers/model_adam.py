from keras import optimizers
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import LSTM
from keras.optimizers import adam_v2, sgd_experimental
from keras.optimizers.adam_v2 import Adam
from keras.optimizers.sgd_experimental import SGD


class Model:
    def __init__(self, *args, **kwargs):
        self.temp_history = None
        self.regressor = None

    def set_model(self, name_opt: 'Adam', input_shape=int(), neuron_shape=int(), lr=0.001):
        neuron_1 = neuron_shape

        if name_opt=='Adam':
            opt=Adam(learning_rate=lr, beta_1=0.9, beta_2=0.999)
        elif name_opt=='SGD':
            opt=SGD(learning_rate=lr, momentum=0)
        else:
            print('OPtimizer not available.')

        regressor = Sequential()
        regressor.add(
            LSTM(units=neuron_1, input_shape=(input_shape, 1))
        )
        regressor.add(Dense(1))
        print(regressor.summary())
        regressor.compile(
            optimizer=opt, 
            loss='mean_squared_error', 
            metrics=['mean_squared_error']
        )
        self.regressor = regressor

    def fitting(self, input_set, target_set, val_input, val_target, val_epoch):
        self.temp_history = self.regressor.fit(
            input_set,
            target_set,
            batch_size=32,
            epochs=val_epoch,
            validation_data = (val_input, val_target)
        )
        print('fitting successfully.')

    def plot_history(self):
        return self.temp_history