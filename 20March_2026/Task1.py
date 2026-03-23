from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get(r'C:\Users\nitin\OneDrive\Desktop\PythonProject\JECRC\20March_2026\playlist.html')
driver.maximize_window()

song_list = driver.find_element(By.ID, 'songs')
select = Select(song_list)

if select.is_multiple:
    for song in select.options:
        if 'Girl' in song.text or  'Love' in song.text:
            select.select_by_visible_text(song.text)


print([i.text for i in select.all_selected_options])
sleep(3)

driver.find_element(By.XPATH, '//button[text() = "Add to Playlist"]').click()
sleep(2)

driver.quit()


