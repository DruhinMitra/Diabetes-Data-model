import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('text2.csv')
X1=df['test_split']
X2=df['random_state']
Y=df['accuracy']

max=Y[0]
for i in Y:
    if(i>max):
        max=i
    else:
        continue

print(max)

plt.plot(X2,Y)
plt.xlabel('test_split')
plt.ylabel('accuracy')
plt.show()
