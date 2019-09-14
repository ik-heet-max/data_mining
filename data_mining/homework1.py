import requests
import json
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-n', '--name', type=str)

arg = parser.parse_args()


# user_agent = 'ik-heet-max'
url = "https://api.github.com/users/"
username = arg.name
repos = '/repos'

resp = requests.get(f'{url}{username}{repos}')
repo_list = []

for item in resp.json():
    repo_list.append(item.get('name'))

with open('repos.txt', 'w') as file:
    json.dump(repo_list, file)
