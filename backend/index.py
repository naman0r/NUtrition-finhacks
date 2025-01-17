import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('https://www.nudining.com/public/whats-on-the-menu');

time.sleep(7.5)

dining_hall_dropdown = driver.find_element(By.ID, "menu-location-selector__BV_toggle_")

date_dropdown = driver.find_element(By.ID, "menuDatePicker")
date_dropdown.click()

arrows = driver.find_elements(By.CLASS_NAME, "vc-svg-icon")
arrows[0].click()

time.sleep(2.5)

day_button = driver.find_element(By.XPATH, "//span[contains(text(),'20')]")
day_button.click()

time.sleep(5)

menu = {}

categories = driver.find_elements(By.CSS_SELECTOR, "caption")
for category in categories:
    menu[category.text] = []
    # print(category.text)

print("\n")

category_tables = driver.find_elements(By.CSS_SELECTOR, "tbody")
for category_table in category_tables:
    category_tables_children = category_table.find_elements(By.CSS_SELECTOR, "tr")
    print(len(category_tables_children))

print("\n")

menu_items = driver.find_elements(By.CLASS_NAME, "category-items_itemNameWrapper_zaBfp")
for menu_item in menu_items:
    all_children_by_xpath = menu_item.find_elements(By.XPATH, ".//*")
    print(all_children_by_xpath[0].text)

time.sleep(5)

driver.quit()