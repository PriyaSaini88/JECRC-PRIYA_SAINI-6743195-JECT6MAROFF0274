## To Open Chrome Browser

from selenium import webdriver
# from time import sleep

## ChromeOptions - isa class which takes your configuration which you apply before browser open (use instead of sleep)
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)

# driver = webdriver.Chrome()
# sleep(2)

# # To Open Microsoft Edge
# opts = webdriver.EdgeOptions()
# opts.add_argument('detach')
# driver = webdriver.Edge(options=opts)
# driver = webdriver.Edge()
# sleep(2)
#
# driver = webdriver.Firefox()
# opts = webdriver.FirefoxOptions()
# opts.add_argument('detach')

# driver = webdriver.Firefox(options=opts)
# sleep(5)

# driver.get('https://supertails.com/')
# driver.get('https://topbrains.com/')
# driver.maximize_window()
# sleep(4)
# driver.minimize_window()
# sleep(5)

# driver.back()
# sleep(3)
# driver.forward()
# sleep(3)
# driver.refresh()
# sleep(3)

# driver.close()
# driver.quit()

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get('https://topbrains.com/')
print(driver.title)
print(f'The title is : {driver.title}')
print(f'The url is : {driver.current_url}')
print(f'The name of browser is: {driver.name}')


