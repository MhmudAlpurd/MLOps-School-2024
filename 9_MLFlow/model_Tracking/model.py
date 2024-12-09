import mlflow
import pandas  as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error


url  = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.data"
columns = ['CRIM',	'ZN'	, 'INDUS', 	'CHAS'	,'NOX'	,'RM'	,'AGE'	,'DIS'	,'RAD'	,'TAX'	, 'PTRATIO'	,'B',	'LSTAT', 	'MEDV']
data = pd.read_csv(url, delim_whitespace=True, names=columns)

X = data.drop('MEDV', axis=1)
y = data['MEDV']



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()


mlflow_server_uri = 'http://127.0.0.1:5000/'
mlflow.set_tracking_uri(mlflow_server_uri)
mlflow.set_experiment("house price estimation")


with mlflow.start_run():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    mlflow.log_param("model name", "Linear Regression")
    mlflow.log_param("data_split", "20 / 80")
    mlflow.log_metric("mse", mse)
    mlflow.sklearn.log_model(model, "linear_regression_model")
    
