import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://stage.dailyobjects.com/auth/login")

phone_number=driver.find_elements_by_class_name("mat-form-field-autofill-control")[0]
phone_number.click()
phone_number.send_keys("9999999999")

time.sleep(2)

driver.find_elements_by_class_name("get-otp-btn")[0].click()

time.sleep(5)

otp_input=driver.find_elements_by_class_name("otp-input")[0]
otp_input.click()
otp_input.send_keys("8888")

time.sleep(5)

driver.find_elements_by_class_name("login-btn")[0].click()

driver.maximize_window()

time.sleep(10)

driver.find_elements_by_class_name("material-icons")[1].click()

time.sleep(5)

driver.find_elements_by_tag_name("li")[0].click()

time.sleep(5)

driver.find_elements_by_class_name("mat-ripple")[2].click()

time.sleep(2)

driver.find_element_by_class_name("add-new-address").click()

time.sleep(2)

name = driver.find_elements_by_class_name("mat-form-field-autofill-control")[0]
name.click()
name.send_keys("Saubhagya")

number = driver.find_elements_by_class_name("mat-form-field-autofill-control")[1]
number.click()
number.send_keys("someText")

pincode = driver.find_elements_by_class_name("mat-form-field-autofill-control")[2]
pincode.click()
pincode.send_keys("22100")

address = driver.find_elements_by_class_name("mat-form-field-autofill-control")[3]
address.click()
address.send_keys("My new address")

time.sleep(2)

country = driver.find_elements_by_class_name("mat-select-placeholder")[0]
country.click()
time.sleep(2)
driver.find_elements_by_class_name("mat-option-text")[99].click()

city = driver.find_elements_by_class_name("mat-form-field-autofill-control")[4]
city.click()
city.send_keys("Delhi")

time.sleep(5)

state = driver.find_elements_by_class_name("mat-select-placeholder")[0]
state.click()
time.sleep(2)
driver.find_elements_by_class_name("mat-option")[22].click()

if (driver.find_elements_by_class_name("ng-star-inserted")[162].text=="Mobile must be a valid mobile number"):
    print("Error detected in mobile number")
    number = driver.find_elements_by_class_name("mat-form-field-autofill-control")[1]
    number.click()
    number.clear()
    number.send_keys("7979901194")
    print("Error in mobile number corrected")

if (driver.find_elements_by_class_name("ng-star-inserted")[165].text=="Pin Code must be valid"):
    print("Error detected in pincode")
    pincode = driver.find_elements_by_class_name("mat-form-field-autofill-control")[2]
    pincode.click()
    pincode.clear()
    pincode.send_keys("110030")
    print("Error in pincode corrected")

driver.find_elements_by_class_name("add-new-address")[0].click()

print("New address saved")












