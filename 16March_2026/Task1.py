# OrangeHRM Login
# Automate the login flow in OrangeHRM and verify that the user successfully reaches the dashboard:
#
# Open the OrangeHRM demo website. https://opensource-demo.orangehrmlive.com/
# Get and print the title of the page.
# Locate the username input field and use clear() if needed.
# Enter the username using send_keys().
# Locate the password input field and enter the password using send_keys().
# Submit the login form using either: click() on the Login button, or Keys.ENTER
# After login, print the current URL.
# Check if dashboard is present in that url using in
# Print 'successful login'
# Test Data:
#
# Username: Admin Password: admin123

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://opensource-demo.orangehrmlive.com/')
driver.maximize_window()
sleep(3)

print(driver.title)

username = driver.find_element(By.NAME, "username")
username.clear()
username.send_keys('Admin')
sleep(2)

password = driver.find_element(By.NAME, "password")
password.clear()
password.send_keys('admin123')
sleep(2)

login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
login.click()
sleep(2)

curr_url = driver.current_url
print(curr_url)

if 'dashboard' in curr_url:
    print('Present')

print('Successful Login!')

driver.quit()