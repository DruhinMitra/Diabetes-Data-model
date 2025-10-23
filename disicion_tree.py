
import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn import linear_model
import matplotlib.pyplot as plt
import random
db=pd.read_csv('diabetes.csv')
X=db.drop('Outcome',axis=1)
y=db['Outcome']
X_train , X_test ,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=25)
model=DecisionTreeRegressor(criterion='squared_error',splitter='best')
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print("Accuracy Score= " ,accuracy_score(y_test,y_pred))
print(y_pred)
print(X_test)
start=0.1
end=0.9
step=0.2
l=[]
while(step<end):

  l.append(step)
  step=step+0.1


flag=0
with open('text2.csv','a+') as ifile:
  df=ifile.read()
  if df=='':
    flag=1

with open('text2.csv','w') as ifile:
  if flag==1:
    header=['test_split','random_state','accuracy']
    writer_=csv.writer(ifile)
    writer_.writerow(header)
acl=[]
for i in range(0,50):

  for j in range(0,len(l)):
    X_train , X_test ,y_train,y_test=train_test_split(X,y,test_size=l[j],random_state=i)
    model=DecisionTreeClassifier(criterion='entropy',splitter='random')
    model.fit(X_train,y_train)
    y_pred=model.predict(X_test)
    accuracy=accuracy_score(y_test,y_pred)
    if(len(acl)==0):
      acl.append(accuracy)

    elif(accuracy>max(acl)):
     
      with open('text2.csv','a') as ifile:
        writer_=csv.writer(ifile)
        writer_.writerow([l[j],i,accuracy])







