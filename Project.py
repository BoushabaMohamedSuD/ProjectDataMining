# importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#reading dataset

dataset=pd.read_csv('employee_retention_data.csv')

#changing the columns dataset on lower case

dataset.columns= map(str.lower, dataset.columns)

#Check column data types
print('#######Check column data types##########')
datasetTypeSeries=dataset.dtypes
print(datasetTypeSeries)


#Convert Columns (join-date & quit-date) on date time

dataset['join_date']= pd.to_datetime(dataset['join_date'])
dataset['quit_date']= pd.to_datetime(dataset['quit_date'])
print('#######Check column data types##########')
datasetTypeSeries=dataset.dtypes
print(datasetTypeSeries)

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
        print(counter)
    counter=counter+1   
     

datasetMissingDataSalary= dataset['salary'].isnull() 


