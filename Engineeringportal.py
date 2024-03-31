import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://webority-os-engineering-web-team-staging.azurewebsites.net/Login?ReturnUrl=%2Fprojects")
time.sleep(1)
eleid = "#Input_Email"
element = driver.find_element(By.CSS_SELECTOR,eleid)
element.send_keys("anuj.vashisht@webority.com")
eleid ="#Input_Password"
element= driver.find_element(By.CSS_SELECTOR,eleid)
element.send_keys("Anuj@123456")
element.send_keys(Keys.ENTER)
# eleid ="header-fixed header-mobile-fixed subheader-enabled subheader-fixed aside-enabled aside-fixed aside-minimize-hoverable swal2-shown swal2-height-auto"
# element= driver.find_element(By.CLASS_NAME,eleid)
# element.send_keys("123456")
input()


