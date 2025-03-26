import pickle
import os
import numpy as np

def run_inference(file_path="app/model.pkl"):
    try:
        # Ensure the model file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Model file not found at: {file_path}")
        
        # Load the model
        with open(file_path, "rb") as file:
            model = pickle.load(file)

        # Ensure input is a 2D array for prediction
        input_data = np.array([[0.00632, 18.0, 2.31, 0.0, 0.538, 6.575, 65.2, 4.09, 1.0, 296.0, 15.3, 396.9, 4.98]])

        
        # Run inference
        y_pred = model.predict(input_data)
        print("Prediction:", y_pred)

    except Exception as e:
        print(f"Error during inference: {e}")

def main():
    run_inference()

if __name__ == "__main__":
    main()
