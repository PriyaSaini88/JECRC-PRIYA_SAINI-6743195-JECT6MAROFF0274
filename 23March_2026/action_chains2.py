from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.devtools.v143.fed_cm import click_dialog_button

# driver = webdriver.Chrome()
#
# driver.get('https://supertails.com')
# driver.maximize_window()
#
# action = ActionChains(driver)
# sleep(3)
#
# catt = driver.find_element(By.XPATH, '//div[@data-ganame = "Breed 5"]')
# action.scroll_to_element(catt).perform()
# sleep(5)
## SCROLL TO : it will scroll to the particular pixel or element
## SCROLL BY : it will scroll from the current position to the given value
## Scroll top = negative value
## Scroll down = positive value

# action.scroll_by_amount(0,+1500).perform()
# sleep(5)
#
# action.scroll_by_amount(0,+500).perform()
# sleep(5)

# click -- left click
# context_click -- right click
# double_click -- double click

## keyboard actions
# driver = webdriver.Chrome()
# driver.get('https://supertails.com/')
# driver.maximize_window()
# action = ActionChains(driver)
#
# action.send_keys(Keys.PAGE_DOWN).perform()  ## it will scroll down 100 px
# sleep(5)
#
# action.send_keys(Keys.PAGE_UP).perform()  ## it will scroll up 100 px
# sleep(5)
#
# action.key_down(Keys.CONTROL).send_keys('a').perform()  # key press
# sleep(2)
# action.key_up(Keys.CONTROL).perform()  # key release
# sleep(2)


## copying and pasting for address fields

# driver = webdriver.Chrome()
# driver.get(r'C:\Users\nitin\OneDrive\Desktop\PythonProject\JECRC\23March_2026\address_fields.html')
# driver.maximize_window()
# action = ActionChains(driver)
#
# present = driver.find_element(By.ID, 'presentAddress')
# permanent = driver.find_element(By.ID, 'permanentAddress')
# present.send_keys('JECRC, JAIPUR, RJ')
# sleep(2)
# present.click()
# action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# sleep(2)
# action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# permanent.click()
# sleep(3)
# action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
#
# sleep(5)

driver = webdriver.Chrome()
driver.get(r'C:\Users\nitin\OneDrive\Desktop\PythonProject\JECRC\23March_2026\index1.html')
driver.maximize_window()
action = ActionChains(driver)

passwd = driver.find_element(By.ID,'password')
passwd.send_keys("skdjsk")
sleep(4)
show_passwd = driver.find_element(By.ID,'eyeBtn')
action.click_and_hold(show_passwd).perform()
sleep(2)
action.release().perform()
sleep(5)

driver.quit()


