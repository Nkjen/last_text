from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in")
driver.maximize_window()
driver.implicitly_wait(5)

account_2 = driver.find_element(By.PARTIAL_LINK_TEXT, "My Account").click()
username_log = driver.find_element(By.ID, "username").send_keys("ivan@ivanov.ru")
log_psw = driver.find_element(By. ID, "password").send_keys("IvAnOv_123I_vAn")
login_btn = driver.find_element(By.XPATH, "//input[@name='login']").click()
shop_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 a").click()
driver.execute_script("window.scrollBy(0,600);")
html_5 = driver.find_element(By.PARTIAL_LINK_TEXT, "HTML5 Forms").click()
book_name = driver.find_element(By.CLASS_NAME, "entry-title")
book_name_check = book_name.text
print(book_name_check)
if book_name_check == "HTML5 Forms":
    print("название книги корректное")
else:
    print("название книги Мимо")
driver.quit()

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in")
driver.maximize_window()
driver.implicitly_wait(5)

account_2 = driver.find_element(By.PARTIAL_LINK_TEXT, "My Account").click()
username_log = driver.find_element(By.ID, "username").send_keys("ivan@ivanov.ru")
log_psw = driver.find_element(By. ID, "password").send_keys("IvAnOv_123I_vAn")
login_btn = driver.find_element(By.XPATH, "//input[@name='login']").click()
shop_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 a").click()
html_btn = driver.find_element(By. CSS_SELECTOR, ".product-categories li:nth-child(2) a").click()
product_qty = driver.find_elements(By.CSS_SELECTOR, ".products li")
product_qty_check = len(product_qty)
print(product_qty_check)
if product_qty_check == 3:
    print("в категории отображается ", product_qty_check, "товара")
else:
    print("в категории отображается не три товара")

driver.quit()

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in")
driver.maximize_window()
driver.implicitly_wait(5)

account_2 = driver.find_element(By.PARTIAL_LINK_TEXT, "My Account").click()
username_log = driver.find_element(By.ID, "username").send_keys("ivan@ivanov.ru")
log_psw = driver.find_element(By. ID, "password").send_keys("IvAnOv_123I_vAn")
login_btn = driver.find_element(By.XPATH, "//input[@name='login']").click()
shop_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 a").click()

sorting_btn = driver.find_element(By.CLASS_NAME, "orderby")
sorting_btn_check = sorting_btn.get_attribute("value")
assert "menu_order" in sorting_btn_check
if sorting_btn_check == "menu_order":
    print("проверка сортировки успешна")
else:
    print("проверка сортировки не очень успешна")
sorting_btn_select = Select(sorting_btn)
sorting_btn_select.select_by_value("price-desc")
sorting_btn_2 = driver.find_element(By.CLASS_NAME, "orderby")
sorting_btn_2_check = sorting_btn_2.get_attribute("value")
print(sorting_btn_2_check)
if sorting_btn_2_check == "price-desc":
    print("сортировка выбрана от большего к меньшему")
else:
    print("сортировка выбрана - не знаю какая")
driver.quit()

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in")
driver.maximize_window()
driver.implicitly_wait(5)

account_2 = driver.find_element(By.PARTIAL_LINK_TEXT, "My Account").click()
username_log = driver.find_element(By.ID, "username").send_keys("ivan@ivanov.ru")
log_psw = driver.find_element(By. ID, "password").send_keys("IvAnOv_123I_vAn")
login_btn = driver.find_element(By.XPATH, "//input[@name='login']").click()
time.sleep(3)
shop_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 a").click()
driver.execute_script("window.scrollBy(0,600);")

android_book = driver.find_element(By.PARTIAL_LINK_TEXT, "Android Quick Start Guide").click()
old_price = driver.find_element(By. CSS_SELECTOR, ".price>del>span")
old_price_text = old_price.text
print(old_price_text)
assert "₹600.00" in old_price_text
new_price = driver.find_element(By.CSS_SELECTOR, ".price>ins>span")
new_price_text = new_price.text
assert "₹450.00" in new_price_text

book_cover = WebDriverWait(driver, 1).until(
    EC.element_to_be_clickable((By. CSS_SELECTOR, ".images a"))
).click()
pp_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))
).click()
driver.quit()

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in")
driver.maximize_window()
driver.implicitly_wait(5)

shop_btn = driver.find_element(By.ID, "menu-item-40").click()
driver.execute_script("window.scrollBy(0,400);")
time.sleep(3)
book_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Develpment").click()
add_basket = driver.find_element(By.CLASS_NAME, "single_add_to_cart_button").click()
time.sleep(3)
basket_qty_count = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-contents .cartcontents")
basket_qty_count_text = basket_qty_count.text
print(basket_qty_count_text)
assert "1 Item" in basket_qty_count_text

basket_amount = driver.find_element(By.CSS_SELECTOR, "#wpmenucartli .amount")
basket_amount_text = basket_amount.text
print(basket_amount_text)
assert "₹180.00" in basket_amount_text

basket_total = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-icon-shopping-cart-0").click()
subtotal_info = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal .woocommerce-Price-amount"), "₹180.00")
)

print(subtotal_info)
total_info = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹189.00")
)
print(total_info)

driver.quit()

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in")
driver.maximize_window()
driver.implicitly_wait(5)

shop_btn = driver.find_element(By. CSS_SELECTOR, "#menu-item-40 a").click()
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(3)
development_btn = driver.find_element(By. CSS_SELECTOR, ".post-182 .button").click()
time.sleep(3)
algorithm_btn = driver.find_element(By.CSS_SELECTOR, ".post-180 .button").click()
basket_into = driver.find_element(By. CSS_SELECTOR, ".wpmenucart-icon-shopping-cart-0").click()
time.sleep(3)
first_to_remove = driver.find_element(By.CSS_SELECTOR, ".woocommerce >form >table>tbody>tr:nth-child(1) .product-remove .remove").click()

undo_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-message a")
)).click()

qty_clear = driver.find_element(By. CSS_SELECTOR, "tbody>tr:nth-child(1) .product-quantity .input-text")
qty_clear.clear()
qty_clear.send_keys("3")
update_btn = driver.find_element(By. XPATH, "//input[@name='update_cart']").click()

qty_check = driver.find_element(By. CSS_SELECTOR, "tbody>tr:nth-child(1) .input-text")
qty_check_2 = qty_check.get_attribute("value")
print(qty_check_2)
assert "3" in qty_check_2
time.sleep(3)
coupon_btn = driver.find_element(By. CSS_SELECTOR, ".actions .coupon .button").click()
time.sleep(3)
coupon_text_btn = driver.find_element(By. CSS_SELECTOR, ".page-content .woocommerce-error li")
coupon_text_btn_text = coupon_text_btn.text
print(coupon_text_btn_text)
assert "Please enter a coupon code." in coupon_text_btn_text
driver.quit()

driver = webdriver.Chrome()
driver.get("http://practice.automationtesting.in")
driver.maximize_window()
driver.implicitly_wait(5)

shop_btn = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 a")
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(3)
basket_add = driver.find_element(By.CSS_SELECTOR, ".post-182 .button").click()
time.sleep(2)
basket_go = driver.find_element(By.CSS_SELECTOR, ".wpmenucart-icon-shopping-cart-0").click()

time.sleep(3)

proceed_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-forward"))
)
proceed_btn.click()
# time.sleep(5)
first_name_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name"))
)

first_name_input.send_keys("Ivan")
last_name_input = driver.find_element(By. ID, "billing_last_name").send_keys("Ivanov")
email_input = driver.find_element(By.ID, "billing_email").send_keys("ivan@ivanov.ru")
phone_input = driver.find_element(By.ID, "billing_phone").send_keys("13465789000")
country_input = driver.find_element(By. ID, "select2-chosen-1").click()

block_input = driver.find_element(By. ID, "s2id_autogen1_search").send_keys("Coc")
country_input_2 = driver.find_element(By. CLASS_NAME, "select2-match").click()

street_input = driver.find_element(By. ID, "billing_address_1").send_keys("Ivanovo str")
city_input = driver.find_element(By. ID, "billing_city").send_keys("Ivanovo town")
county_input = driver.find_element(By. ID, "billing_state").send_keys("Leningradskaya obl")
postcode_input = driver.find_element(By. ID, "billing_postcode").send_keys("190000")
driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)

check_payments = driver.find_element(By. ID, "payment_method_cheque").click()
place_order_btn = driver.find_element(By. ID, "place_order").click()

thank_you_text = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received.")
)
print(thank_you_text)

payment_method = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By. CSS_SELECTOR, ".method strong"), "Check Payments")
)
print(payment_method)

