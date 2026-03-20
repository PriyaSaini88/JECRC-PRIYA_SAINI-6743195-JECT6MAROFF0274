from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://qavbox.github.io/demo/signup/')
driver.maximize_window()

wait = WebDriverWait(driver, 10)

name = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="username"]')))
name.send_keys("Priya")

email = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="email"]')))
email.send_keys("abc@gmail.com")

phone_no = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="tel"]')))
phone_no.send_keys("9876543210")

fax = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@id="fax"]')))
if fax.is_enabled():
    fax.send_keys("987654321")

upload_file = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="datafile"]')))
upload_file.send_keys(r"C:\Users\nitin\Downloads\task2.jpeg")

gender = wait.until(EC.element_to_be_clickable((By.XPATH, '//select[@name = "sgender"]')))
select_gender = Select(gender)
select_gender.select_by_value("female")

experience = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value = "one"]')))
experience.click()

skill1 = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value = "automationtesting"]')))
skill1.click()

skill2 = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value = "testng"]')))
skill2.click()

tools = wait.until(EC.element_to_be_clickable((By.XPATH, '//option[@value = "selenium"]')))
tools.click()

submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id = "submit"]')))
submit.click()

driver.quit()