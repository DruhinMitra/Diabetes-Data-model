import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn import linear_model
import matplotlib.pyplot as plt
import random

df=pd.read_csv('diabetes.csv')

