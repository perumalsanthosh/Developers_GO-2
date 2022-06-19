# -*- coding: utf-8 -*-
"""project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MkOEggC3anEVwcqe9dI47KLj-kbuj37E

**1.Importing necessary libraries.**
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn 
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

"""**2.Importing The github or file into a variable using pandas.**"""

data=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

"""**3.Analysing the dataset.**"""

data.info()

"""**4.Different kinds of variables in the data**"""

#indepedent data="PassengerId","Name",Age,Ticket,sibsip
#dep="survived","Pclass","Sex" 
#Target variable=survived
#categorical data=Pclass,survived,age,sibsip,embarked

"""**5.Dropping unused data in the prediction**"""

data.drop("Name",axis=1,inplace=True)
data.drop("PassengerId",axis=1,inplace=True)
data.drop("Ticket",axis=1,inplace=True)

"""**6.Checking for missing values in data**"""

data.isnull().sum()

"""**From above we Can see that age,cabin,embarked has missing values.**

**7.Removing missing values or noisy from the data.By using fill na method**
"""

data['Age'].fillna(value=data["Age"].mean(),inplace=True) 
data['Cabin'].fillna(0,inplace=True)
data['Embarked'].fillna(0,inplace=True)

x=data.value_counts(data["Embarked"])
print(x)

"""**8.Once again checking data for any missing values or noisy  data.**"""

data.isnull().sum()

"""**From above we can see that the data is not containg any missed values or noisy data**.

**9.Performing data.describe for seeing statistical accuracy of the data.**
"""

print(data.describe())

print(data)

x=data.value_counts(data["Pclass"])
print(x)
sum=0
for i in x:
  sum+=i
print(sum)

data.describe()

"""**10.Visualization using matplotlib**"""

#pie graph which indicate survived or not survived
x=data.value_counts(data["Survived"]).values
a=x[0]
b=x[1]
lab=["Not survived","Survived"]
print(a,b)
plt.pie(x,labels=lab,labeldistance=0.3)
plt.legend(title="Survived")
plt.show()

#bar graph which indicate survived or not survived
x=data.value_counts(data["Survived"]).values
lab=[0,1]
plt.bar(x,x,width=120,color= "#4CAF50")
plt.title("Survived",fontsize=20)
plt.xticks(x,lab,fontsize=14)
plt.xlabel("survived or not survived",fontsize=15)
plt.ylabel("no of persons",fontsize=15)
plt.show()

#bar graph which indicate survived or not survived of male and female
x=data.value_counts(data["Sex"]).values
print(x)
lab=["Male","Female"]
plt.bar(x,x,width=120,color= "#4CAF50")
plt.title("Survived",fontsize=20)
plt.xticks(x,lab,fontsize=14)
plt.xlabel("Sex",fontsize=15)
plt.ylabel("no of persons",fontsize=15)
plt.show()

"""**11.Visualization using Seaborn**"""

#bar graph which indicate survived or not survived using sea born
seaborn.countplot("Survived",data=data)

#bar graph which indicate survived or not survived of male or femle using seaborn
seaborn.countplot("Sex",data=data)

#bar graph which indicate survived or not survived and also indicates how many male or female surived 
seaborn.countplot("Sex",hue="Survived",data=data)

#bar graph which indicate pclass 
seaborn.countplot("Pclass",data=data)

#bar graph which indicate survived or not survived and also indicates plcasses of survived oor not survived
seaborn.countplot("Pclass",hue="Survived",data=data)

#bar graph which indicate embarked of data.
seaborn.countplot("Embarked",data=data)

#bar graph which indicate survived or not survived and also indicates plcasses of survived oor not survived
seaborn.countplot("Pclass",hue="Survived",data=data)

seaborn.countplot("SibSp",data=data)

seaborn.countplot("SibSp",hue="Survived",data=data)

seaborn.countplot("Parch",data=data)

seaborn.countplot("Parch",hue="Survived",data=data)

data["Sex"].value_counts()

"""**12.Encoding categorical data**"""

data.replace({"Sex":{"male":0,"female":1},"Embarked":{"S":0,"C":1,"Q":2}},inplace=True)
print(data.head())

"""**13.spliting data into dependent and independent**"""

x=data.drop(columns=["Survived","Cabin"],axis=1)
y=data["Survived"]
print(x)
print(y)
# print(data)

"""**14.Splitting the data into the Training set and Test set**"""

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.3,random_state=0)
print(x.shape,X_train.shape,X_test.shape)

"""**15.Performing Logistic Regression**"""

log_model=LogisticRegression()
log_model.fit(X_train,Y_train)

"""**16.Predicting training data model**"""

pred_x_train=model.predict(X_train)
print(pred_x_train)

"""**17.Accuracy of training data model**"""

train_accuracy=accuracy_score(Y_train,pred_x_train)
print("The Accuracy of training data is:",train_accuracy)

"""**18.Predicting test data model**"""

pred_x_test=model.predict(X_test)
print(pred_x_test)

"""**19.Accuracy of test data model**"""

test_accuracy=accuracy_score(Y_test,pred_x_test)
print("The Accuracy of test data is:",test_accuracy)