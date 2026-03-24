## ActionChains is a class that contains methods for keyboard and mouse actions

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

## drag and drop

driver = webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/drag_and_drop')
# driver.maximize_window()
# sleep(2)
#
# action = ActionChains(driver)
#
# origin_ele = driver.find_element(By.ID, "column-a")
# target_ele = driver.find_element(By.ID, "column-b")
#
# action.drag_and_drop(origin_ele, target_ele).perform()
# sleep(4)

## Mouse Hover

driver.get('https://supertails.com')
driver.maximize_window()

action = ActionChains(driver)

dog = driver.find_element(By.XPATH, '//span[contains(text(),"Dogs")]')
sleep(2)
action.move_to_element(dog).perform()
sleep(4)


driver.quit()





