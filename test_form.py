import pytest
from selenium.webdriver.common.by import By
def form_success(selenium_browser):
    selenium_browser.get("https://sourceful.nl/nl/contact-pl/")
    your_name = selenium_browser.find_element(By.XPATH, '//input[@name = "your-name"]')
    your_name.send_keys("Jan Kowalski")
    your_email = selenium_browser.find_element(By.XPATH, '//input[@name="your-email"]')
    your_email.send_keys("test@test.com")
    your_subject = selenium_browser.find_element(By.XPATH, '//input[@name = "your-subject"]')
    your_subject.send_keys("Test Subject")
    your_message = selenium_browser.find_element(By.XPATH, '//textarea[@name="your-message"]')
    your_message.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt "
                           "ut labore et dolore magna aliqua.")
    submit_btn = selenium_browser.find_element(By.XPATH, "//input[@value='Wyślij']")
    selenium_browser.execute_script("arguments[0].click();", submit_btn)
    ### To find a mistake below:
    # form_msg_div = selenium_browser.find_element(By.CLASS_NAME, 'wpcf7-response-output')
    # form_msg = form_msg_div.get_attribute('innerHTML')
    # form_msg = form_msg_div.get_text()
    # print(form_msg)
    # assert re.search("Dziękujemy, wiadomość została wysłana.", form_msg)


