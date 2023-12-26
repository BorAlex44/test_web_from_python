import logging
import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    ids = dict()
    with open('locators.yaml') as file:
        locators = yaml.safe_load(file)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception with click')
            return False
        logging.debug(f'Clicked {element_name} button')
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
        logging.debug(f'We find text {text} in field {element_name}')
        return text

    # Enter text
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login form')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description='password form')

    def enter_your_name_to_contact_field(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_YOUR_NAME_FIELD'], word,
                                   description='name contact form')

    def enter_your_email_to_contact_field(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_YOUR_EMAIL_FIELD'], word,
                                   description='email contact form')

    def enter_content_to_contact_field(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CONTACT_CONTENT_FIELD'], word,
                                   description='content contact form')

    def create_post_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CREATE_TITLE'], word,
                                   description='title post create form')

    def create_post_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CREATE_DESCRIPTION'], word,
                                   description='description post create form')

    def create_post_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_CREATE_CONTENT'], word,
                                   description='content post create form')

    # Click
    
    def click_about_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_ABOUT_BTN'], description='about button')

    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='login button')

    def click_contact_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_BTN'], description='contact button')

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_US_BTN'], description='contact_us button')

    def click_create_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CREATE_BUTTON'], description='save post button')

    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CREATE_POST_BTN'], description='create post button')

    def click_home_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_HOME_BTN'], description='home button')

    # Get text
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description='error 401 text')

    def select_hello_user(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_SELECT_HELLO_USER'],
                                          description='hello user text')

    def get_res_create_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_RES_CREATE'],
                                          description='result create post text')

    # All
    def alert(self):
        logging.info('Get alert text')
        text = self.get_alert_text()
        logging.info(text)
        return text

    def login_valid_user(self, login, password):
        self.enter_login(login)
        self.enter_pass(password)
        self.click_login_button()

    def about_page_size(self):
        about_size = self.get_element_property(TestSearchLocators.ids['LOCATOR_ABOUT_PAGE'],
                                               'font-size')
        return about_size
