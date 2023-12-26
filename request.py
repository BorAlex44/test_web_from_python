import logging

import requests
import yaml

with open('testdata.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def get_posts(token):
    try:
        get = requests.get(url=data.get('url'), headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
    except:
        logging.exception('Exception while get request')
        get = None
    if get.status_code == 200:
        return get.json()


def get_my_posts(token):
    try:
        get = requests.get(url=data.get('url'), headers={'X-Auth-Token': token})
    except:
        logging.exception('Exception while get request')
        get = None
    if get.status_code == 200:
        return get.json()


def get_username(token):
    get = requests.get(url='https://test-stand.gb.ru/api/users/profile/20240', headers={'X-Auth-Token': token})
    return get.json()
