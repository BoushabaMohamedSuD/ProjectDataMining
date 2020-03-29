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

#print(table)

tds=table.findAll('td')

for td in tds:
    text=td.findAll()

 




