from data_transformation import train_df, train_targets, test_df, test_targets
from logger import logging
from keras import models
from keras import layers
import numpy as np

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape= (train_df.shape[1],)))
    model.add(layers.Dense(64,activation='relu' ))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    logging.info("Model compiled")
    
    return model

# K-Fold Cross validation
def cross_validation(train_df,train_targets):
    k = 4
    num_val_samples = len(train_df) // k
    num_epochs =100
    all_scores = []
    for i in range(k):
        print("'processing fold ",i)
        val_data = train_df[i *num_val_samples: (i+1)* num_val_samples]
        val_targets = train_targets[i *num_val_samples: (i+1)* num_val_samples]
        partial_train_data = np.concatenate(
            [train_df[:i*num_val_samples],
             train_df[(i+1) * num_val_samples:]], axis=0
        )
        partial_train_targets = np.concatenate(
            [train_targets[: i * num_val_samples],
             train_targets[(i + 1)* num_val_samples:]],
             axis=0
        )
        model = build_model()
        model.fit(partial_train_data, partial_train_targets,
                   epochs=num_epochs, batch_size=1, verbose=0)
        val_mse, val_mae = model.evaluate(val_data, val_targets, verbose=0)
        all_scores.append(val_mae)
    return all_scores

def final_model():
    model= build_model()
    model.fit(train_df, train_targets,
            epochs=80, batch_size=16, verbose=0)
    return model
