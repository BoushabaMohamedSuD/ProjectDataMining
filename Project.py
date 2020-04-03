
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
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression



import requests 
import shutil
from bs4 import BeautifulSoup 
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
#     





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
counter=2;
IdRange=MaxDataSet['company_id']
while(counter<=IdRange):
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
datasetTestttttt=dataset   
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



dfPlot=dataset[['quit_date','salary']]
dfPlot.plot.box(dfPlot,y="salary")


############################
################ knn tree linear regrission

#################################"



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




#Change data type of columns salary to float

dataset['salary']=pd.to_numeric(dataset['salary'])
print('#######Check column data types##########')
datasetTypeSeries=dataset.dtypes
print(datasetTypeSeries)





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


#Feature scaling

#sc_X=StandardScaler()
#X_train=sc_X.fit_transform(X_train)
#X_test=sc_X.fit_transform(X_test)

#Fitting classifier to the training set

classifier=DecisionTreeClassifier(criterion='entropy',random_state=0)
classifier.fit(X_train,Y_train)


# Make Prediction
Y_pred_Tree=classifier.predict(X_test)

#Making the confusion Matrix

cm_Tree=confusion_matrix(Y_test,Y_pred_Tree)



# knn methode

classifier=KNeighborsClassifier(n_neighbors=5,metric='minkowski',p=2)
classifier.fit(X_train,Y_train)


# Make Prediction
Y_pred_kNN=classifier.predict(X_test)


#Making the confusion Matrix

cm_Knn=confusion_matrix(Y_test,Y_pred_kNN)



#############
# Prediction

################


#Linear Regression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)

#Make prediction

Y_pred_Linear=regressor.predict(X_test)

print(regressor.predict([[25,9800]]))






#####################################Exercice#######################################"








#making http request

r = requests.get('https://pokemondb.net/pokedex/national') 

#get the html text

html=r.text 
#print(html)



soup = BeautifulSoup(html,  'html.parser') 
#print(soup.prettify())
print(soup.title)
spans=soup.findAll('span',{"class": "infocard-lg-data text-muted"})
#names=soup.findAll('a',{"class": "ent-name"})
#powers=soup.findAll('a',{"class": "ent-name"})
#print(names)
data=[]
i=0
for span in spans:
    #print("-----start-------")
    i=i+1
    #print(i)
    links=span.findAll('a')
    j=0
    item=["",""]
    for link in links:
        #print(link.text)
        
        
        if(j==0):
            item[0]=link.text
        else:
            item[1]=item[1]+" "+link.text
            
        j=j+1
    data.append(item)        
    #print("-------end--------")        
    
   

#creating dataframe by using pandas

Pokemons=pd.DataFrame(data, columns = ['name', 'powers'])

#creat csv file 

Pokemons.to_csv(r'C:\Users\mohamed\Desktop\MINIPROJET\DataMining\export\Pokemons.csv',index = False)





spans=soup.findAll('span',{"class": "infocard-lg-img"})

print(span)

imgs=soup.findAll('img')
print(imgs)

i=0
for span in spans:
    
    link=span.find('a')
    #print(link)
    img=link.find('span')
    print(img.get('data-src'))
    img_src=img.get('data-src')
    response = requests.get(img_src,stream=True)
    #file=open("/test.png","wb") 

    response.raw_decode_content=True
  

    if response.status_code == 200:
        with open("C:/Users/mohamed/Desktop/MINIPROJET/DataMining/export/TestImages/"+data[i][0]+".jpg"
                  , 'wb') as f:
            f.write(response.content)
        
    del response        
    i=i+1     






#Qusetion3  





spans=soup.findAll('span',{"class": "infocard-lg-data text-muted"})

dataPokedex=[]
dataTraining=[]
dataBreeding=[]
dataOpps=[]

#print("go ....")
index=0
for span in spans:
    print("let's go ....",index)
    index=index+1
    link=span.find('a')
   # print(link.get('href'))
    href=link.get('href')
    response = requests.get('https://pokemondb.net/'+href)
    html1=response.text 
    #print(html1)
    soup1 = BeautifulSoup(html1,'html.parser') 
    name=soup1.find('h1').text
    #print(name)
    #getting data
    tables=soup1.findAll('table',{'class':'vitals-table'})
    #print(tables)
    j=0
    for table in tables:
        #print("her we  go again ....")
        if(j==0):
            #getting base data
            #print("data")
            
            trs=table.findAll('tr')
            counter=0
            item=[name,"","","","","","",""]
            
            
            for tr in trs:
                if(counter==0):
                    #print("National №")
                    info=""
                    try:    
                        info= tr.find('td').find('strong').text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])
                    
                    item[1]=info
                   
               
                    
                elif(counter==1):
                    #print("Type")
                    info=""
                    try:    
                        elements=tr.findAll('a')
                        for element in elements:
                            info=info+" "+element.text
                            
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                    
                    
                    item[2]=info
                    
                elif(counter==2):
                    #print("Species")
                    info=""
                    try:    
                        info=tr.find('td').text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                    
                    item[3]=info
                    
                elif(counter==3): 
                   # print("Height")
                    info=""
                    try:    
                        info=tr.find('td').text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                    
                    item[4]=info
                    
                elif(counter==4):
                    #print("Weight")
                    info=""
                    try:    
                        info=tr.find('td').text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                    
                    item[5]=info
                    
                elif(counter==5):
                    #print("Abilities")
                    info=""
                    try:    
                        elements=tr.findAll('a')
                        for element in elements:
                            info=info+" "+element.text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                    
                   
                    item[6]=info
                    
                elif(counter==6): 
                    #print("Local №№")
                    info=""
                    try:    
                       elements=tr.findAll('small')
                       for elemnent in elements:
                           info=info+" "+element.text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                    
                    
                    item[7]=info
                    
               
                
                counter=counter+1  
            
            dataPokedex.append(item)
             
                
            
            
            
        elif(j==1):
            #getting training data
            #print("training")
            
            trs=table.findAll('tr')
            counter=0
            item=[name,"","","","",""]
            
            for tr in trs:
                if(counter==0):
                   #print("EV yield")
                    #print('what!!!')
                    info=""
                    try:    
                        info=tr.find('td').text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                    
                    #print("ok")
                    #print(info)
                    item[1]=info
                    
                elif(counter==1):
                    #print("Catch rate")
                    info=""
                    try:    
                        info=tr.find('td').text+" "+tr.find('small').text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])
                    
                    item[2]=info
                    
                elif(counter==2):
                   # print("Base Friendship")
                    info=""

                    try:    
                        info=tr.find('td').text+" "+tr.find('small').text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                    
                    item[3]=info
                    
                elif(counter==3): 
                    #print("Base Exp.")
                    info=""
                    try:    
                        info=tr.find('td').text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                    
                    item[4]=info
                    
                elif(counter==4):
                    #print("Growth Rate")
                    info=""
                    try:    
                        info=tr.find('td').text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                    
                    item[5]=info
                    
                
               
                counter=counter+1  
                
            dataTraining.append(item)
            
           
                    
            
        elif (j==2):
            #getting breeding data
            #print("breeding")
            
            trs=table.findAll('tr')
            counter=0
            item=[name,"","",""]
            
            for tr in trs:
                if(counter==0):
                    #print("Egg Groups")
                    info=""

                    try:    
                       elements=tr.findAll('a')
                       for element in elements:
                           info=info+" "+element.text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                    
                        
                    item[1]=info
                    
                    
                elif(counter==1):
                    #print("Gender")
                    info=""

                    try:    
                        elements=tr.findAll('span')
                        for element in elements:
                            info=info+" "+element.text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                   
                        
                    item[2]=info
                    
                elif(counter==2):
                    #print("Egg cycles")
                    info=""

                    try:    
                         info=tr.find('td').text+" "+tr.find('small').text
                    except :
                        print("opps!!!!!!!!!!!!!!!")
                        dataOpps.append([index+1,j,counter])

                   
                    item[3]=info
                    
                    
                
                
                counter=counter+1
                
            dataBreeding.append(item)
                
            
                
            
            
            
            
        else:
            break
        
        
        j=j+1
        
    del response
    
     



#creating dataframe by using pandas

Pokedex=pd.DataFrame(dataPokedex, columns = ['name', 'National №','Type','Species'
                                             ,'Height','Weight','Abilities','Local №'])

Training=pd.DataFrame(dataTraining, columns = ['name','EV yield', 'Catch rate','Base Friendship'
                                               ,'Base Exp.' ,'Growth Rate'])

Breeding=pd.DataFrame(dataBreeding, columns = ['name', 'Egg Groups','Gender','Egg cycles'])

#creat csv file 

Pokedex.to_csv(r'C:\Users\mohamed\Desktop\MINIPROJET\DataMining\export\Pokedex.csv',index = False)
Training.to_csv(r'C:\Users\mohamed\Desktop\MINIPROJET\DataMining\export\Training.csv',index = False)
Breeding.to_csv(r'C:\Users\mohamed\Desktop\MINIPROJET\DataMining\export\Breeding.csv',index = False)










