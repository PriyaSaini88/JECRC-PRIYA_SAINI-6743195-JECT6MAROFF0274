from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

driver.find_element(By.ID, 'datepicker').send_keys('04/30/2026', Keys.ENTER)


month = 'May'
date = '2'
year = '2024'

driver.find_element(By.ID, 'txtDate').click()
sleep(1)

select = Select(driver.find_element(By.XPATH, '//select[@class = "ui-datepicker-month"]'))
select.select_by_visible_text(month)

select2 = Select(driver.find_element(By.XPATH, '//select[@class = "ui-datepicker-year"]'))
select2.select_by_visible_text(year)

driver.find_element(By.XPATH, f'//a[text() = "{date}"]/parent::td').click()
sleep(3)




driver.quit()

