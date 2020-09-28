from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("http://practice.automationtesting.in")
# driver.maximize_window()
# driver.implicitly_wait(5)
#
# account = driver.find_element(By.PARTIAL_LINK_TEXT, "My Account").click()
# reg_email = driver.find_element(By. ID, "reg_email").send_keys("ivan@ivanov.ru")
# reg_psw = driver.find_element(By. ID, "reg_password").send_keys("IvAnOv_123I_vAn")
# register = driver.find_element(By.XPATH, "//input[@name='register']").click()
# driver.quit()

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in")
driver.maximize_window()
driver.implicitly_wait(5)
account_2 = driver.find_element(By.PARTIAL_LINK_TEXT, "My Account").click()
username_log = driver.find_element(By.ID, "username").send_keys("ivan@ivanov.ru")
log_psw = driver.find_element(By. ID, "password").send_keys("IvAnOv_123I_vAn")
login_btn = driver.find_element(By.XPATH, "//input[@name='login']").click()
logout_check = driver.find_element(By. CSS_SELECTOR, "#body li:nth-child(6) a")
logout_check_text = logout_check.text
print(logout_check_text)
if logout_check_text == "Logout":
    print("logout присутствует")
else:
    print("logout мимо")




