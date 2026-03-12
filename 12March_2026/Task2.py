# Task 2: Write a for loop for a list of browsers and open the browsers one by one.

from selenium import webdriver
from time import sleep

List1 = [webdriver.Chrome(), webdriver.Edge(), webdriver.Firefox()]

for i in List1:
    driver = i
    sleep(5)
    driver.quit()



