from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get('https://codepen.io/gdw96/pen/jOypoYL')
driver.maximize_window()

action = ActionChains(driver)

iframe = driver.find_element(By.ID, "result")
driver.switch_to.frame(iframe)
sleep(2)

uname = driver.find_element(By.ID,'username')
uname.clear()
uname.send_keys("skdj")
sleep(2)

passwd = driver.find_element(By.ID,'password')
passwd.clear()
passwd.send_keys("abcdef")
sleep(2)

show_passwd = driver.find_element(By.ID,'showPsswd')
action.click_and_hold(show_passwd).perform()
sleep(2)
action.release().perform()
sleep(2)

register_btn = driver.find_element(By.XPATH, '//input[@type = "submit"]')
register_btn.click()
sleep(2)

driver.back()
sleep(3)

driver.switch_to.frame(iframe)
assert "Registration" in driver.find_element(By.XPATH, '//div[@class = "container"]').text, 'not found!'
print('Found!')


driver.quit()



