from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

# driver.get('https://testautomationpractice.blogspot.com/')
# driver.get('https://www.myntra.com/')
# driver.get('https://www.amazon.in/')
# driver.maximize_window()
# sleep(2)

## text field
# name = driver.find_element(By.ID, 'name')
#name.clear()  # to clear the previous entered data
# name.send_keys('Priya')
# ## send_keys('') will write the text inside it in the input field

# sleep(5)
#
# email = driver.find_element(By.XPATH, '//input[@placeholder = "Enter EMail"]')
# email.send_keys('email@yahooo.in')
# sleep(5)
#
# print(name.get_attribute('placeholder'))
# print(name.get_attribute('value'))

# search = driver.find_element(By.XPATH, '//input[@placeholder = "Search for products, brands and more"]')
# search.send_keys('watches')
# sleep(3)
# print(search.get_attribute('placeholder'))
# print(search.get_attribute('value'))

# search_button = driver.find_element(By.XPATH, '//span[@class = "myntraweb-sprite desktop-iconSearch sprites-search"]')
# search_button.click()
# sleep(3)

# search = driver.find_element(By.XPATH, '//input[@placeholder = "Search for products, brands and more"]')
# search.clear()
# search.send_keys('Watches', Keys.ENTER)
# sleep(3)


# search_amazon = driver.find_element(By.ID, 'twotabsearchtextbox')
# search_amazon.clear()
# search_amazon.send_keys('Samsung s25')
# sleep(3)
#
# search_button = driver.find_element(By.ID, 'nav-search-submit-button')
# search_button.click()
# sleep(3)

# 2nd way
# search_amazon.send_keys('Samsung s25', Keys.ENTER)
# sleep(3)

## radio buttons
# driver.find_element(By.ID, 'male').click()
# sleep(2)
#
# driver.find_element(By.XPATH, '//label[text()="Monday"]/preceding-sibling::input').click()
# sleep(3)
#
# monday_checkBox = driver.find_element(By.XPATH, '//input[@id = "monday"]/following-sibling::label')
# print(monday_checkBox.text)  ## .text will return inner text
# sleep(3)

## Toggle between male and female using for loop
# list1 = ['male', 'female']
# for i in list1:
#     driver.find_element(By.ID, i).click()
#     sleep(2)
#
# # if-else
# gender = input('Enter the gender id:')
# if gender =='male':
#     driver.find_element(By.ID, 'male').click()
#     sleep(2)
# else:
#     driver.find_element(By.ID, 'female').click()
#     sleep(2)
#


# checkbox exercise

# check_box = driver.find_elements(By.XPATH, '//input[@class = "form-check-input"]')
# for ele in range(2, len(check_box)):
#     check_box[ele].click()
# check_box = driver.find_elements(By.XPATH, '//div[@class = "form-group"][4]/child::div')
#
# for ele in check_box:
#     ele.click()
#     print(ele.text)
#     sleep(2)
#
# for ele in check_box[::-1]:
#     ele.click()
#     sleep(2)



## Practice 3
##flipkart
# 1. navigate to flipkart    2. find search field and search for a product   3. get attribute of the product searched    4. click on search button      5. click on a checkbox or boxes in filter
# 6. get the text of that filter

driver.get('https://www.flipkart.com/')
driver.maximize_window()
sleep(2)

search_bar = driver.find_element(By.XPATH, '//div[@class = "Afujtw"]/descendant::input[1]')
search_bar.clear()
search_bar.send_keys('mobiles')
print(search_bar.get_attribute('value'))
# search_bar.send_keys(Keys.ENTER)

button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
sleep(3)
button.click()
sleep(2)

checkbox = driver.find_element(By.XPATH, '//div[text() = "Apple"]')
checkbox.click()
print(checkbox.text)
sleep(2)

image = driver.find_elements(By.XPATH, '//img[@class="UCc1lI"][1]')
print(image.get_attribute('src'))
sleep(2)
# image = driver.find_elements(By.XPATH, '//img[@class="UCc1lI"]')
# print(image[3].get_attribute('src')) ## for printing images other than first one

driver.quit()
