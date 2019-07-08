import time

from selenium import webdriver

TEST_HOST = "https://stage.dailyobjects.com"

driver = webdriver.Chrome()

driver.get("{}/auth/login".format(TEST_HOST))

phone_number = driver.find_elements_by_class_name("mat-form-field-autofill-control")[0]
phone_number.click()
phone_number.send_keys("9999999999")

driver.find_elements_by_class_name("get-otp-btn")[0].click()

time.sleep(5)

otp_input = driver.find_elements_by_class_name("otp-input")[0]
otp_input.click()
otp_input.send_keys("8888")

time.sleep(5)

driver.find_elements_by_class_name("login-btn")[0].click()

driver.maximize_window()

time.sleep(10)

driver.find_elements_by_class_name("image")[0].click()

time.sleep(10)

driver.find_elements_by_class_name("breadcrumb-block")[0].click()

driver.find_element_by_class_name("add-cart").click()

time.sleep(10)

driver.find_element_by_class_name("cart").click()

time.sleep(10)

payable_amount_before_checkout = driver.find_elements_by_class_name("total-payble")[1].text
print('Amount before checkout: ' + payable_amount_before_checkout)
payable_amount_before_checkout = float(payable_amount_before_checkout[1:])

driver.find_element_by_class_name("go-to-checkout").click()

time.sleep(5)

payable_amount_after_checkout = driver.find_elements_by_class_name("total-payble")[1].text
print('Amount after checkout: ' + payable_amount_after_checkout)
payable_amount_after_checkout = float(payable_amount_after_checkout[1:])

driver.find_elements_by_class_name("mat-button")[2].click()

time.sleep(10)

driver.find_elements_by_class_name("checkout-pay-option-list")[2].click()

time.sleep(5)

card_number = driver.find_elements_by_class_name("cdk-text-field-autofill-monitored")[0]
card_number.click()
time.sleep(5)
card_number.send_keys("5123456789012346")

name_on_card = driver.find_elements_by_class_name("mat-form-field-autofill-control")[1]
name_on_card.click()
time.sleep(1)
name_on_card.send_keys("Superman")

driver.find_elements_by_class_name("mat-form-field-infix")[3].click()
time.sleep(1)
driver.find_elements_by_class_name("mat-option-text")[4].click()

driver.find_elements_by_class_name("mat-form-field-infix")[4].click()
time.sleep(1)
driver.find_elements_by_class_name("mat-option-text")[1].click()

cvv = driver.find_elements_by_class_name("mat-form-field-autofill-control")[2]
cvv.click()
time.sleep(1)
cvv.send_keys("123")

time.sleep(1)

driver.find_elements_by_class_name("card-pay-button")[0].click()

time.sleep(20)

paid_amount = driver.find_elements_by_class_name("even")[1].text
paid_amount = paid_amount.replace(",", "")
print('Paid amount: ' + paid_amount)
paid_amount = float(paid_amount[1:])

print(driver.find_elements_by_class_name("text-center")[0].text)

if driver.find_elements_by_class_name("text-center")[
    0].text == 'Thank you for your order!' \
        and payable_amount_before_checkout == payable_amount_after_checkout \
        and payable_amount_after_checkout == paid_amount:
    print('Transaction took place without hiccups :D')
