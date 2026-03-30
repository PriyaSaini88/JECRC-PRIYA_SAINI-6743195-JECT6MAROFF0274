from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
sleep(2)

# parent_window = driver.current_window_handle
# print(parent_window)
## current_window_handle --> will give address of current window

# driver.find_element(By.XPATH, '//a[text() = "Click Here"]').click()
# sleep(2)
#
# all_windows = driver.window_handles
## window_handles--> will return list of all the windows present after the click (including the original one)
## we switch to other windows using indexing in that List and the index = 0 will be parent window
## and index = -1 will be the most recent window

# print(len(all_windows))
#
# driver.switch_to.window(all_windows[-1])
#
# print(driver.current_window_handle)

# print(driver.find_element(By.CLASS_NAME, 'example').text)

# assert 'New' in driver.find_element(By.CLASS_NAME, 'example').text
# driver.close()
# driver.switch_to.window(parent_window)
# print(driver.find_element(By.CLASS_NAME, 'example').text)
# sleep(2)



## opening a website in the new window
driver.switch_to.new_window('window')
sleep(3)
driver.get('https://www.cricbuzz.com/')



driver.quit()