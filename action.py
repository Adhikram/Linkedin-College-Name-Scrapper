import pandas as p
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os
import time 
from parsel import Selector
options = webdriver.ChromeOptions()


driver = webdriver.Chrome(ChromeDriverManager().install())
data = open(r"/mnt/9fd77f34-e78e-483a-9a58-74645782f0b5/Projects/TPO/LinkedIn Information  (Responses) - Form responses 1.csv", "r")
LINK_Error = open(
    "/mnt/9fd77f34-e78e-483a-9a58-74645782f0b5/Projects/TPO/LINK_Error.csv", "w+")
college_name_error = open(
    "/mnt/9fd77f34-e78e-483a-9a58-74645782f0b5/Projects/TPO/college_name_error.csv", "w+")
driver.get('https://www.linkedin.com')
username = driver.find_element_by_id('session_key')
username.send_keys('adhikramm@gmail.com')
password = driver.find_element_by_id('session_password')
password.send_keys('hotfat999')
log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
log_in_button.click()
time.sleep(1)
skip_button = driver.find_element_by_class_name('secondary-action')
skip_button.click()
for d in data.readlines():  
    
    dt = list(d.split(","))
    
    driver.get(dt[-1])
    
    try:
        # print(d)
        dt = list(d.split(","))
        # print(dt)
        time.sleep(5)
        driver.get(dt[-1])
        time.sleep(5)
        sel = Selector(text=driver.page_source) 
        time.sleep(5)
        college = sel.xpath('//*[starts-with(@class,"text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view")]/text()').extract_first()
        if college:
            college = college.strip()
        if college != 'Cooch Behar Government Engineering College':
            print(name,college)
            college_name_error.write(','.join(dt))
    except:
        print(dt)
        LINK_Error.write(','.join(dt))
        continue
    
# driver.close()
