import logging
import pytest
import yaml
from request import get_posts, get_my_posts, get_username

with open('testdata.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_api_step_1(get_token):
    logging.info('Test API 1 started')
    output = get_posts(get_token)['data']
    res = []
    for item in output:
        res.append(item['title'])
    assert data.get('title') in res


def test_api_step_2(get_token, new_post):
    logging.info('Test API 2 started')
    output = get_my_posts(get_token)['data']
    res = []
    for item in output:
        res.append(item['title'])
    assert new_post in res


def test_api_step_3(get_token):
    output = get_username(get_token)
    assert output['username'] == data.get('login')


if __name__ == '__main__':
    pytest.main(['-vv'])
