import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='selenium_test.log',  # Output to file
    filemode='w'  # Overwrite file each run
)

logger = logging.getLogger('selenium_tests')


class TestData:

    def load_credentials():
        return {
            'valid': ('tomsmith', 'SuperSecretPassword!'),
            'invalid_username': ('Tomsmith', 'SuperSecretPassword!'),
            'invalid_password': ('tomsmith', 'SuperSecretPassword'),
            'empty': ('', '')
        }


class LoginTest:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'https://the-internet.herokuapp.com/login'
        self.credentials = TestData.load_credentials()
        self.wait = WebDriverWait(self.driver, 10)

    def run_webpage(self, base_url):
        self.driver.get(base_url)
        logger.info(f"Going to Webpage {base_url}")
        

    def login_using_credentials(self, username, password):
        # locators
        username_field = (By.ID, 'username')
        password_field = (By.ID, "password")
        login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash_message = (By.CSS_SELECTOR, ".flash")
        self.success_message = (By.CSS_SELECTOR, ".flash.success")
        self.error_message = (By.CSS_SELECTOR, ".flash.error")

        username_field.clear()
        logger.info('Clearing the Username Field')
        username_field.send_keys(username)
        logger.info(f'Sending Keys {username} to Username Field')

        password_field.clear()
        logger.info('Clearing the Password Field')
        password_field.send_keys(password)
        logger.info(f'Sending Keys {password} to Password Field')

        login_button.click()
        logger.info('Clicked Login button...')

    def test_valid_login(self):
        username, password = self.credentials['valid']
        self.login_using_credentials(username, password)
        logger.info('Expected Result: Login Successful')

    def test_invalid_username(self):
        username, password = self.credentials['invalid_username']
        self.login_using_credentials(username, password)
        logger.info('Expected Result: Login Unsuccessful')

    def test_invalid_password(self):
        username, password = self.credentials['invalid_password']
        self.login_using_credentials(username, password)
        logger.info('Expected Result: Login Unsuccessful')