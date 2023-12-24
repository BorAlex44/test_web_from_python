import time
import pytest
import logging
import yaml
from testpage import OperationsHelper
from request import get_posts, get_my_posts

with open('testdata.yaml') as file:
    test_data = yaml.safe_load(file)


def test_step_1(browser):
    logging.info('Test-1  starting')
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login('test')
    test_page.enter_pass('test')
    test_page.click_login_button()
    assert test_page.get_error_text() == '401'


def test_step_2(browser):
    logging.info('Test-2 starting')
    test_page = OperationsHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(test_data.get('login'))
    test_page.enter_pass(test_data.get('password'))
    test_page.click_login_button()
    time.sleep(test_data.get('sleep_time'))
    assert test_page.select_hello_user() == f'Hello, {test_data.get("login")}'


def test_step_3(browser):
    logging.info("Test-3 starting")
    test_page = OperationsHelper(browser)
    test_page.click_create_button()
    time.sleep(test_data.get('sleep_time'))
    test_page.create_post_title(test_data.get('new_post_title'))
    test_page.create_post_description(test_data.get('new_post_description'))
    test_page.create_post_content(test_data.get('new_post_content'))
    test_page.click_create_post_button()
    time.sleep(test_data.get('sleep_time'))
    test_page.click_home_button()
    assert test_page.get_res_create_text() == test_data.get('new_post_title')


def test_step_4(browser):
    logging.info('Test-4 starting')
    test_page = OperationsHelper(browser)
    test_page.click_contact_button()
    test_page.enter_your_name_to_contact_field(test_data.get('name_to_contact'))
    test_page.enter_your_email_to_contact_field(test_data.get('email_to_contact'))
    test_page.enter_content_to_contact_field('Content from contact')
    test_page.click_contact_us_button()
    time.sleep(test_data.get('sleep_time'))
    assert test_page.alert() == 'Form successfully submitted'


if __name__ == '__main__':
    pytest.main(['-vv'])
