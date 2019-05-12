#_*_ coding=UTF-8 _*_
from selenium import webdriver
 
driver= webdriver.Chrome()
driver.maximize_window()
 
driver.implicitly_wait(3)#wait for 3seconds
 
 
driver.get("https://baidu.com")
driver.quit()