import logging
from BaseApp import BasePage
from selenium.webdriver.common.by import By

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PASS_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    LOCATOR_CONTACT_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')
    LOCATOR_CONTACT_YOUR_NAME_FIELD = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_CONTACT_YOUR_EMAIL_FIELD = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTACT_CONTENT_FIELD = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_CONTACT_US_BTN = (By.XPATH, '//*[@id="contact"]/div[4]/button')
    LOCATOR_SELECT_HELLO_USER = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CREATE_BUTTON = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[1]/button')
    LOCATOR_CREATE_TITLE = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    LOCATOR_CREATE_DESCRIPTION = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    LOCATOR_CREATE_CONTENT = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    LOCATOR_CREATE_POST_BTN = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button')
    LOCATOR_RES_CREATE = (By.XPATH, '//*[@id="app"]/main/div/div[3]/div[1]/a[1]/h2')
    LOCATOR_HOME_BTN = (By.XPATH, '//*[@id="app"]/main/nav/a/span')


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_text = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_text.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def login_valid_user(self, login, password):
        logging.info(f'Send {login} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(login)
        logging.info(f'Send {password} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(password)
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def click_contact_button(self):
        logging.info('Click contact button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()

    def enter_your_name_to_contact_field(self, name):
        logging.info(f'Send {name} to element {TestSearchLocators.LOCATOR_CONTACT_YOUR_NAME_FIELD[1]}')
        your_name_contact_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_YOUR_NAME_FIELD)
        your_name_contact_field.clear()
        your_name_contact_field.send_keys(name)

    def enter_your_email_to_contact_field(self, email):
        logging.info(f'Send {email} to element {TestSearchLocators.LOCATOR_CONTACT_YOUR_EMAIL_FIELD[1]}')
        your_email_to_contact_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_YOUR_EMAIL_FIELD)
        your_email_to_contact_field.clear()
        your_email_to_contact_field.send_keys(email)

    def enter_content_to_contact_field(self, text):
        logging.info(f'Send {text} to element {TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD[1]}')
        content_to_contact_field = self.find_element(TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD)
        content_to_contact_field.clear()
        content_to_contact_field.send_keys(text)

    def click_contact_us_button(self):
        logging.info('Click create contact_us button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def alert(self):
        logging.info('Starting alert')
        alert = self.driver.switch_to.alert
        return alert.text

    def select_hello_user(self):
        logging.info('Starting select Hello, user')
        return self.find_element(TestSearchLocators.LOCATOR_SELECT_HELLO_USER, time=3)

    def click_create_button(self):
        logging.info('Click create post button')
        self.find_element(TestSearchLocators.LOCATOR_CREATE_BUTTON).click()

    def create_post_title(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_CREATE_TITLE[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_CREATE_TITLE)
        title_field.clear()
        title_field.send_keys(word)

    def create_post_description(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_CREATE_DESCRIPTION[1]}')
        description_field = self.find_element(TestSearchLocators.LOCATOR_CREATE_DESCRIPTION)
        description_field.clear()
        description_field.send_keys(word)

    def create_post_content(self, word):
        logging.info(f'Send "{word}" to element {TestSearchLocators.LOCATOR_CREATE_CONTENT[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_CREATE_CONTENT)
        content_field.clear()
        content_field.send_keys(word)

    def click_create_post_button(self):
        logging.info('Click create post button')
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def get_res_create_text(self):
        enter_field = self.find_element(TestSearchLocators.LOCATOR_RES_CREATE, time=2)
        text = enter_field.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_RES_CREATE[1]}')
        return text

    def click_home_button(self):
        self.find_element(TestSearchLocators.LOCATOR_HOME_BTN, time=3).click()
