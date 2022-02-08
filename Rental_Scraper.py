#Importing Libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Get URL content
url = 'https://www.your-move.co.uk/properties-to-rent/london/!/bedrooms/2/type/1,2/page/2#property_1528444471'
page = requests.get(url)
scrape = BeautifulSoup(page.content,'html5lib')

#Now extracting different tags 
page_contents = scrape.find_all('div',class_="list_item property rental single_image")

#Loop to iterate to each housing section/div
#Also creating arrays to store data in and then export it to excel file
title=[]
loc=[]
price=[]
deposit=[]
available_date=[]
typehouse=[]
for i in page_contents:
    house_type = i.find('div',class_="prop-list-head prop-list-head-lettings").text.split(",",2)
    type=house_type[0]
    date=house_type[1].split(" ")
    only_date=date[2].replace('.','')
    
    house_deposit = i.find('span',class_="deposit").text
    house_price = i.find('div',class_="prop-list-head-price").text
    house_title = i.find('div',class_="prop-list-body-blurb col-md-12").text
    house_location = i.find('div',class_="prop-list-body-address col-md-12").text
    
    #Appending to array
    title.append(house_title)
    loc.append(house_location)
    typehouse.append(type)
    deposit.append(house_deposit)
    price.append(house_price)
    available_date.append(only_date)

#Dataframe
df=pd.DataFrame({'Title':title, 'Location':loc, 'Type':typehouse, 'Date Available':available_date,'Deposit Price':deposit,'Price of house':price})
df.to_excel('D:/Salman/Data Analyst/Web_Scraping/UK_House_rental.xlsx',encoding='utf8',index=False)