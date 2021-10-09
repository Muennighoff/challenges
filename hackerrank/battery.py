#!/bin/python3

import math
import os
import random
import re
import sys

import numpy as np
import pandas as pd
import requests
from sklearn.ensemble import RandomForestRegressor


url = 'https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt'

def get_data(fname='train.txt', url='https://s3.amazonaws.com/hr-testcases/399/assets/trainingdata.txt'):
    """
    Downloads the training data.
    """
    r = requests.get(url)
    open(fname , 'wb').write(r.content)
    
    
def train_model(data_path='trainingdata.txt', debug=False):
    """
    Trains a model on training data.
    """
    train = pd.read_csv(data_path, names=["x", "y"], delimiter=",")
    
    # Prepare Data 
    # Shape: (100, 1) (Samples, Features)
    X = train.x.values.reshape(-1, 1)
    # Shape: (100)
    y = train.y.values
    
    if debug:
        X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_size, random_state=0)
    else:
        X_train = X
        y_train = y
    
    # Run Training
    model = RandomForestRegressor(n_estimators=10, max_features=1)
    model.fit(X_train, y_train)
    
    if debug:
        print("Score", model.score(X_test, y_test))
    
    return model
        
    
def main(timeCharged):
    # get_data()
    model = train_model()
    return round(model.predict(np.array([[timeCharged]])).item(), 2)
    
if __name__ == '__main__':
    timeCharged = float(input().strip())
    print(main(timeCharged))
