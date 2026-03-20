from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

# driver.get('https://www.lenskart.com/')
# driver.get('https://www.myntra.com/')
driver.get('https://www.lenskart.com/lenskart-mel-s18819-demi-sunglasses.html')
driver.maximize_window()
sleep(3)

## assert a keyword in python that will check if the statement is true or false. If true move on with execution else throw assertion element.
# eye_glasses = driver.find_element(By.ID, 'lrd1')
# print(eye_glasses.text)

# assert 'GLASSES' == eye_glasses.text, "didn't find"
# print('Success')

check = driver.find_element(By.XPATH, '//h4[text() = "Check"]')
sleep(3)
check.click()
sleep(2)
next_check = driver.find_element(By.XPATH, '//div[text() = "Check"]')
print(next_check.is_enabled())
sleep(2)
# check.send_keys('3033026')
# sleep(2)
# print(check.is_enabled())




# profile = driver.find_element(By.XPATH, '//span[@data-reactid = "988"]')

# assert 'Profile' == profile.text, "Didn't find Profile"
# print('Success')

driver.quit()