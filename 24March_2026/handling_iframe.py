from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
sleep(2)

## single iframe
# iframe = driver.find_element(By.ID, 'singleframe')
# driver.switch_to.frame(iframe)
# sleep(2)
# driver.find_element(By.XPATH, '//input[@type = "text"]').send_keys('1233')
# sleep(2)

## nested iframes
driver.find_element(By.XPATH, '//a[text()= "Iframe with in an Iframe"]').click()

nested_iframe = driver.find_element(By.XPATH, '//iframe[@src = "MultipleFrames.html"]')
driver.switch_to.frame(nested_iframe)

inner_iframe  = driver.find_element(By.XPATH, '//iframe[@src = "SingleFrame.html"]')
driver.switch_to.frame(inner_iframe)

driver.find_element(By.XPATH, '//input[@type = "text"]').send_keys('1233')
sleep(2)

## switch_to.parent_frame and switch_to.default_content (default_content is the main webpage)

# driver.switch_to.parent_frame()
# print('Switched to nested iframe!')

# driver.switch_to.parent_frame()
# print('switch to parent frame')

driver.switch_to.default_content()
print('switch to main page!')

driver.quit()