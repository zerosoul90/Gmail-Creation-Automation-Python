# Gmail Account Creation Automation Script - Version 1.1.0
# Original script by Abdelhakim Khaouiti (khaouitiabdelhakim on GitHub)

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from faker import Faker

#chrome_options = ChromeOptions()
#chrome_options.add_argument("--disable-infobars")  # Optional: Disable info bars

service = ChromeService('../../chromedriver.exe')
driver = webdriver.Chrome(service=service) #, options=chrome_options)


# your data
fake = Faker()
your_first_name = fake.first_name()
your_last_name = fake.last_name()
your_username = fake.user_name()+fake.day_of_month()+fake.month()+fake.year() # gama1445pro@gmail.com // make sure to be unique
your_email = your_username+"@gmail.com"
your_birthday = "02 3 1999" #dd m yyyy exp : 24 11 2003
your_gender = "1" # 1:F 2:M 3:Not say 4:Custom
your_password = "x,nscldsj123...FDKZ"

try:
    driver.get("https://account.alibabacloud.com/register/intl_register.htm")

    next_button = driver.find_element(By.LINK_TEXT, "Next")
    next_button.click()

    email_address = driver.find_element(By.ID, "email")
    password_field = driver.find_element(By.ID, "password")
    re_password_field = driver.find_element(By.ID, "confirmPwd")
    email_address.clear()
    email_address.send_keys(your_email)
    password_field.clear()
    password_field.send_keys(your_password)
    re_password_field.clear()
    re_password_field.send_keys(your_password)

    next_button = driver.find_element(By.ID,"account__submit")
    next_button.click()


    # Close the browser window at the end of your automation
    driver.quit()

    print("Your Gmail successfully created:\n{\ngmail: " + your_username + "@gmail.com\npassword: " + your_password + "\n}")


except Exception as e:
    # Close the browser window in case of failure
    driver.quit()
    print("Failed to create your Gmail, Sorry")
    print(e)
