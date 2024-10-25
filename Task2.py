from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search bar, enter "cats"
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("cats")
time.sleep(3)  # Wait for 3 seconds

# Print the page title
print(driver.title)

# Quit the driver
driver.quit()