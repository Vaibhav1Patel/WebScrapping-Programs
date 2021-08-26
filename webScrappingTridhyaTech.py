from bs4 import BeautifulSoup
import requests
import json
from xlwt import Workbook
import xlsxwriter
import os
  
# check if file exists
if os.path.exists("company_Employee_details.json"):
    os.remove("company_Employee_details.json")
  
    # Print the statement once
    # the file is deleted 
    print("File deleted !") 

# WorkBook
workbook = xlsxwriter.Workbook('Company_Employee_Details.xlsx')
worksheet = workbook.add_worksheet()
row = 1
col = 1
worksheet.set_column('A:A', 20)
worksheet.set_column('B:B', 40)

# WEBSITE DATA FETCHING

html_text = requests.get('https://www.tridhya.com/company/team/').text
soup = BeautifulSoup(html_text, 'lxml')
profs = soup.find_all('div', class_ = 'col-sm-6 col-md-3 profile-card-main')
for x in profs:
    employee_name = x.find('span').text
    employee_job = x.find('h2', class_ ='profile-title').text
    print(f'''Employee Name : {employee_name}
Employee Job : {employee_job}

''')     
    employee_img = x.find('img')
    try:
        response = requests.get(employee_img['src'])
        file = open(f"Images/{employee_name}.png", "wb")
        file. write(response.content) 
    except:
        print(f"Image of {employee_name} not exists")
    
    #JSON Importing dETAILS

    empl = {
        "employee_name":employee_name,
        "employee_job" : employee_job

    }
    with open("company_Employee_details.json","a") as write_file:  
        json.dump(empl,write_file) 
        write_file.write("\n")


    #Excel sheet Entries
    try:
        

        worksheet.write(f'A{row}', employee_name)
        worksheet.write(f'B{row}', employee_job)
        
        row+=1
    except:
        workbook.close()
        print("Error Occur In : ",employee_name)
        print("------------------------------------------------------")

print("SuccesFully COMPLETED")
workbook.close()