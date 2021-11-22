import requests
from bs4 import BeautifulSoup
import json


# URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
# res = requests.get(URL)
# soup = BeautifulSoup(res.content, 'html.parser')
# results_div = soup.find_all('sup', class_="noprint")
# print(len(results_div))
# for text in results_div:
#     parent = text.parent.get_text().strip()
#     print(parent)

def get_citations_needed_count(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    results_div = soup.find_all('sup', class_="noprint")
    return(len(results_div))
print(get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_the_Ottoman_Empire'))

def get_citations_needed_report(url):
    all_jobs_object = []
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    results_div = soup.find_all('sup', class_="noprint")
    for text in results_div:
        job_dict = {'paragraph':''}
        parent = text.parent.get_text().strip()
        job_dict['paragraph'] = parent
        all_jobs_object.append(job_dict)
    print(all_jobs_object)
    with open('all_jobs.json', 'w') as f:
        content = json.dumps(all_jobs_object)
        f.write(content)
get_citations_needed_report('https://en.wikipedia.org/wiki/History_of_the_Ottoman_Empire')