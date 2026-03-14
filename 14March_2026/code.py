from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()


driver.get('https://www.amazon.in/')
sleep(3)

driver.get('https://www.myntra.com/')
sleep(3)


driver.quit()