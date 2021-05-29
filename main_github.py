from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

#apply to my dummy job
URL = "https://www.linkedin.com/jobs/view/2526049348"
ACCOUNT_EMAIL = "robert.lee@berkeley.edu"
ACCOUNT_PASSWORD = "redacted"
PHONE="5551212"

chrome_driver_path = "/Users/robertlee/Applications/Chrome Apps.localized/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(URL)

sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()


#Wait for the next page to load.
time.sleep(3)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

#remember me
time.sleep(3)
remember = driver.find_element_by_class_name("btn__primary--large")
#<footer class=""
remember.click()

#APPLY
time.sleep(8)
apply_button = driver.find_element_by_class_name("jobs-apply-button--top-card")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

#Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()

driver.quit()


