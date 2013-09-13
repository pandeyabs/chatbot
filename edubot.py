import sys 
import time
import socket 
import string 
import os
#import mechanize
import selenium
from selenium import webdriver
import codecs
from selenium.webdriver.common.by import By

def send_msg(browser, message):
      browser.find_element_by_id('pfc_words').send_keys(message )
      browser.find_element_by_id('pfc_send').click()

def quit_chat(browser):
      browser.find_element_by_id('pfc_loginlogout').click()
      browser.quit()
   
count =0

browser = webdriver.Firefox()
cleverbot = webdriver.Firefox()
cleverbot.get('http://www.cleverbot.com/')

old_string = "asdsadsadasdsadsadas" 

URL = 'http://www.edulix.com/forum/member.php?action=login'
browser.get(URL)
time.sleep(20)

browser.find_element_by_name('username').send_keys('alice6')
browser.find_element_by_name('password').send_keys('choker')
browser.find_element_by_class_name('button').click()

browser.get('http://www.edulix.com/forum/chat/')
time.sleep(20)

while True:
   time.sleep(15)
   
   allelements = browser.find_elements_by_xpath("//*[@id='pfc_chat_f6a004c8995926505f45498596dafcc8']")
   new_string = allelements[0].text

   remain = new_string
   index = new_string.rfind(old_string) 
   if index > -1:
      length = len(old_string)
      remain = new_string[index+length:]

   if (remain.find('edugoogle') > -1):
   #if remain.find('alice6,edugoogle') > -1:
      send_msg(browser, "Here is the edulix-google link: https://www.google.com/cse/home?cx=005962135015314495706:z5kwyszeoi0") 
      #browser.find_element_by_id('pfc_words').send_keys('Here is the edugoogle link: https://www.google.com/cse/home?cx=005962135015314495706:z5kwyszeoi0')
      #browser.find_element_by_id('pfc_send').click()

   if (remain.find('alice6')  > -1) and (remain.find('noob guide') > -1) :
   #if remain.find('alice6,give profile evaluation guide') > -1:
      send_msg(browser,"Guide to profile evaluation: http://www.edulix.com/forum/showthread.php?tid=130448") 

   remain_length = len(remain)
   index2 = remain.rfind('alice6,')
   
   if index2 > -1:
      cleverbot.find_element_by_id('stimulus').send_keys(remain[index2 + len('alice6,'):])
      cleverbot.find_element_by_id('sayit').click()
      time.sleep(10)

      response = cleverbot.find_element_by_id('typArea').text
      if (response.find('Please avoid Unicode')  == -1):  //ignore unicode response
            user = remain[remain.rfind('<', 0, index2 ) + 1 : remain.rfind('>', 0, index2 )] + ', '  //<user>, 
            send_msg(browser, user + response)

   old_string = new_string
   count = count+1
   if count == 30 :
      browser.get('http://www.edulix.com/forum/chat/')
      count =0
