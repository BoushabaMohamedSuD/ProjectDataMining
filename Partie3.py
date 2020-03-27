######
# Prétraitement de données
#####
# importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import datetime as dtime

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

#reading dataset

dataset=pd.read_csv('employee_retention_data.csv')



#changing the columns dataset on lower case

dataset.columns= map(str.lower, dataset.columns)


# delteing missing values of salary column


datasetMissingData= dataset.isnull() 
datasetMissingDataSalary= dataset['salary'].isnull() 
print("#########Mising values of dataset########");
#print(dataset['salary'].isnull() )
#print(dataset['salary'][100])
print("dataset lenght :",len(dataset));
counter=0
lenghtDataset=len(dataset)
while(counter<lenghtDataset):
    if(datasetMissingDataSalary[counter]==True):
        dataset=dataset.drop([counter])
        #print(counter)
    counter=counter+1   
     
    
datasetMissingDataSalary= dataset['salary'].isnull() 



#encodeing churn data

LabelEncoder_Fit=LabelEncoder()
churnEncoding=LabelEncoder_Fit.fit_transform(dataset['churn'])
print(churnEncoding)
dataset['churn']=churnEncoding


#splitting dataset to input output
X=dataset[['seniority','salary']]
Y=dataset[['churn']]


#split dataset to the train set and test set

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,
train_size=0.8,
test_size=0.2,
random_state=0)


#Fitting classifier to the training set

classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(X_train,Y_train)


# Make Prediction
Y_pred=classifier.predict(X_test)

#Making the confusion Matrix

cm=confusion_matrix(Y_test,Y_pred)













