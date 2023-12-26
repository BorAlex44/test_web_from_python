import logging

import pytest
import yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open('testdata.yaml') as file:
    test_data = yaml.safe_load(file)
    test_browser = test_data.get('browser')


@pytest.fixture(scope='session')
def browser():
    if test_browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def get_token():
    post = requests.post(url=test_data.get('path'),
                         data={'username': test_data.get('login'), 'password': test_data.get('password')})
    if post.status_code == 200:
        token = post.json()['token']
        logging.debug(f'Received token {token}')
        return token
    else:
        logging.error('error receiving token')
        return None


@pytest.fixture()
def new_post(get_token):
    post = requests.post(url=test_data.get('url'), headers={'X-Auth-Token': get_token},
                         data={'username': test_data.get('login'),
                               'password': test_data.get('password'),
                               'title': 'new_test_title',
                               'description': 'new_test_description',
                               'content': 'new_test_content'})
    logging.debug(f'Create post with title: new_test_title, description: new_test_description, '
                  f'content: new_test_content')
    if post.status_code == 200:
        return post.json()['title']
    else:
        logging.error('error find post')
        return None


@pytest.fixture()
def site():
    site = test_data.get('address')
    return site
