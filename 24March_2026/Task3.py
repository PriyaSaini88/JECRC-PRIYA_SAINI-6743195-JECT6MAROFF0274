from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demoqa.com/browser-windows')
driver.maximize_window()
sleep(2)

main_window = driver.current_window_handle
sleep(2)
## New Tab
driver.find_element(By.ID, 'tabButton').click()
sleep(2)
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
sleep(2)

assert "sample page" in driver.find_element(By.ID, 'sampleHeading').text, 'not present!'
print('Worked!')

driver.close()
driver.switch_to.window(main_window)
## New Window
driver.find_element(By.ID, 'windowButton').click()
sleep(2)
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
sleep(2)

assert "sample page" in driver.find_element(By.ID, 'sampleHeading').text, 'not present!'
print('Worked!')

driver.close()
driver.switch_to.window(main_window)

## New Window Message
driver.find_element(By.ID, 'messageWindowButton').click()
sleep(2)
all_windows = driver.window_handles
driver.switch_to.window(all_windows[-1])
sleep(2)

driver.close()
driver.switch_to.window(main_window)
sleep(2)

driver.quit()