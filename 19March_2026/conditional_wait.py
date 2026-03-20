from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)



## implicit wait -- driver.implicitly_wait(time in sec)
# --> can only use for driver.find_element, find element in dom structure
# --> global wait
# --> it will execute the code even if it find the element in 1st second itself that does not happen with sleep()
# -->NoSuchElementException

# driver.get('https://abc.com/')
# driver.maximize_window()

# driver.implicitly_wait(1)
#
# ele = driver.find_element(By.XPATH, '(//a[@class = "AnchorLink"]/parent::li/descendant::img)[1]')
# print(ele.get_attribute("src"))

## Explicit wait -- you can give multiple conditions
## import WebDriverWait and expected_conditions
## not global wait, it is confined to a particular element
## it takes two argument -- 1. driver 2. timeout: time
## it will wait, find element and then interact too
## it wil throw TimeoutException

# wait_obj = WebDriverWait(driver, 10)
#
# loading_circles = wait_obj.until(EC.invisibility_of_element_located((By.ID, 'preloader-animated_svg__circle3')))
#
# title_abc = driver.find_element(By.XPATH, '//span[text()="ABC SHOWS, SPECIALS & MORE"]')
#
# assert 'SPECIALS' in title_abc.text, 'the text is not present'
#
# print('working')

driver.get('https://demoqa.com/dynamic-properties')
driver.maximize_window()
#
# wait = WebDriverWait(driver, 6)
#
# enable_before = driver.find_element(By.ID, 'enableAfter')
# print(enable_before.is_enabled())
#
# enable_btn = wait.until(EC.element_to_be_clickable((By.ID, 'enableAfter')))
#
#
# if enable_btn.is_enabled():
#     enable_btn.click()
#     print(enable_btn.text)
#
# visible_ele = wait.until(EC.visibility_of_element_located((By.ID, 'visibleAfter')))
# visible_ele.click()

## never use implicit wait and explicit wait together as the seconds will get combined , the implicit wait will be for find element inside the find_element in EC.condition


driver.quit()




