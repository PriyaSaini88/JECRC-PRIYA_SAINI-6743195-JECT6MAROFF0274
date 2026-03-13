from selenium import webdriver
from selenium.webdriver.common.by import By

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opts)
driver.get('https://www.cricbuzz.com/')
driver.maximize_window()



print('Locators using ID:')
leaderboard=driver.find_elements(By.ID,'leaderboard')
print('Leaderboard found')
google_ads=driver.find_elements(By.ID,'google_ads_iframe_/1024780/Desktop_new/LB/Home_0__container__')
print('Google ads found')
main_header=driver.find_element(By.ID,'main-header')
print('Main header found')
shosh =driver.find_element(By.ID,'shosh')
print('Shosh found')
match_carousel=driver.find_element(By.ID,'match-carousel')
print('Match carousel found')
print('Locators using ID done!')

print('Locators using NAME:')
robots=driver.find_element(By.NAME,'robots')
print('Robots found')
viewport=driver.find_element(By.NAME,'viewport')
print('Viewport found')
description=driver.find_element(By.NAME,'description')
print('Description found')
google_bot=driver.find_element(By.NAME,'googlebot')
print('Googlebot found')
google_site_verification=driver.find_element(By.NAME,'google-site-verification')
print('Googlebot verified')
print('Locators using NAME done!')

print('Locators using CLASS:')
Bold_font=driver.find_elements(By.CLASS_NAME,'font-bold')
print('Bold font found')
XL_text=driver.find_elements(By.CLASS_NAME,'text-xl')
print('XL text found')
Mt_6=driver.find_elements(By.CLASS_NAME,'mt-6')
print('Mt 6 found')
col_span=driver.find_elements(By.CLASS_NAME,'col-span-9')
print('Col span found')
background=driver.find_elements(By.CLASS_NAME,'bg-white')
print('Background found')
print('Locators using CLASS done!')


driver.quit()