from typing import Text
from bs4 import BeautifulSoup
import requests
import json

html_text = requests.get('https://www.trustpilot.com/categories/furniture_store').text
soup = BeautifulSoup(html_text, 'lxml')
comps = soup.find('div', class_ = 'styles_categoryBusinessListWrapper__2H2X5')

import os
  
# check if file exists
if os.path.exists("Company_Demo_On.json"):
    os.remove("Company_Demo_On.json")
  
    # Print the statement once
    # the file is deleted 
    print("File deleted !") 
  
else:
  
    # Print if file is not present 
    print("File doesnot exist !") 


# print(comps)
for x in comps:
    # link = x.a['href']
    names = x.find('div', class_='styles_businessTitle__1IANo').text
    review = x.find('div',class_='styles_textRating__19_fv').text.replace('\u00a0\u00b7\u00a0', '   ')
    field = x.find('div', class_ = 'styles_categories__c4nU-')

    fieldtext = field.find('span').text
    # print(fieldtext)
    
    try:
        address = x.find('div', class_='styles_location__3JATO').text
        # print(address)
    except:
        # print("Address Not Available.")
        pass


    empl = {
        "Company Name : " : names,
        "Reviews : " : review,
        "Profession : " : fieldtext,
        "Address : ":address
    }
    with open("Company_Demo_On.json","a") as write_file:  
        json.dump(empl,write_file) 
        write_file.write("\n")

print("Done Successfully")