import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://webority.dev/pariva/form3/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"#GetStartedButton").click()
driver.find_element(By.CSS_SELECTOR,"label[id='parent-flow-show'] div[class='radio-circle']").click()
driver.find_element(By.CSS_SELECTOR,"label[id='parent-flow-show'] div[class='radio-circle']")
driver.execute_script("window.scrollTo(0,400)")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"#your_name").send_keys("John the great")
driver.find_element(By.CSS_SELECTOR,"#child_relationship").send_keys("Father")
driver.find_element(By.CSS_SELECTOR,"#your_location").send_keys("America")
driver.find_element(By.CSS_SELECTOR,"#your_email").send_keys("John@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#your_phone_number").send_keys("0987654321")
driver.find_element(By.CSS_SELECTOR,"select[id='your_communication_method'] option[value='Text']").click()
# driver.find_element(By.XPATH,"(//option[@value='Email'][normalize-space()='Email'])[1]").click()
driver.find_element(By.CSS_SELECTOR,"#AgreeTextMessage").click()
driver.execute_script("window.scrollTo(0,900)")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"#child_name").send_keys("Khushi sharma")
driver.find_element(By.CSS_SELECTOR,"option[value='Male']").click()
driver.find_element(By.CSS_SELECTOR,"#child_dob").click()
driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(2) td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR,".w-50.dummy-div").click()
driver.execute_script("window.scrollTo(0,100)")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"label[id='referral-flow-show'] p[class='radio-text']").click()
driver.execute_script("window.scrollTo(0,400)")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"#referral_name").send_keys("Anuj vvvv")
driver.find_element(By.CSS_SELECTOR,"#referral_agency").send_keys("near faridabad")
driver.find_element(By.CSS_SELECTOR,"#referral_phone_number").send_keys("7303255250")
driver.find_element(By.CSS_SELECTOR,"#referral_email").send_keys("anuj@gmail.com")
driver.execute_script("window.scrollTo(0,700)")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"#parent_name").send_keys("anuj vashisth")
driver.find_element(By.CSS_SELECTOR,"#parent_relationship").send_keys("Son")
driver.find_element(By.CSS_SELECTOR,"#parent_location").send_keys("netherland")
driver.find_element(By.CSS_SELECTOR,"#parent_email").send_keys("anujvashisth@gmail.com")
driver.find_element(By.CSS_SELECTOR,"#parent_phone_number").send_keys("7654321009")
driver.find_element(By.CSS_SELECTOR,"select[id='preferred_communication_method'] option[value='Email']").click()
driver.execute_script("window.scrollTo(0,1200)")
time.sleep(2)
driver.find_element(By.XPATH,"(//a[normalize-space()='Next'])[1]").click()

# driver.find_element(By.CSS_SELECTOR,"#insuranceNo").click()
driver.find_element(By.XPATH,"(//label[@id='insuranceYes'])[1]").click()
driver.execute_script("window.scrollTo(0,400)")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#insurance_name").send_keys("Policy bazaar")
driver.find_element(By.CSS_SELECTOR,"#insurance_policy_number").send_keys("BMZPVyt56787654321009")
driver.find_element(By.CSS_SELECTOR,"#insurance_group_id").send_keys("FD")
driver.find_element(By.CSS_SELECTOR,"#p_card_holder_name").send_keys("Raghav")
driver.find_element(By.CSS_SELECTOR,"#datePicker2").click()
driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(2) td:nth-child(2)").click()
driver.find_element(By.CSS_SELECTOR,"#insurance_company_phone_no").send_keys("9711441628")
driver.find_element(By.CSS_SELECTOR,"#HolderAddressText").send_keys("H.no 9211,dubai")
driver.execute_script("window.scrollTo(0,1200)")
time.sleep(2)
driver.find_element(By.XPATH,"(//a[normalize-space()='Next'])[1]").click()
driver.find_element(By.XPATH,"(//div[@id='step2-radio-container'])[1]").click()
driver.execute_script("window.scrollTo(0,900)")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"#ConcernArea").send_keys("Webority technologies pvt ltd ")
driver.execute_script("window.scrollTo(0,100)")
time.sleep(2)
driver.find_element(By.XPATH,"(//div)[118]").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0,1100)")
time.sleep(1)
driver.find_element(By.XPATH,"(//input[@id='PsychologistRadioBtn2'])[1]").click()
driver.find_element(By.XPATH,"(//input[@id='MentalRadioBtn2'])[1]").click()
driver.find_element(By.CSS_SELECTOR,"#evolutionOfChild").send_keys("abcdefghijklmnop")
driver.execute_script("window.scrollTo(0,100)")
time.sleep(2)
driver.find_element(By.XPATH,"(//div)[122]").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0,1500)")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"#otherNeedsinput").send_keys("poiuytewegffggcgchvnvnbnbnb")
driver.find_element(By.XPATH,"(//a[normalize-space()='Next'])[1]").click()
driver.execute_script("window.scrollTo(0,1600)")
time.sleep(1)
# driver.find_element(By.XPATH,"(//a[normalize-space()='Finish'])[1]").click()

input()