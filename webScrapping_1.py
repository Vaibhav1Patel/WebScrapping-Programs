from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python+django&txtLocation=&cboWorkExp1=0').text

# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')

jobs_list = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
# jobOne = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
for jobOne in jobs_list:
    company_name = jobOne.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
    print("Company : ",company_name.replace('(MoreJobs)', '').strip())

    skills = jobOne.find('span', class_ = 'srp-skills').text.replace(' ', '')
    print("Skills Required: ",skills.strip())

    publish_dt = jobOne.find('span', class_= 'sim-posted').span.text.replace(' ', '')
    print("Publish Date : ",publish_dt.strip())

    more_info = jobOne.header.h2.a['href']
    print("More-Info : ",more_info)
    print('')
    


