from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

import pandas as pd
from time import sleep
import string  # for string constants
import random  # for generating random strings
import time
import email
import imaplib

TARGET_URL = "https://dhl-nl.benefitsatwork.eu/registration?lang=en"
LOGIN_URL = "https://dhl-nl.benefitsatwork.eu/login"
LOGOUT_URL = "https://dhl-nl.benefitsatwork.eu/logout"
TASK_URL = "https://dhl-nl.benefitsatwork.eu/offer/27293/cat/2790"
SUFFIX_MAIL = "{}@leavology.nl"
REGISTER_CODE = "DHL2019"
username = 'all@leavology.nl'
password = 'f~zC.GWD*j4V'
dysonCode = []



def register_step():

    # Generate First Name and Last Name and Email
    random_first_name = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(5)])
    random_last_name = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(5)])
    random_mail = SUFFIX_MAIL.format(''.join([random.choice(string.ascii_letters + string.digits) for i in range(5)]))
    random_password = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(10)])
    

    # Run Chrome Driver
    driver = webdriver.Chrome()
    driver.set_window_size(1200, 800)
    driver.get(TARGET_URL)

    # Enter the Keys
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//form[1]/fieldset[1]/div[1]/div/div/select/option[2]"))).click()
        print("Mr. Clicked!")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//form[1]/fieldset[1]/div[2]/div[1]/input"))).send_keys(random_first_name)
        print("First Name is inputed!")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//form[1]/fieldset[1]/div[2]/div[2]/input"))).send_keys(random_last_name)
        print("Last Name is inputed!")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//form[1]/fieldset[2]/div[1]/fieldset/div[3]/label"))).click()
        print("Private Email Item is clicked!")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//form[1]/fieldset[2]/fieldset[2]/div[1]/div/input"))).send_keys(random_mail)
        print("Random Email is inputed!")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//form[1]/fieldset[2]/fieldset[2]/div[2]/div/input"))).send_keys(REGISTER_CODE)
        print("Register Code is inputed!")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//form[1]/fieldset[2]/div[2]/div/input"))).send_keys(random_password)
        print("Password is inputed!")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//form[1]/fieldset[2]/div[3]/div/input"))).send_keys(random_password)
        print("Password is Confirmed!")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        driver.implicitly_wait(10)
        checkbox = driver.find_element(By.XPATH, "//form[1]/fieldset[3]/div[2]/div/input")
        driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2]);", checkbox, "checked", "true")
        print("T&C is checked!")
    except TimeoutException:
        print ("Loading took too much time!")
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//form[1]/div[2]/div[3]/input"))).click()
        print("Register Button Clicked!")
    except TimeoutException:
        print ("Loading took too much time!")
    
    time.sleep(10)
    activation_code = receive_code()
    
    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "registrationDoiData[activationCode]"))).send_keys(activation_code)
        print("Activation code is inputed!")
    except TimeoutException:
        print ("Loading took too much time!")

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "cbg3-submit"))).click()
        print("Activation button is clicked!")
    except TimeoutException:
        print ("Loading took too much time!")
    
    # Go to Login
    driver.get(LOGIN_URL)
    time.sleep(10)

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "loginData[email]"))).send_keys(random_mail)
        print("LogIn Mail is inputed!")
    except TimeoutException:
        print ("Loading took too much time!")
    
    time.sleep(3)

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "loginData[password]"))).send_keys(random_password)
        print("LogIn Password is inputed!")
    except TimeoutException:
        print ("Loading took too much time!")

    time.sleep(5)

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "cbg3-submit-login"))).click()
        print("LogIn Button is clicked!")
    except TimeoutException:
        print ("Loading took too much time!")

    # popup message accept

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "cbg3-submit"))).click()
        print("Offer Accept Button is clicked!")
    except TimeoutException:
        print ("Loading took too much time!")

    # Go to Target URL

    driver.get(TASK_URL)

    try:
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-offerid='27293']"))).click()
        print("Generate Button is clicked!")
    except TimeoutException:
        print ("Loading took too much time!")

    time.sleep(5)

    try:
        gotCode = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[@data-request-id='code-84227']"))).text
        print("Got Result Code!!!", gotCode)
    except TimeoutException:
        print ("Loading took too much time!")


    dysonCode.append(gotCode)

    # Log Out
    driver.get(LOGOUT_URL)
    # Driver quit
    driver.quit()
    

# Receive Activation Code from leavolgy.nl.
def receive_code():
    mail = imaplib.IMAP4_SSL (host='mail.leavology.nl', port=993,timeout=None)
    mail.login(username,password)
    mail.select('Inbox')

    status,results = mail.search(None, 'ALL')

    if status == "OK":
        for result in results[0].split():
            status, data = mail.fetch(result,'(RFC822)')
            msg = email.message_from_bytes(data[0][1])
        str_res = str(msg.get_payload(decode=True))
        res_str = str_res.split(' ')
        ress = res_str[13][0:10]
        return ress

# Export TXT file
def export_txt(dysonCode):
    with open('result.txt', 'w') as file:
    	file.writelines("%s\n" % line for line in dysonCode)

def main():
    counter = 0
    while True:
        counter += 1
        register_step()
        if counter == 3:
            break
    export_txt(dysonCode)

main()
