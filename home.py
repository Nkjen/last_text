from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in")
driver.maximize_window()
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0,600);")
ruby_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium Ruby").click()
review_link = driver.find_element(By.CSS_SELECTOR, ".reviews_tab a").click()
star_five = driver.find_element(By.CLASS_NAME, "star-5").click()
comment_tab = driver.find_element(By.ID, "comment").send_keys("Nice book!")
author = driver.find_element(By. ID, "author").send_keys("Ivan")
email = driver.find_element(By. ID, "email").send_keys("ivan@ivanov.ru")
submit = driver.find_element(By.ID, "submit").click()
driver.quit()

