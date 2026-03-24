from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get('https://www.myntra.com/')
driver.maximize_window()


action  = ActionChains(driver)

women = driver.find_element(By.XPATH, '(//div[@class = "desktop-navLink"]/descendant::a[@class = "desktop-main"])[2]')
sleep(2)
action.move_to_element(women).perform()
sleep(2)

category = driver.find_element(By.XPATH, '//div[@class = "desktop-categoryContainer"]/descendant::li[@data-reactid="189"]').click()
sleep(4)

fifth_row = driver.find_element(By.XPATH, '//ul[@class = "results-base"]/descendant::li[30]')
sleep(2)
action.scroll_to_element(fifth_row).perform()
sleep(3)

driver.quit()





