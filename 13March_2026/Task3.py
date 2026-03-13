from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(3)
# Locate the main search bar using its ID with a CSS Selector.
search_bar = driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
print('Working fine for search bar')

# Locate the Amazon logo(usually an < a > tag with an ID like nav-logo sprites) using a CSS Selector.
amazon_logo = driver.find_element(By.CSS_SELECTOR, '#nav-logo-sprites')
print('Working fine for logo')

# Locate the "Cart" link/icon (often has an ID like nav-cart) using a CSS Selector.
cart = driver.find_element(By.CSS_SELECTOR, 'span[class="nav-cart-icon nav-sprite"]')
print('Working fine for cart')

#  Locate the "Sign in" link in the navigation bar (It might be inside a div with an ID like nav-tools. Use descendant way (space)).
sign_in = driver.find_element(By.CSS_SELECTOR, 'div[id="nav-tools"] div[class="nav-line-1-container"] span[id="nav-link-accountList-nav-line-1"]')
print('Working fine for sign in')

#  Locate all the main category links in the navigation bar under "All"(e.g."Best Sellers", "Mobiles", "Today's Deals").
main = driver.find_elements(By.CSS_SELECTOR, 'div[id="nav-xshop"] a')
print(len(main))
print('Working fine for main category links')


driver.quit()