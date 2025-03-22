from data_transformation import train_df, train_target, test_df, test_target
from logger import logging
from keras import models
from keras import layers

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape= (train_df.shape[1],)))
    model.add(layers.Dense(64,activation='relu' ))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    logging.info("Model compiled")
    
    return model

# K-Fold Cross validation
def cross_validation(model, train_df,):
    