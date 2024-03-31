import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# names=["ereqye","jegfjwe ejhwekj","ewjkjwe&^hdklwehf","","   ","7364573","^$^*&"]
# for namei in range(len(names)):
#     try:
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get("https://parivahealth-web-admin-staging.azurewebsites.net/")
driver.maximize_window()

element = driver.find_element(By.CSS_SELECTOR,"#Input_Email")
element.send_keys("kanchan@webority.com")

        # eleid = "#Input_Password"
element = driver.find_element(By.CSS_SELECTOR,"#Input_Password")
element.send_keys("1234567")
element.send_keys(Keys.ENTER)

        # driver.execute_script("window.scrollTo(0,300)")

        # eleid = "/html[1]/body[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/a[1]"
driver.find_element(By.CSS_SELECTOR,".btn.btn-success.font-weight-bolder.font-size-xs.mt-4").click()

driver.execute_script("window.scrollTo(0,200)")

        ## Child detail form-

        # driver.find_element(By.XPATH,"//i[@class='fa fa-pen icon-sm text-muted']").click()

driver.find_element(By.XPATH,"//input[@id='Input_ChildProfileImageFile']").send_keys("C:\\Users\\Anuj vashisth\\Desktop\\Abcd.jpeg")

driver.find_element(By.CSS_SELECTOR,"#Input_ChildName").send_keys("anuj")
        # element = driver.find_elements(By.CSS_SELECTOR,"#Input_ChildDateOfBirth")
driver.find_element(By.CSS_SELECTOR,"#Input_ChildDateOfBirth").click()

# driver.find_element(By.XPATH,"//th[normalize-space()='March 2024']").click()
#
# driver.find_element(By.XPATH,"//th[normalize-space()='2024']").click()
#
#         #driver.find_element(By.XPATH,"//th[normalize-space()='2020-2029']").click()
#
# found=0
# while(found==0):
#     print("started")
#     alldata=driver.find_elements(By.CLASS_NAME,"year")
#     for i in alldata:
#         print(i.text)
#         if i.text=='1974':
#             i.click()
#             found=1
#             break
#     if found==1:
#         break
#
#     driver.find_element(By.XPATH,"//div[@class='datepicker-years']//th[@class='prev'][normalize-space()='«']").click()
#
# allmonth=driver.find_elements(By.CLASS_NAME,"month")
# for i in allmonth:
#     print(i.text)
#     if i.text=='Jul':
#         i.click()
#         break
# driver.find_element(By.XPATH,"//td[normalize-space()='12']").click()
driver.find_element(By.XPATH,"//td[normalize-space()='17']").click()
driver.find_element(By.XPATH,"(//button[@title='Select Gender'])[1]").click()

driver.find_element(By.CSS_SELECTOR,"#bs-select-3-2").click()
driver.find_element(By.CSS_SELECTOR,"button[title='First Child']").click()

driver.find_element(By.CSS_SELECTOR,"#bs-select-4-1").click()
driver.find_element(By.CSS_SELECTOR,"#Input_ChildSchool").send_keys("Rotary Public school")
driver.execute_script("window.scrollTo(0,600)")
driver.find_element(By.CSS_SELECTOR,"button[title='Select Grade']").click()

driver.find_element(By.CSS_SELECTOR,"#bs-select-5-10").click()
driver.find_element(By.CSS_SELECTOR,"#Input_ChildDiagnosis").send_keys("Hello everyone welcome to India")
driver.find_element(By.CSS_SELECTOR,"#next-step").click()
time.sleep(2)
        # driver.find_element(By.CSS_SELECTOR,"button[class='swal2-confirm btn btn-success font-weight-bolder swal2-styled']").click()

        ## IFSP Members form -
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Name']").send_keys("Vashisth one")

date_input = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Select Date of Birth'][name='PatientMembersInput[0][DateOfBirth]']")
ActionChains(driver).move_to_element(date_input).click().perform()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"tbody tr:nth-child(2) td:nth-child(1)"))).click()
driver.execute_script("window.scrollTo(0,300)")

driver.find_element(By.CSS_SELECTOR,"button[title='Select Gender']").click()

driver.find_element(By.CSS_SELECTOR,"#bs-select-6-2").click()
 
driver.find_element(By.CSS_SELECTOR,"button[title='Select Relation']").click()

driver.find_element(By.CSS_SELECTOR,"#bs-select-7-1").click()
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Phone Number']").send_keys("1234567890")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Email']").send_keys("Anuj@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter Profession']").send_keys("Business man")
driver.execute_script("window.scrollTo(0,500)")
driver.find_element(By.CSS_SELECTOR,".btn.btn-light-success.collapseArea.font-size-m").click()
driver.execute_script("window.scrollTo(0,800)")

driver.find_element(By.CSS_SELECTOR,".btn.btn-light-danger.collapseArea.font-size-m.mb-8").click()

driver.find_element(By.CSS_SELECTOR,"button[class='swal2-cancel btn btn-secondary font-weight-bolder swal2-styled']").click()
driver.find_element(By.CSS_SELECTOR,".btn.btn-light-danger.collapseArea.font-size-m.mb-8").click()

driver.find_element(By.CSS_SELECTOR,"button[class='swal2-confirm btn btn-success font-weight-bolder swal2-styled']").click()
date_input = driver.find_element(By.CSS_SELECTOR,"#prev-step")
driver.execute_script("arguments[0].scrollIntoView();", date_input)
date_input.click()
time.sleep(2)
date_input = driver.find_element(By.CSS_SELECTOR,"#next-step")
driver.execute_script("arguments[0].scrollIntoView();", date_input)
date_input.click()
time.sleep(2)
driver.execute_script("window.scrollTo(0,800)")
driver.find_element(By.CSS_SELECTOR,"button[title='Select Primary Language']").click()
driver.find_element(By.CSS_SELECTOR,"#bs-select-8-1").click()
driver.find_element(By.CSS_SELECTOR,"button[title='Select Secondary Language']").click()
driver.find_element(By.CSS_SELECTOR,"#bs-select-9-2").click()
driver.find_element(By.CSS_SELECTOR,"#next-step").click()

        ## INSURANCE page
driver.execute_script("window.scrollTo(0,300)")
driver.find_element(By.CSS_SELECTOR,"#next-step").click()
    # except Exception as e:
    #     print("error",e)
    #     print("excpetion at name",names[namei])


## Program page

driver.find_element(By.CSS_SELECTOR,"button[title='Select Service Enrollment']").click()
driver.find_element(By.CSS_SELECTOR,"#bs-select-10-1").click()

driver.find_element(By.CSS_SELECTOR,"label[class='radio ml-4'] span[class='mr-2']").click()
driver.find_element(By.CSS_SELECTOR,"label[class='radio'] span[class='mr-2']").click()
driver.find_element(By.CSS_SELECTOR,"label[class='radio ml-4'] span[class='mr-2']").click()
driver.execute_script("window.scrollTo(0,600)")
driver.find_element(By.CSS_SELECTOR,"#Input_Provider").send_keys("ABCD")
driver.find_element(By.CSS_SELECTOR,"#Input_AddressLine1").send_keys("House number 9211")
driver.find_element(By.CSS_SELECTOR,"#Input_AddressLine2").send_keys("Railway road")
driver.find_element(By.CSS_SELECTOR,"#Input_City").send_keys("Gurgaon")
driver.find_element(By.CSS_SELECTOR,"button[title='Select State'] div[class='filter-option-inner-inner']").click()
driver.find_element(By.CSS_SELECTOR,"#bs-select-11-57").click()
driver.find_element(By.CSS_SELECTOR,"#Input_PostalCode").send_keys("123456")



input()
