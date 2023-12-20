import yaml
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

with open('testdata.yaml') as file:
    test_data = yaml.safe_load(file)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = test_data.get('address')

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        return element.value_of_css_property(property)

    def go_to_site(self):
        return self.driver.get(self.base_url)
