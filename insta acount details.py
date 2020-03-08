from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import datetime
import time
import os
driver = webdriver.Chrome('C:\\Users\\NEW\\Downloads\\chromedriver.exe')
driver.get("https://www.instagram.com")
time.sleep(1.5)
n=int(input("To login via facebook press 1, To login via instagram press 2: "))
if n==1:
    driver.find_element_by_class_name('KPnG0').click()
    time.sleep(1.25)
    id = driver.find_element_by_id('email')
    id.send_keys("7825968223")
    password = driver.find_element_by_id('pass')
    password.send_keys("rupesh1183")
    driver.find_element_by_id("loginbutton").click()
    time.sleep(5)
else:
    driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(1.25)
    username=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
    username.send_keys('this_is_rupeshkj')
    passwordinsta=driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input')
    passwordinsta.send_keys('rupesh1104')
    driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4)').click()
    time.sleep(8)
driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm').click()
time.sleep(3)
driver.get("https://www.instagram.com/accounts/access_tool/")
time.sleep(3)
driver.get('https://www.instagram.com/accounts/access_tool/accounts_following_you')
for i in range(0,1000):
    try:
        driver.find_element_by_css_selector('#react-root > section > main > div > article > main > button').click()
        driver.send_keys(Keys.PAGE_DOWN)
    except:
        pass
    print(i,end="\r")
Accounts_following_you=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/main/section')
Accounts_following_you=Accounts_following_you.text
Accounts_following_you=Accounts_following_you.split('\n')    
driver.get("https://www.instagram.com/accounts/access_tool/accounts_you_follow")
for i in range(0,1000):
    try:
        driver.find_element_by_css_selector('#react-root > section > main > div > article > main > button').click()
        driver.send_keys(Keys.PAGE_DOWN)
        print("trying",end="\r")
    except:
        pass
    print(i,end="\r")
Accounts_you_follow=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/main/section')
Accounts_you_follow=Accounts_you_follow.text
Accounts_you_follow=Accounts_you_follow.split('\n')    
driver.close()
file=open("Instagram account details.txt",'w',encoding="utf-8")
file.write('+-----------------------------------------------------+\n')
file.write("|=========Rupesh Instagram account analyser===========|\n")
file.write('+-----------------------------------------------------+\n')
today=str(datetime.datetime.today())
file.write("Details on data and time: ")
file.write(today)
file.write('\n')
file.write('------------------------------------------------------\n')
file.write("people who don't follow you\n")
file.write('------------------------------------------------------\n')
for i in Accounts_you_follow:
    for j in Accounts_following_you:
        if i==j:
            r=1
            break
        else:
            r=0
    if r==0:
        print(i,'is not following you')
        file.write(i)
        file.write(" ")
        file.write('is not following you\n')
file.write('\n------------------------------------------------------\n')
file.write("people who you don't follow\n")
file.write('------------------------------------------------------\n')
write_you_not_following=[]
for i in Accounts_following_you:
    for j in Accounts_you_follow:
        if i==j:
            r=1
            break
        else:
            r=0
    if r==0:
        print('You are not following ', i)
        file.write('You are not following')
        file.write(" ")
        file.write(i)
        file.write("\n")
file.close()


