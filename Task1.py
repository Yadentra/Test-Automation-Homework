from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://masterschool.com")
time.sleep(2)  # Wait for 2 seconds

# Find and click "Browse Programs" link
browse_programs = driver.find_element(By.LINK_TEXT, "Browse Programs")
browse_programs.click()
time.sleep(2)  # Wait for 2 seconds

# Quit the driver
driver.quit()