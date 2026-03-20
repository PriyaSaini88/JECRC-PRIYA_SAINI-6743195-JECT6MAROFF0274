from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/upload')
# driver.maximize_window()

# choose_file = driver.find_element(By.ID, 'file-upload')
# choose_file.send_keys(r" C:\Users\nitin\Downloads\task_css.jpeg")
#
# submit = driver.find_element(By.ID, 'file-submit')
# submit.click()
# sleep(5)

###################

driver.get('https://the-internet.herokuapp.com/download')
driver.maximize_window()
driver.find_element(By.XPATH, "//a[text() = 'Screenshot 2025-12-24 164603.png']").click()
sleep(10)

print('Downloaded')

driver.quit()
