import requests
import yaml

with open('config.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def get_posts(token):
    get = requests.get(url=data.get('url'), headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
    if get.status_code == 200:
        return get.json()


def get_my_posts(token):
    get = requests.get(url=data.get('url'), headers={'X-Auth-Token': token})
    if get.status_code == 200:
        return get.json()
