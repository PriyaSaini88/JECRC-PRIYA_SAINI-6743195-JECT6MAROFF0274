from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
# opts.add_argument('--headless')  ## makes sure browser runs in headless mode i.e runs in the background not in ui

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
# driver.get('https://www.myntra.com/')
driver.maximize_window()

sleep(1)
# name = driver.find_element(By.ID, 'name')
# phone_no = driver.find_element(By.ID, 'phone')
# nav_bar = driver.find_element(By.NAME, 'Navbar')
# # radio_button = driver.find_element(By.CLASS_NAME, 'form-check-input')
#
# radio_button = driver.find_elements(By.CLASS_NAME, 'form-check-input') # if no elements found then this method return empty list
#
# inp = driver.find_elements(By.TAG_NAME, 'input')

# print(inp)
# print(len(inp))
# print(radio_button)
# print(len(radio_button))
# print('List of elements are found')
# print('Navbar found')
# print(name)
# print('name textfield found')


## id
# root = driver.find_element(By.ID, 'mountRoot')
# print(root)
# half_ele = driver.find_element(By.ID, 'amnHalfCard')
# print(half_ele)
# overlay = driver.find_element(By.ID, 'sec-overlay')
# print(overlay)
# desktop_header = driver.find_element(By.Id, 'desktop-headerMount')
# print(desktop_header)
#
# print('By id done')
#
# ## name
# theme_color = driver.find_element(By.NAME, 'theme-color')
# print(theme_color)
# viewport = driver.find_element(By.NAME, 'viewport')
# print(viewport)
# keyword = driver.find_element(By.NAME, 'keywords')
# print(keyword)
# desc = driver.find_element(By.NAME, 'description')
# print(desc)
#
# print('By name done')
#
# ## class
# desktop_con = driver.find_elements(By.CLASS_NAME, 'desktop-container')
# print(desktop_con)
# print(len(desktop_con))
# sub_con = driver.find_elements(By.CLASS_NAME, 'desktop-sbContainer')
# print(len(sub_con))
# header_link = driver.find_elements(By.CLASS_NAME, 'desktop-preHeaderLinks')
# print(len(header_link))
# bound = driver.find_elements(By.CLASS_NAME, 'desktop-bound')
# print(bound)
# print(len(bound))
# shop_base = driver.find_elements(By.CLASS_NAME, 'shop-base')
#
# print('BY class name done')


## USING CSS SELECTORS
# 'tag_name[attribute = 'value']' and can also use symbols like for id - #, class - .

# name = driver.find_element(By.CSS_SELECTOR, 'select[id="animals"]')
# animals = driver.find_element(By.CSS_SELECTOR, '#animals')

# form_group = driver.find_elements(By.CSS_SELECTOR, '.form-group')
# form_group = driver.find_elements(By.CSS_SELECTOR, "div[class='form-group]")

# mid_string = driver.find_elements(By.CSS_SELECTOR, "a[href*='testautomation']")
# print('using * done')
# start_string = driver.find_elements(By.CSS_SELECTOR, "a[href^='https']")
# print('using ^ done')
# end_string = driver.find_elements(By.CSS_SELECTOR, "a[href$='.com']")
# print('using $ done')

# a[href* = 'substring'] --> * gives all the elements having the substring
# a[href^='substring'] --> ^ gives all the elements starting with the substring
# a[href$= 'substring'] --> $ gives elements which ends with the substring
# css selectors only go downward and you can't find inner Text
# div[class= "widget-content"] a[href*='testautomation']  -- to make it unique we can go down the tree writing space separated
## input[type = 'text'][class = 'register']

# downward = driver.find_elements(By.CSS_SELECTOR, "div[class='widget-content'] a[href*='testautomation']")
# print('using multiple done')
#
# print('worked fine')



## XPATH
## can go backwards or upwards and downwards, can also locate inner text, but it is slower than other locators and difficult to read
## two types -- absolute path and relative path
# absolute -- /html/body/..../tag_name[@attribute = 'value']
# relative path -- //tag_name[@attribute = 'value'] [index]
# can use indexing if there are multiple elements
## accessing inner text -- //tag_name[text() = "inner text"]


male = driver.find_element(By.XPATH, '//input[@type="radio"][1]')
print(male)
print("working fine1")
phone_no = driver.find_element(By.XPATH, '//input[@maxLength="10"]')
print("working fine")
value = driver.find_element(By.XPATH, '//option[@value="canada"]')
print('working fine')

udemy = driver.find_element(By.XPATH, '//a[text()= "Udemy Courses"]')
print(udemy)
print('working fine')

female = driver.find_element(By.XPATH, "//label[text()= 'Female']")
print('working fine')

# if there are multiple spaces we use contains method -- //tag_name[contains(text(), 'innerText')]

japan = driver.find_element(By.XPATH, '//option[contains(text(),"Japan")]')
print('working fine')

table_id = driver.find_element(By.XPATH, '//th[text()="ID"]')
print('working fine')
driver.quit()