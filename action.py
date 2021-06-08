import pandas as p
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os
import time 
from parsel import Selector
from key import userName, passWord 
options = webdriver.ChromeOptions()


driver = webdriver.Chrome(ChromeDriverManager().install())
data = open(r"/mnt/9fd77f34-e78e-483a-9a58-74645782f0b5/Projects/TPO/LinkedIn Information  (Responses) - Form responses 1.csv", "r")
LINK_Error = open(
    "/mnt/9fd77f34-e78e-483a-9a58-74645782f0b5/Projects/TPO/LINK_Error.csv", "w+")
college_name_error = open(
    "/mnt/9fd77f34-e78e-483a-9a58-74645782f0b5/Projects/TPO/college_name_error.csv", "w+")
driver.get('https://www.linkedin.com')
username = driver.find_element_by_id('session_key')
username.send_keys(userName)
password = driver.find_element_by_id('session_password')
password.send_keys(passWord )
log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
log_in_button.click()
for d in data.readlines():  
    
    dt = list(d.split(","))
    
    driver.get(dt[-1])
    
    try:
        # print(d)
        dt = list(d.split(","))
        # print(dt)
        time.sleep(5)
        driver.get(dt[-1])
        driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        time.sleep(5)
        sel = Selector(text=driver.page_source) 
        time.sleep(5)
        college = sel.xpath('//*[starts-with(@class,"pv-entity__school-name t-16 t-black t-bold")]/text()').extract_first()
        print(college)
        if college != 'Cooch Behar Government Engineering College':
            print(college)
            college_name_error.write(','.join(dt))
    except:
        print(dt)
        LINK_Error.write(','.join(dt))
        continue
    
# driver.close()
