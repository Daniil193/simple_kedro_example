import logging
from typing import Dict, Tuple

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

import mlflow
from mlflow import sklearn



def get_score(name_metric: str, y_true: pd.Series, y_pred: (np.ndarray, np.array)) -> float:
    ## проверка на правильность названия метрики
    name_metrics = [i for i in dir(metrics) if callable(getattr(metrics, i)) and not i.startswith("__")]
    if name_metric not in name_metrics:
        print("Invalid metric name")
        return np.nan
    score = getattr(metrics, name_metric)(y_true, y_pred)
    return round(score, 2)


def split_data(df: pd.DataFrame, parameters: Dict) -> Tuple:
    X = df[parameters["features"]]
    y = df["Survived"]
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y,
                                                        test_size=parameters["test_size"],
                                                        random_state=parameters["random_state"])
    mlflow.log_param("test_size", parameters["test_size"])
    mlflow.log_param("random_state", parameters["random_state"])
    mlflow.log_param("features", parameters["features"])
    return X_train, X_test, y_train, y_test
    
    
def train_model(X_train: pd.DataFrame, y_train: pd.Series, parameters: Dict) -> RandomForestClassifier:
    rndm_forest = RandomForestClassifier(n_estimators=parameters["n_estimators"])
    rndm_forest.fit(X_train, y_train)
    mlflow.log_param("n_estimators", parameters["n_estimators"])
    return rndm_forest

    
def evaluate_model(rndm_forest: RandomForestClassifier, X_test: pd.DataFrame, y_test: pd.Series, parameters: Dict):
    y_pred = rndm_forest.predict(X_test)
    score = get_score(parameters["metric"], y_test, y_pred)
    #logger = logging.getLogger(__name__)
    #logger.info(f"Model has a value {score} for {parameters['metric']}")
    #sklearn.log_model(sk_model=rndm_forest, artifact_path="model")
    mlflow.log_metric(parameters["metric"], score)
    
    
    
    