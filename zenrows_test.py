from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from anticaptchaofficial.turnstileproxyless import *
import time

# Step 1: Launch Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Step 2: Open the ZenRows website
driver.get("https://www.zenrows.com/")
time.sleep(5)

# Step 3: Click "Start free trial" button
start_trial_button = driver.find_element(By.XPATH, "//span[normalize-space()='Start Free Trial']")
start_trial_button.click()
time.sleep(5)


# Step 5: Solve Turnstile CAPTCHA using Anti-Captcha API
solver = turnstileProxyless()
solver.set_key("11eeb3f3b838db1a3fffd5346e1ba3b9")  
solver.set_website_url(driver.current_url)

# Replace with the Turnstile site key (inspect page source to find it)
solver.set_website_key("0x4AAAAAAADnPIDROrmt1Wwj")  

# Solve CAPTCHA
token = solver.solve_and_return_solution()

if token != 0:
    print("CAPTCHA Solved. Token: " + token)

    
    driver.execute_script(
        f'document.getElementById("cf-turnstile-response").value="{token}";'
    )
    time.sleep(2)

    
    driver.find_element(By.ID, "submit").click()
else:
    print("Failed to solve CAPTCHA. Error: " + solver.error_code)

# Wait for the next page
time.sleep(5)

# Close the browser
driver.quit()
