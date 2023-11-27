import pandas as pd
import numpy as np

# Modelling
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from scipy.stats import randint


import sys
 
# setting path
sys.path.insert(0, '/home/taposh/programming/dhal_ml')

import data_processing.get_x_y

X, Y = data_processing.get_x_y.get_now()

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

lr = LogisticRegression()

lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

