from model_train import cross_validation, final_model, train_df, train_targets,test_df, test_targets
from logger import logging
import numpy as np
import pickle
import os

def evaluate_model():
    print("Cross validation Result")
    #all_scores = cross_validation(train_df,train_targets)
    #print(np.mean(all_scores))
    # Evaluate final model
    model = final_model()
    test_mse_score, test_mae_score = model.evaluate(test_df, test_targets)
    print(test_mse_score, test_mae_score)
    return model

model = evaluate_model()

def save_model(model, file_path="app/model.pkl"):
    
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            pickle.dump(model, file)
        print(f"Model saved successfully at {file_path}")
    except Exception as e:
        print(f"Error saving model: {e}")


# Save the model
save_model(model)


