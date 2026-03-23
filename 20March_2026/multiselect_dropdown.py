from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
#
# multi_drop = driver.find_element(By.ID, "colors")
# select = Select(multi_drop)
#
# if select.is_multiple:
#     select.select_by_value('blue')
#     select.select_by_index(3)
#     select.select_by_visible_text('Red')
#
#
# print('Before Deselect:', [i.text for i in select.all_selected_options])
#
# sleep(3)
#
# select.deselect_by_value('blue')
#
# print('Before Deselect:', [i.text for i in select.all_selected_options])
#
#
# driver.quit()

#########################

driver.get(r'C:\Users\nitin\OneDrive\Desktop\PythonProject\JECRC\20March_2026\playlist.html')
driver.maximize_window()

song_list = driver.find_element(By.ID, 'songs')
select = Select(song_list)

if select.is_multiple:
    select.select_by_index(4)
    select.select_by_visible_text('Shape of You')
    select.select_by_visible_text('Animals')

print([i.text for i in select.all_selected_options])

driver.find_element(By.XPATH, '//button[text() = "Add to Playlist"]').click()

print([i.text for i in select.options])
sleep(5)

driver.quit()


