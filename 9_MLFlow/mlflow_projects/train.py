import mlflow
import mlflow.sklearn
import argparse
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error, r2_score



#mlflow_server_uri = 'http://127.0.0.1:5000/'
#mlflow.set_tracking_uri(mlflow_server_uri)
#mlflow.set_experiment("california house price estimation")

def train_model(learning_rate, test_size, epochs):
    with mlflow.start_run():
        data = fetch_california_housing(as_frame=True)
        X = data.data
        y = data.target


        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42 )


        #train
        model = SGDRegressor(max_iter=epochs, eta0=learning_rate, learning_rate='constant')
        model.fit(X_train, y_train)

        #evalution
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        #hyper parameters
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("test_size", test_size)
        mlflow.log_param("epochs", epochs)

        #performance metrics
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("r2_score", r2)

        #model
        mlflow.sklearn.log_model(model, "SGDRegressor_model")


if __name__=="__main__":
    #sample : python train.py --lr 0.5 --test_size 0.1 --epochs 100
    parser = argparse.ArgumentParser()
    parser.add_argument("--lr", type=float, default=0.01, help="Learning rate for the model")
    parser.add_argument("--test_size", type=float, default=0.2, help="Proportion of test data")
    parser.add_argument("--epochs", type=int, default=100, help="Number of training epochs")

    args = parser.parse_args()

    train_model(args.lr, args.test_size, args.epochs )



