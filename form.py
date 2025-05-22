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


driver = webdriver.Firefox()
driver.get('https://the-internet.herokuapp.com/login')

wait = WebDriverWait(driver, 10)

driver.maximize_window()

# Find the username and password fields
username = driver.find_element(By.XPATH, '//*[@id="username"]')
password = driver.find_element(By.XPATH, '//*[@id="password"]')

username.send_keys('tomsmith')
time.sleep(2) 
password.send_keys('SuperSecretPassword!')
time.sleep(2) 

loginButton = driver.find_element(By.XPATH, '//*[@id="login"]/button')
loginButton.click()


try:
	# Take a screenshot and save it as 'screenshot.png'
	driver.find_element(By.CSS_SELECTOR, '.flash.success')
	logger.info("Login Successful")
	driver.save_full_page_screenshot('login-success.png')
except Exception as e:
	logger.error(f"Login Unsuccessful: {str(e)}")
	driver.save_full_page_screenshot('login-failed.png')
	raise
finally:
	driver.quit()
	logger.info('Browser Closed')

