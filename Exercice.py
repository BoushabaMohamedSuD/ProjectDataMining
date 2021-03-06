
#importing

import requests 
import shutil
from bs4 import BeautifulSoup 
import pandas as pd


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




'''
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


'''



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












