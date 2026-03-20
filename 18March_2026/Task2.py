## Task 2
### Registration Form

# 1. Go to: https://demoqa.com/automation-practice-form
# 2. Handle every element in that form except the calendar
# `Note: Give fake names and emails`
# 3. Click on submit button


from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from time import sleep

from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/automation-practice-form')
driver.maximize_window()
sleep(3)

first_name = driver.find_element(By.ID, 'firstName')
first_name.clear()
first_name.send_keys('Priya')
print(first_name.get_attribute('placeholder'))
sleep(3)

last_name = driver.find_element(By.ID, 'lastName')
last_name.clear()
last_name.send_keys('Saini')
sleep(3)

email = driver.find_element(By.ID, 'userEmail')
email.clear()
email.send_keys('abc@gmail.com')
sleep(3)

gender = driver.find_element(By.ID, 'gender-radio-2').click()
sleep(3)

phone_no = driver.find_element(By.ID, 'userNumber')
phone_no.clear()
phone_no.send_keys('1234567890')
print(phone_no.get_attribute('class'))
sleep(3)

subject = driver.find_element(By.ID, 'subjectsInput')
subject.clear()
subject.send_keys('English')
subject.send_keys(Keys.ENTER)
sleep(3)


hobbies = driver.find_element(By.ID, 'hobbies-checkbox-2')
hobbies.click()
sleep(3)

upload_file = driver.find_element(By.ID, 'uploadPicture')
upload_file.send_keys(r"C:\Users\nitin\Downloads\task2.jpeg")
sleep(3)

Address = driver.find_element(By.ID, 'currentAddress')
Address.clear()
Address.send_keys('123 street')
sleep(3)

state = driver.find_element(By.XPATH, "//div[@id ='state']")
sleep(1)
state.click()
sleep(1)
driver.find_element(By.XPATH, "//div[text() = 'Rajasthan']").click()

city = driver.find_element(By.XPATH, "//div[@id = 'city']")
sleep(1)
city.click()
sleep(1)
driver.find_element(By.XPATH, "//div[text() = 'Jaipur']").click()
sleep(1)

submit = driver.find_element(By.ID, 'submit')
submit.click()
sleep(3)




driver.quit()
