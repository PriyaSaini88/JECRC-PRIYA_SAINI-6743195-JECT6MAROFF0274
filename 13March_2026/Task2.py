from selenium import webdriver
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()

uname = driver.find_element(By.XPATH, '//input[@name="username"]')
print('working fine for username!')

pwd = driver.find_element(By.XPATH, '//input[@id="password"]')
print('working fine for password!')

login = driver.find_element(By.XPATH, '//button[@type="submit"]')
print('working fine for login!')

ele_selenium = driver.find_element(By.XPATH, '//a[text()="Elemental Selenium"]')
print('working fine for elemental selenium!')

login_page = driver.find_element(By.XPATH, '//h2[contains(text(),"Login Page")]')
print('working fine for heading!')

driver.quit()