from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
sleep(2)

## Simple alert
# driver.find_element(By.XPATH, '//button[@onclick = "jsAlert()"]').click()
# sleep(3)
# # switch_to --> to switch to the particular alert
# alert = driver.switch_to.alert
# alert.accept()
# sleep(3)

## Confirmation alert
# driver.find_element(By.XPATH, '//button[@onclick = "jsConfirm()"]').click()
# sleep(3)
# alert = driver.switch_to.alert
# # alert.accept()  ## to accept the alert
# alert.dismiss()
# sleep(3)

## Prompt Alert
# driver.find_element(By.XPATH, '//button[@onclick = "jsPrompt()"]').click()
# sleep(3)
# alert = driver.switch_to.alert
# alert.send_keys("hellooo")
# sleep(3)
# # alert.accept()
# alert.dismiss()
# sleep(3)

wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH, '//button[@onclick = "jsAlert()"]').click()
alert = wait.until(EC.alert_is_present())

alert.accept()
sleep(2)

driver.quit()