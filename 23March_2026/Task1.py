from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get('https://www.chennaisuperkings.com/')
driver.maximize_window()

action  = ActionChains(driver)

mat_henry = driver.find_element(By.XPATH, '(//div[@class = "row lions-carousel pb-3"]/descendant::img)[5]')
action.scroll_to_element(mat_henry).perform()
sleep(5)

for i in range(5):
    action.send_keys(Keys.PAGE_UP).perform()
    sleep(3)

sleep(2)

driver.quit()