from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import time
import re

appium = "http://localhost:4723/wd/hub"

# Set up the desired capabilities
desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "13.0",
    "deviceName": "Pixel 4 ",
    "automationName": "Appium",
}
# Create WebDriver instance and connect to the Appium server
driver = webdriver.Remote(appium, desired_capabilities)

# Open the Keep Notes App
driver.find_element(By.XPATH, '//android.widget.TextView[@content-desc="Keep Notes"]').click()
time.sleep(2)

# Locate and click on the new note button
driver.find_element(By.ID,'com.google.android.keep:id/new_note_button').click()
time.sleep(2)

# Locate and fill out the title field
title = driver.find_element(By.ID, 'com.google.android.keep:id/editable_title')
title.send_keys("Test title")

# Locate and fill out the body field
body = driver.find_element(By.ID, 'com.google.android.keep:id/edit_note_text')
body.send_keys('Test body')

# Back to the list of notes
back_to_notes =driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]').click()
time.sleep(2)

# Click on the last created note
TouchAction(driver).tap(None, 270, 415, 1).perform()

# Find out timestamp field and get text
timestamp_field = driver.find_element(By.ID, 'com.google.android.keep:id/bs_timestamp').text

# Check out if the note was created
assert re.match("Edited", timestamp_field)

# Close the Keep Notes App
driver.swipe(start_x=555, start_y=2242, end_x=555, end_y=1221, duration=800)

# Terminate WebDriver session
driver.quit()