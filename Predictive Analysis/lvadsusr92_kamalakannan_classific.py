# -*- coding: utf-8 -*-
"""lvadsusr92_kamalakannan_classific.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-RyLW1kr56444lYuTNpel8LYp9oICIMz
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix, recall_score, f1_score, precision_score,silhouette_score, davies_bouldin_score, calinski_harabasz_score,mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('/content/loan_approval.csv')
df.columns

df.isnull().sum()

plt.figure(figsize = (20,7), dpi = 150)
sns.boxplot(df)
plt.show()

df

q1=df[' residential_assets_value'].quantile(0.25)
q3=df[' residential_assets_value'].quantile(0.75)
iqr=q3-q1
l_limit=q1-(iqr*1.5)
u_limit=q3+(iqr*1.5)
df=df[(df[' residential_assets_value']>l_limit) & (df[' residential_assets_value']<u_limit)]
df

dd=df[df.duplicated()]
dd

print('Head of the dataset:\n',df.head())
print('Description of the dataset:\n',df.describe())
print('Columns of the dataset:\n',df.columns)
print('Shape of the data:\n',df.shape)

#Encoding categorical variables
lb=LabelEncoder()
df[' education']=lb.fit_transform(df[' education'])
df[' loan_status']=lb.fit_transform(df[' loan_status'])
df[' self_employed']=lb.fit_transform(df[' self_employed'])

#Model dev
X=df.drop(columns=[' loan_status','loan_id'])
y=df[' loan_status']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
ml=RandomForestClassifier()
fit=ml.fit(X_train,y_train)
op=ml.predict(X_test)
print(op)

a=accuracy_score(y_test,op)
c=confusion_matrix(y_test,op)
r=recall_score(y_test,op)
f=f1_score(y_test,op)
p=precision_score(y_test,op)
cvs=cross_val_score(ml,X_train,y_train,cv=5)

print('Accuracy Score:',a)
print('\nConfusion Matrix:\n',c)
print('\nRecall Score:',r)
print('\nF1 Score:',f)
print('\nPrecision Score:',p)
print('\nCross validation score:',cvs)

