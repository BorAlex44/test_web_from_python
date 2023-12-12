import pytest
import yaml
from request import get_posts, get_my_posts

with open('config.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_step1(get_token):
    output = get_posts(get_token)['data']
    res = []
    for item in output:
        res.append(item['title'])
    assert data.get('title') in res


def test_step2(get_token, new_post):
    output = get_my_posts(get_token)['data']
    res = []
    for item in output:
        res.append(item['title'])
    assert new_post in res


if __name__ == '__main__':
    pytest.main(['-vv'])
