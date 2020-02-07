import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.applications import VGG16
import numpy as np
from random import shuffle
 
vgg_conv = VGG16(weights='imagenet',
                  include_top=False,
                  input_shape=(224, 224, 3))
                  
train_dir = './trainSmall'
validation_dir = './validationSmall'

nTrain = 600
nVal = 150
datagen = ImageDataGenerator(rescale=1./255)
batch_size = 20
nImages = 984 + 246
 
train_features = np.zeros(shape=(nTrain, 7, 7, 512))
train_labels = np.zeros(shape=(nTrain,3))
 
train_generator = datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=shuffle)
    
i = 0
for inputs_batch, labels_batch in train_generator:
    features_batch = vgg_conv.predict(inputs_batch)
    train_features[i * batch_size : (i + 1) * batch_size] = features_batch
    train_labels[i * batch_size : (i + 1) * batch_size] = labels_batch
    i += 1
    if i * batch_size >= nImages:
        break
         
train_features = np.reshape(train_features, (nTrain, 7 * 7 * 512))