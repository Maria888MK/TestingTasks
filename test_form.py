from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
import re


# Entering data
url = "https://sourceful.nl/nl/contact-pl/"
name = 'Jan Kowalski'
email = 'test@test.com'
subject = 'Test Subject'
message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. '

# XPATHs
name_xpath =  '//input[@name = "your-name"]'
email_xpath = '//input[@name="your-email"]'
subject_xpath = '//input[@name = "your-subject"]'
message_xpath = '//textarea[@name="your-message"]'
submit_xpath = "//input[@value='Wyślij']"
form_msg_xpath = '//div[@class ="wpcf7-response-output"]'


def test_form_all_the_fields(selenium_browser):
    selenium_browser.get(url)
    selenium_browser.find_element(By.XPATH,name_xpath).send_keys(name)
    selenium_browser.find_element(By.XPATH, email_xpath).send_keys(email)
    selenium_browser.find_element(By.XPATH,subject_xpath).send_keys(subject)
    selenium_browser.find_element(By.XPATH, message_xpath).send_keys(message)
    submit_btn = selenium_browser.find_element(By.XPATH, subject_xpath)
    selenium_browser.execute_script("arguments[0].click();", submit_btn)
    # WebDriverWait(selenium_browser, 20).until(EC.presence_of_element_located((By.XPATH, form_msg_xpath)))
    time.sleep(15)
    form_msg = selenium_browser.find_element(By.XPATH,form_msg_xpath).text
    assert re.fullmatch('Dziękujemy, wiadomość została wysłana.', form_msg)

def test_required_fields(selenium_browser):
    selenium_browser.get(url)
    selenium_browser.find_element(By.XPATH, name_xpath).send_keys(name)
    selenium_browser.find_element(By.XPATH, email_xpath).send_keys(email)
    submit_btn = selenium_browser.find_element(By.XPATH, subject_xpath)
    selenium_browser.execute_script("arguments[0].click();", submit_btn)
    # WebDriverWait(selenium_browser, 20).until(EC.presence_of_element_located((By.XPATH, form_msg_xpath)))
    time.sleep(10)
    form_msg = selenium_browser.find_element(By.XPATH,form_msg_xpath).text
    assert re.fullmatch('Dziękujemy, wiadomość została wysłana.', form_msg)





