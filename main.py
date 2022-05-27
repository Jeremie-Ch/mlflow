import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor

import mlflow.sklearn

"""MLFlow UI's address"""
mlflow.set_tracking_uri("http://10.3.15.100:8080")

"""Experiment that you are working on"""
exp_id = "0"

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == '__main__':
    # Load the data and create the train and test sets here
    df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=";")
    train, test = train_test_split(df)
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    n_estimators = int(sys.argv[1]) if len(sys.argv) > 1 else 100

    with mlflow.start_run(experiment_id=exp_id, run_name="run_name", description="Run description") as run:
        """ Write the model here """
        rf = RandomForestRegressor(n_estimators)
        rf.fit(train_x, train_y)
        prediction = rf.predict(test_x)

        rmse, mae, r2 = eval_metrics(test_y, prediction)

        print('Score (n_estimators=%f):' % (n_estimators))
        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)

        # Logging parameters
        mlflow.log_param("n_estimators", n_estimators)

        # Logging metrics
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)

        # Saving artifacts
        mlflow.log_artifact("txt_artifact.txt", artifact_path="model")

        # Logs the model and saves it as an artifact
        mlflow.sklearn.log_model(rf, "model", registered_model_name="sklearn model")
