from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
import accountInfoGenerator as account
import getVerifCode as verifiCode
import fakeMail as email



def proxye(x):
    global browser

    # proxy_test = False

    # while not proxy_test:
    if x > 4 :
        x=0

    proxy_list = ["168.81.228.176:3199","168.81.245.195:3199","168.80.37.195:3199",  "168.81.213.51:3199",'168.80.149.191:3199']


    settings = {
        # "httpProxy": "p.webshare.io:19999",
        # "sslProxy": "p.webshare.io:19999",

        "httpProxy": proxy_list[x],
        "sslProxy": proxy_list[x],

    }
    print(proxy_list[x])
    proxy = Proxy( settings )

    cap = DesiredCapabilities.CHROME.copy()

    cap['platform'] = "WINDOWS"
    cap['version'] = "10"
    proxy.add_to_capabilities( cap )



    opt = Options()
    opt.binary_location = "C:\Program Files\Google\Chrome Beta\Application\chrome.exe"
    browser = ChromeDriver( desired_capabilities=cap , options=opt, executable_path="drivers/chromedriver.exe")
    browser.maximize_window()
    # driver.get( 'https://whatismyipaddress.com/' )
    # facbook_first_page = input( 'enter any key: ' )
    browser.get( 'https://www.instagram.com/accounts/emailsignup/' )


    # facbook_second_page=input('enter any key: ')






    # x +=1
    #
    # user_proxy_test = input( 'if you want new proxy any keyes and if want contuniu enter (0): ' )
    # if user_proxy_test == "0":
    #     proxy_test = True

def code():
    # Fill the fullname value
    fullname_field = browser.find_element_by_name( 'fullName' )
    fullname_field.send_keys( account.generatingName() )
    print( account.generatingName() )
    user_name = account.generatingName()
    user_name = user_name.replace( " ", "_" )
    user_name_f = ""
    o = 0
    for i in user_name:
        if o < 14:
            # print(i)
            user_name_f += i
        o += 1

    # Fill username value
    username_field = browser.find_element_by_name( 'username' )
    # username_field.send_keys(name)
    username_field.send_keys( user_name_f.lower() )
    print( user_name_f.lower() )
    # time.sleep(10)
    # Fill password value
    password_field = browser.find_element_by_name( 'password' )
    password_field.send_keys( 'ammar0599' )
    # if email_opt == 0:
    #     password_field.send_keys(pass_opt)  # You can determine another password here.
    # if email_opt != 0:
    #     password_field.send_keys(account.generatePassword())  # You can determine another password here.
    #     print(account.generatePassword())
    WebDriverWait( browser, 20 ).until( EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button") ) ).click()

    time.sleep( 8 )

    # Birthday verification
    browser.find_element_by_xpath(
        "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select" ).click()
    WebDriverWait( browser, 20 ).until( EC.element_to_be_clickable( (By.XPATH,
                                                                     "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]") ) ).click()

    browser.find_element_by_xpath(
        "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select" ).click()
    WebDriverWait( browser, 20 ).until( EC.element_to_be_clickable( (By.XPATH,
                                                                     "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]") ) ).click()

    browser.find_element_by_xpath(
        "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select" ).click()
    WebDriverWait( browser, 20 ).until( EC.element_to_be_clickable( (By.XPATH,
                                                                     "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]") ) ).click()

    WebDriverWait( browser, 20 ).until( EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button") ) ).click()
    time.sleep( 3 )
    #

email_opt=int(input('if you want put your emails enter 0 if fake email enter any numper: '))
proxy_opt=int(input('if you want proxy enter 0 if not enter any numper: '))
# if email_opt == 0:
#     pass_opt=input('Enter instgram account password: ')
if proxy_opt == 0:
    proxy_num=int(input('Enter proxy numper: '))
if proxy_opt != 0:
    print('proxy_opt != 0')

name = account.username()



if email_opt == 0:
    file1 = open( 'emails.txt', 'r' )
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        # print( line )
        if proxy_opt == 0:
            proxye( proxy_num )
        if proxy_opt != 0:
            browser = webdriver.Chrome( "drivers/chromedriver.exe" )
            browser.get( "https://www.instagram.com/accounts/emailsignup/" )

        time.sleep( 8 )
        # Fill the email value
        email_field = browser.find_element_by_name( 'emailOrPhone' )

        fake_email = line
        email_field.send_keys( fake_email )
        print( fake_email )
        code()


if email_opt != 0:
    fake_email = email.getFakeMail()
    email_field.send_keys( fake_email )
    print( fake_email )
    code()

    fMail = fake_email[0].split( "@" )
    mailName = fMail[0]
    domain = fMail[1]
    instCode = verifiCode.getInstVeriCode( mailName, domain, browser )
    browser.find_element_by_name( 'email_confirmation_code' ).send_keys( instCode, Keys.ENTER )



