import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import subprocess
import os
import csv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='selenium_test_v2.log',  # Output to file
    filemode='w'  # Overwrite file each run
)

logger = logging.getLogger('selenium_tests')


class LoginTest:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.base_url = 'https://the-internet.herokuapp.com/login'
        self.credentials = self.read_data_from_csv('C:/Users/Esterlin/VSCodeProjects/Selenium-Python/test_data/test_data.csv')
        self.wait = WebDriverWait(self.driver, 10)

    def read_data_from_csv(self, filename):
        # create an empty list
        datalist = []

        # open csv file
        csvdata = open(filename, "r")

        # create csv reader
        reader = csv.reader(csvdata)
        
        #skip header 
        next(reader)

        # add csv rows to list
        for rows in reader:
            datalist.append(rows)
        return datalist

    def run_webpage(self, base_url):
        self.driver.get(base_url)
        logger.info(f"Going to Webpage {base_url}")
        

    def login_using_credentials(self, username, password, testNumber):

        self.run_webpage(self.base_url)

        # locators
        username_field = self.wait.until(
                EC.presence_of_element_located((By.ID, 'username'))
            )
        username_field.clear()
        logger.info('Clearing the Username Field')
        username_field.send_keys(username)
        logger.info(f'Sending Keys {username} to Username Field')

        password_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "password"))
            )
        
        password_field.clear()
        logger.info('Clearing the Password Field')
        password_field.send_keys(password)
        logger.info(f'Sending Keys {password} to Password Field')

        login_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )

        login_button.click()
        logger.info('Clicked Login button...')

        time.sleep(2)

        result = self.check_success(testNumber)
        return result

    
    def check_success(self, testNumber):
        version = self.get_latest_git_tag()

        screenshot_folder = os.path.join('screenshots', version)
        os.makedirs(screenshot_folder, exist_ok=True)

        try:
            # Wait for flash message to appear
            flash_element = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".flash"))
            )
            
            # Check if it's success or error
            if "success" in flash_element.get_attribute("class"):
                logger.info('Login was Successful')
                screenshot_name = f'login-success-{testNumber}.png'
                result = "SUCCESS"
            else:
                logger.error('Login was Unsuccessful')
                screenshot_name = f'login-failed-{testNumber}.png'
                result = "FAILED"
                
            # Take screenshot with descriptive name
            # Full path to save screenshot
            screenshot_path = os.path.join(screenshot_folder, screenshot_name)
            self.driver.save_screenshot(screenshot_path)
            logger.info(f'Screenshot saved as: {screenshot_path}')
            
            # Log the flash message content
            flash_text = flash_element.text
            logger.info(f'Flash message: {flash_text}')
            
            return result
            
        except Exception as e:
            logger.error(f'Error checking login result: {str(e)}')
            screenshot_name = f'login-error-.png'
            self.driver.save_screenshot(screenshot_name)
            return "ERROR"
        
    def run_all_tests(self, credentials):
        """Run all login tests"""
        test_results = {}
        
        try:
            count = 1
            for username, password in credentials:
                test_results[count] = self.login_using_credentials(username, password, count)
                count += 1
            # Summary
            logger.info('=== TEST SUMMARY ===')
            for test_name, result in test_results.items():
                logger.info(f'{test_name}: {result}')
                
        except Exception as e:
            logger.error(f'Error during test execution: {str(e)}')
        finally:
            self.cleanup()
            
        return test_results

    def cleanup(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()
            logger.info('Browser closed')
    @staticmethod
    def get_latest_git_tag():
        try:
            return subprocess.check_output(['git', 'describe', '--tags', '--abbrev=0']).decode('utf-8').strip()
        except Exception:
            return "v0.0.0"

if __name__ == "__main__":
    test_runner = LoginTest()
    results = test_runner.run_all_tests(test_runner.credentials)