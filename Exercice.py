
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
data=[]
for span in spans:
    link=span.find('a')
    #print(link.get('href'))
    href=link.get('href')
    response = requests.get('https://pokemondb.net/'+href)
    html1=r.text 
    soup1 = BeautifulSoup(html,  'html.parser') 
    
    #getting data
    tables=soup1.findAll('table',{'class':'vitals-table'})
    j=0
    for table in tables:
        if(j==0):
            #getting base data
            print("data")
            
            tr=table.find('tr')
            counter=0
            for tr in trs:
                if(counter==0):
                    print("National №")
                    
                elif(counter==1):
                    print("Type")
                    
                elif(counter==2):
                    print("Species")
                    
                elif(counter==3): 
                    print("Height")
                    
                elif(counter==4):
                    print("Weight")
                    
                elif(counter==5):
                    print("Abilities")
                    
                elif(counter==6): 
                    print("Local №№")
                    
                    
            
            
            
        elif(j==1):
            #getting training data
            print("training")
            tr=table.find('tr')
            counter=0
            for tr in trs:
                if(counter==0):
                    print("EV yield")
                    
                elif(counter==1):
                    print("Catch rate")
                    
                elif(counter==2):
                    print("Base Friendship")
                    
                elif(counter==3): 
                    print("Base Exp.")
                    
                elif(counter==4):
                    print("Growth Rate")
                    
                    
            
        elif (j==2):
            #getting breeding data
            print("breeding")
            tr=table.find('tr')
            counter=0
             for tr in trs:
                if(counter==0):
                    print("Egg Groups")
                    
                elif(counter==1):
                    print("Gender")
                    
                elif(counter==2):
                    print("Egg cycles")
                    
                
            
            
            
            
        else:
            break
        j=j+1
    
















