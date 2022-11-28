from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re
from selenium.webdriver.common.by import By


# options = Options()
# options.headless = True
driver = webdriver.Firefox()
driver.get("https://sourceful.nl/nl/contact-pl/")
your_name = driver.find_element(By.XPATH, '//input[@name = "your-name"]')
your_name.send_keys("Jan Kowalski")
# your_email = driver.find_element(By.XPATH, '//input[@name="your-email"]')
# your_email.send_keys("test@test.com")
# your_subject = driver.find_element(By.XPATH, '//input[@name = "your-subject"]')
# your_subject.send_keys("Test Subject")
# your_message = driver.find_element(By.XPATH, '//textarea[@name="your-message"]')
# your_message.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt "
#                        "ut labore et dolore magna aliqua.")
submit_btn = driver.find_element(By.XPATH, "//input[@value='Wyślij']")
print("Element is visible? " + str(submit_btn.is_displayed()))
driver.execute_script("arguments[0].click();", submit_btn)

# form_msg_div = driver.find_element(By.CLASS_NAME, 'wpcf7-response-output')
print(driver.find_element(By.CLASS_NAME, 'wpcf7-response-output').text)
# form_msg = form_msg_div.get_attribute("textContent")
# print(form_msg)
# assert form_msg_div =='One or more fields have an error. Please check and try again.'

# # form_msg = form_msg_div.get_text()
# print(form_msg_div)
# if re.search("One or more fields have an error. Please check and try again.",form_msg_div):
#     print('ok')
# # assert re.search("One or more fields have an error. Please check and try again.", form_msg_div)







driver.quit()