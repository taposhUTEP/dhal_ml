import numpy as np
import tensorflow as tf
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

import sys
 
# setting path
sys.path.insert(0, '/home/taposh/programming/dhal_ml')

import data_processing.get_x_y

X, Y = data_processing.get_x_y.get_now()
print(X[0])
print(Y[0])
hv = X.max()
X = X/hv # Normalize
print(X[0])

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

available_classes = np.unique(y_train)
#print(available_classes)
p_class = np.zeros(available_classes.shape)

for x in available_classes:
  p_class[x] = np.count_nonzero(y_train==x)
#print(np.sum(p_class))
print(p_class)
p_class = p_class/y_train.size
print(p_class)
print(p_class.shape[0])
print(x_train.shape[1])

p_att_given_class = np.zeros(p_class.shape[0]*x_train.shape[1]).reshape(p_class.shape[0], x_train.shape[1])
for x in available_classes:
  class_instances = x_train[y_train==x]
  #tt = class_instances.sum(axis=0)
  p_att_given_class[x] = class_instances.sum(axis=0)/class_instances.shape[0]
  #print(class_instances.shape)
  #print(class_instances.size)
  #print(tt)
print(p_att_given_class.shape)
#print(p_att_given_class[1])

def classify_no_loops(x,pc,pac):
  p = x*pac + (1-x)*(1-pac)
  #print(p)
  p = np.prod(p, axis=1)
  #print(p)
  p = pc*p
  #print(p)
  p = p/np.sum(p)
  #print(p)
  return np.argmax(p)

y_preds = np.zeros(y_test.shape)
for i in range(y_preds.shape[0]):
  y_preds[i] = classify_no_loops(x_test[i], p_class, p_att_given_class)
#print(preds)
print("Accuracy: {}".format(accuracy_score(y_test, y_preds)))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_preds))
