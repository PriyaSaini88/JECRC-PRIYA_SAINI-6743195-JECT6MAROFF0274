# Radio Buttons
# Automate interaction with radio buttons https://demoqa.com/radio-button
#
# Open the radio button page.
# Print the title of the page.
# Locate the "Yes" radio button.
# Click the radio button using click().
# Capture and print the result message using .text.
# Use get_attribute() to fetch attributes like:
# class
# id
# Print the current URL.


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://demoqa.com/radio-button')
driver.maximize_window()
sleep(3)

print(driver.title)
sleep(1)

# yes = driver.find_element(By.XPATH, '//label[@for = "yesRadio"]')
yes = driver.find_element(By.XPATH, '//div[@class = "col-auto form-check"][1]/child::input')
yes.click()
result = driver.find_element(By.XPATH, '//span[@class = "text-success"]')
print(result.text)
print(yes.get_attribute('class'))
print(yes.get_attribute('id'))
sleep(3)

print(driver.current_url)



driver.quit()