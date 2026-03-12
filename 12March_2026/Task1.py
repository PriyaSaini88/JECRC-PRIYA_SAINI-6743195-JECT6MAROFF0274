## Task 1 : Use all methods in one script on chrome
from selenium import webdriver
# from time import sleep

# driver = webdriver.Chrome()
# sleep(3)

# driver.get('https://topbrains.com/')
# sleep(2)
#
# driver.maximize_window()
# sleep(2)
#
# # driver.minimize_window()
# # sleep(2)
#
# driver.back()
# sleep(2)
#
# driver.forward()
# sleep(2)
#
# driver.refresh()
# sleep(2)
#
# driver.close()
# driver.quit()


## using ChromeOptions

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://topbrains.com/')
driver.maximize_window()


driver.back()
driver.forward()
driver.refresh()

driver.minimize_window()

driver.close()
driver.quit()
