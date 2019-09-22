import user_agent
import requests
import lxml
from bs4 import BeautifulSoup
from argparse import ArgumentParser
from urllib.parse import unquote


parser = ArgumentParser()
parser.add_argument('-s', '--search', type=str, nargs='+')
parser.add_argument('-p', '--pages', type=int)
entry = parser.parse_args().search
pages = parser.parse_args().pages


USER_AGENT = user_agent.generate_user_agent()
url = 'https://spb.hh.ru/search/vacancy?only_with_salary=true&area=2&st=searchVacancy&text='


vacancies = []
salaries = []
links = []
for page in range(pages):
    response = requests.get(f'{url}{entry}&page={page}', headers={'User-Agent': USER_AGENT})
    soup = BeautifulSoup(response.text, features='lxml')
    for itm in soup.find_all('a', class_='bloko-link HH-LinkModifier'):
        vacancies.append(itm.text)
        links.append(itm['href'])
    for salary in soup.find_all('div', class_='vacancy-serp-item__compensation'):
        salaries.append(salary.text)


salaries = [salary.replace('\xa0', ' ') for salary in salaries]
links = [unquote(link) for link in links]
print(vacancies)
print(salaries)
print(links)

