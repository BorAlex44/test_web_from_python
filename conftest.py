import pytest
import yaml

from module import Site

with open('testdata.yaml') as file:
    test_data = yaml.safe_load(file)


@pytest.fixture()
def select_input_login():
    return '//*[@id="login"]/div[1]/label/input'


@pytest.fixture()
def select_input_password():
    return '//*[@id="login"]/div[2]/label/input'


@pytest.fixture()
def select_click_button():
    return 'button'


@pytest.fixture()
def select_error_401():
    return '//*[@id="app"]/main/div/div/div[2]/h2'


@pytest.fixture()
def select_hello_user():
    return '//*[@id="app"]/main/nav/ul/li[3]/a'


@pytest.fixture()
def site():
    site_class = Site(test_data.get('address'))
    yield site_class
    site_class.close()


@pytest.fixture()
def login_user(site, select_input_login, select_input_password, select_click_button):
    input1 = site.find_element('xpath', select_input_login)
    input1.send_keys(test_data.get('login'))
    input2 = site.find_element('xpath', select_input_password)
    input2.send_keys(test_data.get('password'))
    btn = site.find_element('css', select_click_button)
    btn.click()


@pytest.fixture()
def select_create_post():
    return '//*[@id="create-btn"]'


@pytest.fixture()
def select_test_post_title():
    return '//*[@id="create-item"]/div/div/div[1]/div/label/input'


@pytest.fixture()
def select_test_post_description():
    return '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea'


@pytest.fixture()
def select_test_post_content():
    return '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea'


@pytest.fixture()
def select_save_post():
    return '//*[@id="create-item"]/div/div/div[7]/div/button/span'


@pytest.fixture()
def select_button_home():
    return '//*[@id="app"]/main/nav/a/span'


@pytest.fixture()
def select_save_test_post():
    return '//*[@id="app"]/main/div/div[3]/div[1]/a[1]/h2'
