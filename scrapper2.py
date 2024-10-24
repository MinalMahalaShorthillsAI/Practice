from  bs4 import BeautifulSoup
import requests
import time
print('Put some skills you are not familiar with')

unfamiliar_skill=input('>')

print(f"filtering out {unfamiliar_skill}")

def find_jobs():

    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text

    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        job_status=job.find('span', class_='sim-posted').text
        if  'few' in job_status:
            company_name=job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')

            skills = job.find('span', class_='srp-skills').text

            more_info=job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f'''Company Name: {company_name}Required Skills: {skills}job_status: {job_status}More info: {more_info}''')
                
                print(f"files saved: {index}")
                
#print(job_status)
if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=1
        print(f'waiting {time_wait} minutes....')
        time.sleep(time_wait*60)
