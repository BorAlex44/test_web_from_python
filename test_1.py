import time
import pytest
import yaml

with open('testdata.yaml') as file:
    test_data = yaml.safe_load(file)


def test_step1(site, select_input_login, select_input_password, select_click_button, select_error_401):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys('test')
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys('test')
    btn = site.find_element('css', select_click_button)
    btn.click()
    err_label = site.find_element('xpath', select_error_401)
    assert err_label.text == '401'


def test_step2(site, select_input_login, select_input_password, select_click_button, select_hello_user):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(test_data.get('login'))
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(test_data.get('password'))
    btn = site.find_element('css', select_click_button)
    btn.click()
    result = site.find_element('xpath', select_hello_user)
    assert result.text == f'Hello, {test_data.get("login")}'


def test_step3(site, login_user, select_create_post, select_test_post_title, select_save_post, select_button_home,
               select_save_test_post):
    time.sleep(test_data.get('sleep_time'))
    btn_create_post = site.find_element('xpath', select_create_post)
    btn_create_post.click()
    time.sleep(test_data.get('sleep_time'))
    input_title = site.find_element('xpath', select_test_post_title)
    input_title.send_keys(test_data.get('title_test_post'))
    save_post = site.find_element('xpath', select_save_post)
    save_post.click()
    time.sleep(test_data.get('sleep_time'))
    btn_home = site.find_element('xpath', select_button_home)
    btn_home.click()
    time.sleep(test_data.get('sleep_time'))
    result = site.find_element('xpath', select_save_test_post)
    assert result.text == f'{test_data.get("title_test_post")}'


if __name__ == '__main__':
    pytest.main(['-vv'])
