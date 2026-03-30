## sometimes ui doesn't work so to solve those type of errors we use javascript executor
## it works from the backend

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://in.pinterest.com/')
driver.maximize_window()
sleep(3)

## using scroll to
## To the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)
# to the origin of the page
driver.execute_script('window.scrollTo(0, 0);')
# driver.execute_script('window.scrollTo(-5, -20);')  ##  -ve values in scrollTo will be treated as 0, 0 or origin
sleep(3)

## using scroll by
driver.execute_script('window.scrollBy(0, 800);') ## scroll 800px down
sleep(3)

driver.execute_script('window.scrollBy(0, -200);') ## scroll 200px up from the current position
sleep(3)

## scrolling to element

ele = driver.find_element(By.XPATH, "//img[contains(@alt, 'Photo of a woman in a cherry-patterned')]")
driver.execute_script('arguments[0].scrollIntoView();', ele)
sleep(3)

## clicking
click_ele = driver.find_element(By.XPATH, '//div[text() = "Join Pinterest"]')
driver.execute_script('arguments[0].click();', click_ele)
sleep(3)

driver.quit()