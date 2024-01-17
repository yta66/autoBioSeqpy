from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Flatten, Activation, Input, Reshape
from keras import optimizers

model = Sequential()
model.add(Dense(64, activation = 'relu', input_shape=(2048,)))
model.add(Dropout(0.2))
model.add(Dense(16, activation = 'relu'))
model.add(Dropout(0.2))
model.add(Dense(1))
model.add(Activation('sigmoid'))