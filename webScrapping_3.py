from logging import exception
from typing import Text
from bs4 import BeautifulSoup
import requests
# import json
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin123",
  database="CrickDB"
)

mycursor = mydb.cursor()





# sql = "TRUNCATE TABLE cricketers"

# mycursor.execute(sql)
# print("Table Truncted")
mycursor.execute("TRUNCATE TABLE cricketers")
# mycursor.execute("DELETE FROM cricketers")

mydb.commit()
# mycursor = mydb.cursor()
# mycursor.execute("SHOW TABLES")
html_text = requests.get('https://stats.espncricinfo.com/ci/content/records/223646.html').text
soup = BeautifulSoup(html_text, 'lxml')
series = soup.find('tbody')
data = series.find_all('tr', class_ = 'data1')

# print(data)


for x in data:
    try:
        try2 = x.find_all('td', class_='left')
        # print(try2)
        print('================================')
        # name = x.find('a' , class_='data-link').text
        # # print("Nme : ",name)
        year = x.find_all('td')
        # # print("YY : ",year)
        l1 = []
        for a in year:
            l1.append(a.text)

        sql = "INSERT INTO cricketers (player, Span, mat, Inns, NO, Runs, HS, Ave, Hundreds, fiftys, Zeor) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (l1[0], l1[1], l1[2], l1[3], l1[4], l1[5], l1[6], l1[7], l1[8], l1[9], l1[10])
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

        print(l1)

    except exception as e:
        print(e)
    
print("Done Succesfully")
mydb.close()