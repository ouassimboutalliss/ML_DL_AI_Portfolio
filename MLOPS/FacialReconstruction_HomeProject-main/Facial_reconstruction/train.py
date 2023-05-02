# Functional model autoencoder
import os
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix, accuracy_score

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Input, Dense, Dropout, Flatten, BatchNormalization,concatenate
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, Conv2DTranspose
from tensorflow.keras import backend as K
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing import image
from tensorflow.keras import regularizers

from tensorflow.keras.callbacks import EarlyStopping

# Model checkpoint
checkpoint_filepath = './Autoencoder_Undercomplete_Faces_bestModel'
mc = tf.keras.callbacks.ModelCheckpoint(filepath = checkpoint_filepath,save_weights_only=True, monitor='val_loss',mode='auto',save_best_only=True)
# Early stopping
es = EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience = 20)


#parameter
input_dim= X_train.shape[1]
epochs = 5
batchsize = 32
img_rows, img_cols = image_size, image_size
input_shape = (img_rows, img_cols,3) # 1 -> grijs waarden, 3 -> kleur

#model trainen

#Encoder
input_img = Input(shape=(image_size, image_size, 3))  ## 1 -> grijs waarden, 3 -> kleur

#dimensie gelijk aan image_size
#x = Flatten()(input_img)
x = Conv2D(100, (3, 3), activation='relu', padding='same')(input_img)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(100, (3, 3), activation='relu', padding='same')(x)
encoder = MaxPooling2D((2, 2), padding='same')(x)

# Decoder

x = Conv2D(100, (3, 3), activation='relu', padding='same')(encoder)
x = UpSampling2D((2, 2))(x)
x = Conv2D(100, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
decoder = Conv2D(3, (3, 3), activation='sigmoid', padding='same')(x)

# get hold of the current run
run = Run.get_context()

Convolution_autoencoder = Model(input_img, decoder)
Convolution_autoencoder.compile(optimizer='adam', loss='mean_squared_error')
#autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
Convolution_autoencoder.summary()

X_train_noise = np.reshape(X_train_noise, (len(X_train_noise), image_size, image_size, 3)) 
X_test_noise = np.reshape(X_test_noise, (len(X_test_noise), image_size, image_size, 3)) 
X_test = np.reshape(X_test, (len(X_test), image_size, image_size, 3)) 
X_train = np.reshape(X_train, (len(X_train), image_size, image_size, 3)) 



Convolution_autoencoder.fit(X_train_noise, X_train, epochs=epochs, batch_size=batchsize,shuffle=True )

#run.log('loss', np.float(loss))

os.makedirs('outputs', exist_ok=True)
# note file saved in the outputs folder is automatically uploaded into experiment record
Convolution_autoencoder.save("outputs/model.h5")