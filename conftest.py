import pytest
import requests
import yaml

with open('config.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


@pytest.fixture()
def get_token():
    post = requests.post(url=data.get('path'),
                         data={'username': data.get('username'), 'password': data.get('password')})
    if post.status_code == 200:
        token = post.json()['token']
        return token


@pytest.fixture()
def new_post(get_token):
    post = requests.post(url=data.get('url'), headers={'X-Auth-Token': get_token},
                         data={'username': data.get('username'),
                               'password': data.get('password'),
                               'title': 'new_test_title',
                               'description': 'new_test_description',
                               'content': 'new_test_content'})
    if post.status_code == 200:
        return post.json()['title']
