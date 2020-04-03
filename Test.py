import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import datetime as dtime
from bs4 import BeautifulSoup 

#reading datase

test=["",""]
test[0]=test[0]+"ds"
test[0]=test[0]+" "+"ghj"




#importing

import requests 
import shutil

'''

response = requests.get('https://img.pokemondb.net/sprites/sword-shield/pixel/copperajah.png',stream=True)
#file=open("/test.png","wb") 

response.raw_decode_content=True
  




if response.status_code == 200:
    with open("C:/Users/mohamed/Desktop/MINIPROJET/DataMining/export/TestImages/TestImagesTestImagessample.jpg"
              , 'wb') as f:
        f.write(response.content)
        
        
        
del response        
        

r = requests.get('https://pokemondb.net/pokedex/bulbasaur') 

html=r.text 
#print(html)



soup = BeautifulSoup(html,  'html.parser')

table=soup.find('table',{'class':'vitals-table'})
name=soup.find('h1').text
print(name)


items=[""]
items[0]="ds"

print(items)
#print(table)

'''
response=requests.get("https://pokemondb.net/pokedex/falinks")

html1=response.text
soup1 = BeautifulSoup(html1,'html.parser') 
name=soup1.find('h1').text
print(name)
tables=soup1.findAll('table',{'class':'vitals-table'})



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
                    info= tr.find('td').find('strong').text
                    item[1]=info
                   
               
                    
                elif(counter==1):
                    #print("Type")
                    info=""
                    elements=tr.findAll('a')
                    for element in elements:
                        info=info+" "+element.text
                    item[2]=info
                    
                elif(counter==2):
                    #print("Species")
                    info=tr.find('td').text
                    item[3]=info
                    
                elif(counter==3): 
                   # print("Height")
                    info=tr.find('td').text
                    item[4]=info
                    
                elif(counter==4):
                    #print("Weight")
                    info=tr.find('td').text
                    item[5]=info
                    
                elif(counter==5):
                    #print("Abilities")
                    info=""
                    elements=tr.findAll('a')
                    for element in elements:
                        info=info+" "+element.text
                   
                    item[6]=info
                    
                elif(counter==6): 
                    #print("Local №№")
                    info=""
                    elements=tr.findAll('small')
                    for elemnent in elements:
                        info=info+" "+element.text
                    
                    item[7]=info
                    
               
                
                counter=counter+1  
            
           
             
                
            
            
            
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
                    info=tr.find('td').text
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
                       
                    
                    item[2]=info
                    
                elif(counter==2):
                   # print("Base Friendship")
                   info=""
                   try:
                        info=tr.find('td').text+" "+tr.find('small').text
                   except :
                       print("opps!!!!!!!!!!!!!!!")
                        
                   
                   item[3]=info
                    
                elif(counter==3): 
                    #print("Base Exp.")
                    info=tr.find('td').text
                    item[4]=info
                    
                elif(counter==4):
                    #print("Growth Rate")
                    info=tr.find('td').text
                    item[5]=info
                    
                
               
                counter=counter+1  
                
            
            
           
                    
            
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
                    elements=tr.findAll('a')
                    for element in elements:
                        info=info+" "+element.text
                        
                    item[1]=info
                    
                    
                elif(counter==1):
                    #print("Gender")
                    info=""
                    elements=tr.findAll('span')
                    for element in elements:
                        info=info+" "+element.text
                        
                    item[2]=info
                    
                elif(counter==2):
                    #print("Egg cycles")
                    info=tr.find('td').text+" "+tr.find('small').text
                    item[3]=info
                    
                    
                
                
                counter=counter+1
                
           
                
            
                
            
            
            
            
        else:
            break
        
        
        j=j+1

