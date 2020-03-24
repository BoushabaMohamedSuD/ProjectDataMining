
######
# Prétraitement de données
#####
# importing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import datetime as dtime

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
        #print(counter)
    counter=counter+1   
     
    
datasetMissingDataSalary= dataset['salary'].isnull() 


#Change data type of columns salary to float

dataset['salary']=pd.to_numeric(dataset['salary'])
print('#######Check column data types##########')
datasetTypeSeries=dataset.dtypes
print(datasetTypeSeries)








###########################################################################"
##########################################################################
#         LOOOOOOOOOK PARTIE 2





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
 

# delteing missing values of join_date column

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
dataCondition=[]
value=1
capturINDEX=0
counter1=0
counter2=1
key=True



#initializing dataCondition

counter=1
while(counter<=MaxDataSet['company_id']):
    dataCondition.append([counter,True])
    counter=counter+1
print(dataCondition)


# delteing missing values of quit_date   column
# join date already did

datasetMissingDataQuiteDate= dataset['quit_date'].isnull() 
print("#########Mising values of dataset quit_date  time#########")
counter=0
lenghtDataset=len(dataset)
while(counter<lenghtDataset):
    if(datasetMissingDataQuiteDate[counter]==True):
        dataset=dataset.drop([counter])
        
    counter=counter+1   
         

print('ok')




#sort the dataset to make the calcule more easy
print("######### sort the dataset to make the calcule more easy #########")
dataset.sort_values(by=['join_date'], inplace=True, ascending=True)
dataset =dataset.reset_index(drop=True)


if(dataset['join_date'][0]==dataset['join_date'][1]):
    print('ok yuuup')

# Make Operations

print('make operation')
lenghtDataset=len(dataset)

while(counter1<lenghtDataset):
    #print(counter1)
    #counter2=counter1+1
    while (counter2<lenghtDataset):
        if(dataset['join_date'][counter1]==dataset['join_date'][counter2]):
            if(dataset['company_id'][counter1]==dataset['company_id'][counter2]):
                value=value+1
                if(counter2==lenghtDataset-1):
                    companyId=dataset['company_id'][counter1]
                    joinDATE=dataset['join_date'][counter1]
                    data.append([companyId,joinDATE,value])
                    # RESET EVRYTHING !!!!!
                
                    key=True
                    value=1
                    counter1=counter2+1
                
                    counter=0
                    while(counter<MaxDataSet['company_id']):
                        dataCondition[counter][1]=True
                        counter=counter+1
                        
                    print('break 1')    
                    break
            else:
                if(key):
                    companyId=dataset['company_id'][counter2]
                    #print(companyId)
                    if(dataCondition[companyId-1][1]): 
                        capturINDEX=counter2
                        key=False
                        
                        if(counter2==lenghtDataset-1):
                            companyId=dataset['company_id'][counter1]
                            joinDATE=dataset['join_date'][counter1]
                            data.append([companyId,joinDATE,value])
                
                            #block this case to happen agian
                
                            dataCondition[companyId-1][1]=False
                
                            # jump to the other case   
                            #in this case counter1=lenghtDataset-1 !!!!!!!!!!
                            
                            counter1=capturINDEX
                            key=True
                            value=1
                        
                            print('break 2')
                            break
                        
        else :
            if(capturINDEX==counter1):
                companyId=dataset['company_id'][counter1]
                joinDATE=dataset['join_date'][counter1]
                data.append([companyId,joinDATE,value])
                
                # RESET EVRYTHING !!!!!
                
                key=True
                value=1
                counter1=counter2
                counter2=counter1+1   
                
                #############################
                #it cause me 6 houres to fix it
                #by adding just this line to code
                
                capturINDEX=counter1
                ##############################
                counter=0
                while(counter<MaxDataSet['company_id']):
                    dataCondition[counter][1]=True
                    counter=counter+1
                
                #print('break3')
                break
            else:
                companyId=dataset['company_id'][counter1]
                joinDATE=dataset['join_date'][counter1]
                data.append([companyId,joinDATE,value])
                
                #block this case to happen agian
                
                dataCondition[companyId-1][1]=False
                
                # jump to the other case   
             
                counter1=capturINDEX
                counter2=counter1+1
                key=True
                value=1
                #print('break 4')
                break
        #print(counter1)                        
        counter2=counter2+1
        #print(counter2)
       # print(counter2)
        
    # add if the last one is unique
    
    if(counter1==lenghtDataset-1):
        companyId=dataset['company_id'][counter1]
        joinDATE=dataset['join_date'][counter1]
        data.append([companyId,joinDATE,value])
        break
        
        
            
            
print('ok')
NewHire=pd.DataFrame(data, 
           columns = ['company_id', 'join_date',', count_new_hire'])
                            





# count churn each day


##initialinitializing dataframe handler
data=[]
dataCondition=[]
value=1
capturINDEX=0
counter1=0
counter2=1
key=True



#initializing dataCondition

counter=1
while(counter<=MaxDataSet['company_id']):
    dataCondition.append([counter,True])
    counter=counter+1
print(dataCondition)



#sort the dataset to make the calcule more easy
print("######### sort the dataset to make the calcule more easy #########")
dataset.sort_values(by=['quit_date'], inplace=True, ascending=True)
dataset =dataset.reset_index(drop=True)




# Make Operations

print('make operation')
lenghtDataset=len(dataset)

while(counter1<lenghtDataset):
    #print(counter1)
    #counter2=counter1+1
    while (counter2<lenghtDataset):
        if(dataset['quit_date'][counter1]==dataset['quit_date'][counter2]):
            if(dataset['company_id'][counter1]==dataset['company_id'][counter2]):
                value=value+1
                if(counter2==lenghtDataset-1):
                    companyId=dataset['company_id'][counter1]
                    QuitDate=dataset['quit_date'][counter1]
                    data.append([companyId,QuitDate,value])
                    # RESET EVRYTHING !!!!!
                
                    key=True
                    value=1
                    counter1=counter2+1
                
                    counter=0
                    while(counter<MaxDataSet['company_id']):
                        dataCondition[counter][1]=True
                        counter=counter+1
                        
                    #print('break 1')    
                    break
            else:
                if(key):
                    companyId=dataset['company_id'][counter2]
                    #print(companyId)
                    if(dataCondition[companyId-1][1]): 
                        capturINDEX=counter2
                        key=False
                        
                        if(counter2==lenghtDataset-1):
                            companyId=dataset['company_id'][counter1]
                            QuitDate=dataset['quit_date'][counter1]
                            data.append([companyId,QuitDate,value])
                
                            #block this case to happen agian
                
                            dataCondition[companyId-1][1]=False
                
                            # jump to the other case   
                            #in this case counter1=lenghtDataset-1 !!!!!!!!!!
                            
                            counter1=capturINDEX
                            key=True
                            value=1
                        
                            #print('break 2')
                            break
                        
        else :
            if(capturINDEX==counter1):
                companyId=dataset['company_id'][counter1]
                QuitDate=dataset['quit_date'][counter1]
                data.append([companyId,QuitDate,value])
                
                # RESET EVRYTHING !!!!!
                
                key=True
                value=1
                counter1=counter2
                counter2=counter1+1   
                
                #############################
                #it cause me 6 houres to fix it
                #by adding just this line to code
                
                capturINDEX=counter1
                ##############################
                counter=0
                while(counter<MaxDataSet['company_id']):
                    dataCondition[counter][1]=True
                    counter=counter+1
                
                #print('break3')
                break
            else:
                companyId=dataset['company_id'][counter1]
                QuitDate=dataset['quit_date'][counter1]
                data.append([companyId,QuitDate,value])
                
                #block this case to happen agian
                
                dataCondition[companyId-1][1]=False
                
                # jump to the other case   
             
                counter1=capturINDEX
                counter2=counter1+1
                key=True
                value=1
                #print('break 4')
                break
        #print(counter1)                        
        counter2=counter2+1
        #print(counter2)
       # print(counter2)
        
    # add if the last one is unique
    
    if(counter1==lenghtDataset-1):
        companyId=dataset['company_id'][counter1]
        QuitDate=dataset['quit_date'][counter1]
        data.append([companyId,QuitDate,value])
        break
        
        
            
            
print('ok')
Churn=pd.DataFrame(data, 
           columns = ['company_id', 'quit_date',', count_chrun'])
 

                           
#boxplot churn/salary





















