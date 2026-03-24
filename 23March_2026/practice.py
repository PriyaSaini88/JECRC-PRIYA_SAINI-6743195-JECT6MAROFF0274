from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://demoqa.com/droppable')
driver.maximize_window()
action = ActionChains(driver)
sleep(3)

## task1
# origin_ele = driver.find_element(By.ID, 'draggable')
# target_ele = driver.find_element(By.ID, 'droppable')
#
# action.drag_and_drop(origin_ele, target_ele).perform()
# sleep(10)
#
# assert 'Dropped!' == target_ele.text, 'not changed!'
# print('drag and drop done!')

## task2
button = driver.find_element(By.ID, 'droppableExample-tab-preventPropogation').click()
sleep(5)
drag = driver.find_element(By.ID, 'dragBox')
outer_drop1 = driver.find_element(By.XPATH, '//p[text() = "Outer droppable"]')
action.drag_and_drop(drag, outer_drop1).perform()
sleep(5)

inner_drop1 = driver.find_element(By.ID, 'notGreedyInnerDropBox')
action.drag_and_drop(drag, inner_drop1).perform()
sleep(5)

outer_drop2 = driver.find_element(By.XPATH, '//div[@id = "greedyDropBox"]/descendant::p')
action.drag_and_drop(drag, outer_drop2).perform()
sleep(5)

inner_drop2 = driver.find_element(By.ID, 'greedyDropBoxInner')
action.drag_and_drop(drag, inner_drop2).perform()
sleep(5)






driver.quit()