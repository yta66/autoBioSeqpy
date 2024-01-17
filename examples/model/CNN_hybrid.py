from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from keras import optimizers



max_features = 32
embedding_size = 64
filters = 330
kernel_size = 16
hidden_dims = 128



print('Building model...')
model = Sequential()
model.add(Embedding(max_features,embedding_size,input_length=167))
model.add(Dropout(0.2))
model.add(Conv1D(filters,kernel_size = kernel_size,padding ='valid',activation = 'relu',strides = 1))
model.add(GlobalMaxPooling1D())
model.add(Dense(hidden_dims))
model.add(Dropout(0.2))
model.add(Activation('relu'))
model.add(Dense(1))
model.add(Activation('sigmoid'))