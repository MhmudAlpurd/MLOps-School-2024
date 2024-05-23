#inference
import numpy as np 
import joblib

model_filename = 'house_price_model.joblib'
loaded_model = joblib.load(model_filename)


def predicted_house_price():
    try:
        house_size = float(input("Enter the size of the house in square feet: "))
        house_size_array = np.array([[house_size]])
        
        predicted_price = loaded_model.predict(house_size_array)
        print(f'Predicted price for a {house_size} sq ft house:${predicted_price[0]*1000:.2f}')
    except ValueError:
              print("Invalid input, please enter a numeric value for house size.")
   
    

