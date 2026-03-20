from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

# dropdown are most of the time in select tag and if not in select tag we import select

driver = webdriver.Chrome()

# driver.get('https://testautomationpractice.blogspot.com/')
driver.get('https://www.lenskart.com/')
driver.maximize_window()

# country_dropdown = driver.find_element(By.ID, 'country')
# dropdown = Select(country_dropdown)

## can select by three ways -- select_by_visible_text, select_by_value, select_by_index(0 to n indexing)
# dropdown.select_by_value('australia')
# sleep(4)
# dropdown.select_by_index(3)
# sleep(5)
# dropdown.select_by_visible_text("Japan")
# sleep(2)

search = driver.find_element(By.ID, 'autocomplete-0-input')
sleep(2)
search.send_keys('eyeglasses', Keys.ENTER)
sleep(2)

sort_dropdown = driver.find_element(By.ID, 'sortByDropdown')
sort = Select(sort_dropdown)

sort.select_by_value('saving')
sleep(3)

# first_product = driver.find_element(By.XPATH, '//div[@class = "sc-bf32d8a7-0 gOVKHN"][1]/descendant::a[1]/descendant::div[3]/descendant::p[1]')
first_product = driver.find_element(By.XPATH, '//div[@class = "sc-bf32d8a7-0 gOVKHN"][1]/descendant::p[1]')
# first_product = driver.find_element(By.XPATH, '//div[@class = "sc-bf32d8a7-0 gOVKHN"][1]/child::div[@class = "sc-23b7d3eb-8 gUutuN"][1]/descendant::a[1]/child::div[3]/child::p')
print(first_product.text)
sleep(3)

# sort.select_by_index(4)
# sleep(3)
# sort.select_by_visible_text('Biggest Savings')
# sleep(3)



driver.quit()