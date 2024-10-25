from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open LinkedIn
driver.get("https://www.linkedin.com/login")
time.sleep(2)  # Wait for the page to load

# Find username and password fields, enter credentials
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("yadentra@gmail.com")  # Replace with your email
password.send_keys("Hdao@2023")  # Replace with your password

# Find and click the "Sign in" button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(2)  # Wait for 2 seconds to ensure login

# Quit the driver
driver.quit()