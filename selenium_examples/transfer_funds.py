from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.implicitly_wait(5)

driver.get("https://www.patchmutual.com/")

login_button = driver.find_element(By.ID, "AccountLink")
login_button.click()

username_field = driver.find_element(By.ID, "uid")
password_field = driver.find_element(By.ID, "passw")
submit_button = driver.find_element(By.NAME, "btnSubmit")

username_field.send_keys("jsmith")
password_field.send_keys("demo1234")
submit_button.click()

time.sleep(5)

transfer_funds_link = driver.find_element(By.ID, "MenuHyperLink3")
transfer_funds_link.click()

time.sleep(2)

transfer_dropdown = Select(driver.find_element(By.ID, "toAccount"))
transfer_dropdown.select_by_value("800003")

transfer_ammount = driver.find_element(By.ID, "transferAmount")
transfer_ammount.send_keys("12345")

time.sleep(2)

transfer_button = driver.find_element(By.NAME, "transfer")
transfer_button.click()

time.sleep(5)
driver.quit()
