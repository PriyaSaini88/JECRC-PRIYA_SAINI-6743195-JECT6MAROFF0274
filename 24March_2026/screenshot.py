import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

folder = os.path.join(os.getcwd(), 'screenshots') ## set the path for the folder, it will get the current working directory(the method we use inside join is os.getcwd() for current path) and it will join the folder name to it
os.makedirs(folder, exist_ok=True)

driver = webdriver.Chrome()
driver.get('https://in.pinterest.com/')
driver.maximize_window()
action = ActionChains(driver)
sleep(3)

## save_screenshot() --> to take screenshot of full page, it will take folder path and file name with .png
# driver.save_screenshot(f'{folder}/full_page.png')
# sleep(4)

# ele = driver.find_element(By.XPATH, '(//div[@class = "ADXRXN AsRsEE"])[3]/descendant::img')
ele = driver.find_element(By.XPATH, "//img[contains(@alt, 'Photo of a woman in a cherry-patterned')]")
sleep(2)
## screenshot() --> to take screenshot of a particular element

ele.screenshot(f'{folder}/cherry_red.png')
sleep(2)


driver.quit()
