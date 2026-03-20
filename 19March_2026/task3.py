# TAsk 3
# 1. navigate to amazon
# 2. search a product through send_keys
# BUT dont click on search or keys.enter
# 3. Wait for the suggestions to appear
# 4. Click on 4th suggestion
# 5. Click on Sort By and click on newest
# 6. Click on free shipping check box
# 7. wait for first product and return me the name=price
# (without using inner text)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get('https://www.amazon.in/')
driver.maximize_window()

wait = WebDriverWait(driver, 20)

search = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
search.send_keys("dress")

fourth_suggest = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class = "s-suggestion-container"])[4]/child::div')))
fourth_suggest.click()

sort_by = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@id = "a-autoid-0-announce"]/child::span')))
sort_by.click()

newest = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@id = "s-result-sort-select_4"]')))
newest.click()

free_shipping = wait.until(EC.element_to_be_clickable((By.XPATH, '(//i[@class="a-icon a-icon-checkbox"])[3]')))
free_shipping.click()

first_product_name = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@class = "a-link-normal s-line-clamp-2 puis-line-clamp-3-for-col-4-and-8 s-link-style a-text-normal"]/descendant::span')))
print(f'The name of the Product is : {first_product_name.text}')

price = wait.until(EC.visibility_of_element_located((By.XPATH, '(//div[@class="sg-col-inner"])[5]/descendant::div[@data-cy="price-recipe"]/div/div/a/span')))
print(f'The Price is: {price.text}')


driver.quit()