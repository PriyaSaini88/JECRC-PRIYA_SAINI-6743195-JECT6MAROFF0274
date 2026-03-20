### Link Text & Partial Link Text


# 1. Go to https://the-internet.herokuapp.com/
# 2. Find the "Checkboxes" link using LINK_TEXT
# 3. Find the "Drag and Drop" link using PARTIAL_LINK_TEXT
# 4. Find how many <li> (list item) elements are on the page using find_elements and TAG_NAME. Print the count.
# 5. Navigate to https://the-internet.herokuapp.com/tables
# 6. Write an XPath to find the "Web Site" (td) for the person with email "jdoe@hotmail.com" in table 1 (Hint: Use text() and ancestor/following sibling or preceding-sibling).
# 7. Write an XPath to find the Delete link (a) for the person with Last Name "Bach" in table 1.
# 8. Write an XPath to find the second table `(<table>)` on the page using indexing.
# 9. Write an XPath to find the cell containing "$100.00" in table 2. Find its parent <tr> element.



from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()

checkbox = driver.find_element(By.LINK_TEXT, 'Checkboxes')
print('found!!')
sleep(3)

drag_n_drop = driver.find_element(By.PARTIAL_LINK_TEXT, 'Drag')
print('Found!!')
sleep(3)

list_items= driver.find_elements(By.TAG_NAME, 'li')
print(len(list_items))
sleep(3)


driver.get('https://the-internet.herokuapp.com/tables')
sleep(1)

web_site = driver.find_element(By.XPATH, '(//td[text() = "jdoe@hotmail.com"][1]/following-sibling::td[2])[1]')
print('found!!')
sleep(2)

delete_link = driver.find_element(By.XPATH, '(//td[text() ="Bach"][1]/following-sibling::td[5])[1]/descendant::a[2]')
print('found!!')
sleep(3)

sec_table = driver.find_element(By.XPATH, '//table[2]')
print('found!!')
sleep(3)

dues = driver.find_element(By.XPATH, '//table[@id="table2"]/child::tbody/child::tr[3]/child::td[4]')
print('found!!')
sleep(3)

driver.quit()