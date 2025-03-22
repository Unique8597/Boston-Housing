from keras.datasets import boston_housing
from logger import logging

def load_data():
    (train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()
    logging.info("Data loaded Successfully")
    return train_data, train_targets, test_data, test_targets

   