from model_train import cross_validation, final_model, train_df, train_targets,test_df, test_targets
from logger import logging
import numpy as np


def evaluate_model():
    print("Cross validation Result")
    all_scores = cross_validation(train_df,train_targets)
    print(np.mean(all_scores))
    # Evaluate final model
    model = final_model()
    test_mse_score, test_mae_score = model.evaluate(test_df, test_targets)
    print(test_mse_score, test_mae_score)

evaluate_model()

