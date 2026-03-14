from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


## XPATH Axes
# ancestor --
# //tag_name[@attribute="value"]/ancestor::ancestor_tag_name[@attribute="value"]

# driver.get('https://www.amazon.in/')
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
sleep(3)

# fresh_button = driver.find_elements(By.XPATH, '//span[text()="Fresh"]/ancestor::div[@id="nav-link-groceries"]')
# fresh = driver.find_elements(By.XPATH, '//a[@class="nav-a  "]/ancestor::div[@id="nav-link-groceries"]')
# # div = driver.find_element(By.XPATH, '//span[text()="All"]/ancestor::div[@id="nav-main"]')
# print('working fine!')

## descendant
## //tag_name[@attribute="value"]/descendant::descendant_tag_name[@attribute="value"]
# InnerText = driver.find_elements(By.XPATH, '//div[@id="nav-main"]/descendant::span[text()="All"]')
# print('Working fine!')

## parent and child will find only immediate child and immediate parent
## preceding sibling(above the current one) ---> //tag_name[@attribute="value"]/preceding-sibling::ps_tag_name[@attribute="value"]
## following sibling(younger one/below it) ---> //tag_name[@attribute="value"]/following-sibling::fs_tag_name[@attribute="value"]
# mx_player = driver.find_elements(By.XPATH, '//span[text()="Fresh"]/ancestor::li/following-sibling::li[1]')
# print('working fine!')

## Link_Text and Partial_Link_Text
## only when we have anchor tag(link) with Inner Text -- link + Inner Text

# driver.find_element(By.LINK_TEXT, "Udemy Courses")
# print('Working fine using Link Text')
#
# driver.find_element(By.PARTIAL_LINK_TEXT, "Udemy")
# print('using Partial_Link_Text')


## Practice XPath Axes
# Price = driver.find_element(By.XPATH, '//td[text()="Learn Java"]/following-sibling::td[3]')
# print(Price)
# print('worked!')

# selenium = driver.find_element(By.XPATH, '//td[text()="Amod"]/ancestor::tr/preceding-sibling::tr[4]/child::td[3]')
selenium = driver.find_element(By.XPATH, '//td[text()="Amod"]/ancestor::table/child::tbody/child::tr[2]/child::td[3]')
print('Worked!')

book_names = driver.find_elements(By.XPATH, '//td[text() ="300"]/preceding-sibling::td[3]')
print(book_names)
print('worked!')

#
Name = driver.find_elements(By.XPATH, '//tbody[@id = "rows"]/descendant::tr/descendant::td[1]')
print(Name)
print('worked!')

driver.quit()
