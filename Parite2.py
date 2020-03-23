#####
# importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import datetime as dtime



#reading dataset

dataset=pd.read_csv('employee_retention_data.csv')




######
# Description
#####

#nbr rows and columns 
print('#######Number rows columns##########')
print(dataset.shape)
nbrRows=dataset.shape[0]
nbrColumns=dataset.shape[1]

# min max std count

print('########Mean#########')
MeanDataSet=dataset.mean()      
#print(dataset.mean())
print('########Max#########')
MaxDataSet=dataset.max()     
#print(dataset.max())
print('########Count#########')
CountDataSet=dataset.count()     
#print(dataset.count())
print('########Std#########')
StdDataSet=dataset.std()     
#print(dataset.std())
print('########Min#########')
MinDataSet=dataset.min()     
#print(dataset.std())

print(dataset.describe())
DatasetDescription=dataset.describe()

# estimate of the workforce, for each company

time1=dataset['join_date'][0]
time2=dataset['join_date'][1]
timeStart=np.datetime64('2011-01-24')
timeEnd=np.datetime64('2015-12-13')
if(timeEnd<timeStart):
    print('not ok')
else :
    print('it is ok')
    
counter=0   

print(timeEnd-timeStart)
lenghtDataset=len(dataset)
print(counter)
##initialinitializing dataframe handler
data = [[1, 0]] 
counter=1;
IdRange=MaxDataSet['company_id']
while(counter<IdRange):
    data.append([counter,0])
    counter=counter+1
#print(data)

print(dataset['quit_date'][26])


if(dataset.isnull()['quit_date'][26]):
    print('ok')
else: 
    print('not ok')
 

# delteing missing values of salary column

datasetMissingDataJoinDate= dataset['join_date'].isnull() 
print("#########Mising values of dataset join time#########")
#print(dataset['salary'].isnull() )
#print(dataset['salary'][100])
counter=0
lenghtDataset=len(dataset)
while(counter<lenghtDataset):
    if(datasetMissingDataJoinDate[counter]==True):
        dataset=dataset.drop([counter])
        #print(counter)
    counter=counter+1   
         
#calculing    
lenghtDataset=len(dataset)
counter=0
while(counter<lenghtDataset):
  
    if(dataset['join_date'][counter]<=timeEnd and 
       dataset['join_date'][counter]>=timeStart):
        index=dataset['company_id'][counter]-1
        data[index][1]=data[index][1]+1
    if(dataset['quit_date'][counter]<=timeEnd and
       dataset['quit_date'][counter]>=timeStart): 
        index=dataset['company_id'][counter]-1
        data[index][1]=data[index][1]-1
    counter=counter+1
    #print(counter)
    
    
print('end loop')    
print(data)

#creating data frame

Estimation=pd.DataFrame(data, columns = ['company_id', 'count'])

# estimate of the workforce, for each company, each day

counter=0
print((timeEnd-timeStart).astype("float"))
AverageTime=(timeEnd-timeStart).astype("float")
while(counter<len(data)):
    data[counter][1]=data[counter][1]/AverageTime
    counter=counter+1

EstimationEachDay=pd.DataFrame(data, columns = ['company_id', 'count\Day'])

# count new hire each day


##initialinitializing dataframe handler
data=[]


#sort the dataset to make the calcule more easy

dataset.sort_values(by=['join_date'], inplace=True, ascending=True)
dataset =dataset.reset_index(drop=True)
