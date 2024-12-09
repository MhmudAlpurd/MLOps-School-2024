import mlflow
import pandas  as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

mlflow_server_uri = 'http://127.0.0.1:5000/'
mlflow.set_tracking_uri(mlflow_server_uri)


url  = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.data"
columns = ['CRIM',	'ZN'	, 'INDUS', 	'CHAS'	,'NOX'	,'RM'	,'AGE'	,'DIS'	,'RAD'	,'TAX'	, 'PTRATIO'	,'B',	'LSTAT', 	'MEDV']
data = pd.read_csv(url, delim_whitespace=True, names=columns)

X = data.drop('MEDV', axis=1)
y = data['MEDV']



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


logged_model = 'runs:/bf4d507fe8c944c09b02fb294c475041/linear_regression_model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd
predictions = loaded_model.predict(pd.DataFrame(X_test))
print(predictions)