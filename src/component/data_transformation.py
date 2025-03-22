 
from data_ingestion import load_data
from logger import logging

train_data, train_targets, test_data, test_targets = load_data()

def normalize(train_data, test_data):
# Normalize Data using Feature-wise Technique
    mean = train_data.mean(axis=0)
    train_data -=mean
    std = train_data.std(axis=0)
    train_data /=std
    logging.info("train data Normalized")
    test_data -=mean
    test_data/= std
    logging.info("test data Normalized")
    return train_data, test_data

train_df, test_df = normalize(train_data, test_data)