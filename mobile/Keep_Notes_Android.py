from appium import webdriver
from selenium.webdriver.common.by import By
from applitools.selenium import Eyes
import time

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9.0",
    "deviceName": "Pixel 2",
    # "automationName": "Appium",
    # "app": 	'//android.widget.TextView[@content-desc="Keep Notes"]'

}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities)
# Open app
driver.find_element(By.XPATH,'//android.widget.TextView[@content-desc="Keep Notes"]').click()
# driver.find_element(By.ID,'Keep Notes').click()
time.sleep(2)
# Creating note
# driver.find_element(By.ID,'com.google.android.keep:id/new_note_button').click()
# time.sleep(5)
# title = driver.find_element(By.ID, 'com.google.android.keep:id/editable_title')
# title.send_keys("Test title")
# body = driver.find_element(By.ID, 'com.google.android.keep:id/edit_note_text')
# body.send_keys('Test body')