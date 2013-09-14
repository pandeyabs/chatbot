# coding: utf-8
import sys 
import time
import socket 
import string 
import os
import selenium
import codecs
from selenium.webdriver.common.by import By
from selenium import webdriver
# http://coreygoldberg.blogspot.com/2011/06/python-headless-selenium-webdriver.html
from pyvirtualdisplay import Display
#replace it later with xvfbwrapper, which is lighter https://pypi.python.org/pypi/xvfbwrapper

def send_msg(browser, message):
      browser.find_element_by_id('pfc_words').send_keys(message )
      browser.find_element_by_id('pfc_send').click()

def quit_chat(browser):
      browser.find_element_by_id('pfc_loginlogout').click()
      browser.quit()
   
count =0

display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Firefox()
cleverbot = webdriver.Firefox()
cleverbot.get('http://www.cleverbot.com/')

old_string = "asdsadsadasdsadsadas" 

URL = 'http://www.edulix.com/forum/member.php?action=login'
browser.get(URL)
time.sleep(20)

name = 'alice6'
mods = ['opeth', 'Wololo', 'Black Knight']

browser.find_element_by_name('username').send_keys(name)
browser.find_element_by_name('password').send_keys('choker')
browser.find_element_by_class_name('button').click()

browser.get('http://www.edulix.com/forum/chat/')
time.sleep(20)

while True:
   #try to reduce this sleep as much as possible
   time.sleep(5)
   
   allelements = browser.find_elements_by_xpath("//*[@id='pfc_chat_f6a004c8995926505f45498596dafcc8']")
   new_string = allelements[0].text.encode('utf-8','replace').replace('‹','<').replace('›','>').decode('ascii','ignore')

   remain = new_string
   index = new_string.rfind(old_string) 
   if index > -1:
      length = len(old_string)
      remain = new_string[index+length:]

   if (remain.find('edugoogle') > -1):
      send_msg(browser, "Here is the edulix-google link: https://www.google.com/cse/home?cx=005962135015314495706:z5kwyszeoi0") 

   if (remain.find('noob guide') > -1) :
      send_msg(browser,"Guide to profile evaluation: http://www.edulix.com/forum/showthread.php?tid=130448") 

   index2 = remain.rfind(name + ',')
   
   if index2 > -1 :
      #get the user who addressed
      user = remain[remain.rfind('<', 0, index2) + 1 : remain.rfind('>', 0, index2)]
      #get the command till newline. earlier it took even the chat messages which were not addressed to it below it, producing incorrect results.
      command = remain[index2 + len(name + ',') : remain[index2 + len(name + ','):].find('\n') + index2 + len(name + ',')]
      #make it quit if one of the mods asks it to
      if (user in mods) and (command == " quit") :
         quit_chat(browser)
         break
      else :
         cleverbot.find_element_by_id('stimulus').send_keys(command)
         cleverbot.find_element_by_id('sayit').click()
         time.sleep(10)

         response = cleverbot.find_element_by_id('typArea').text
         if response.find('Unicode')  == -1 :
            send_msg(browser, user + ', ' + response)

   old_string = new_string
   count = count+1
   if count == 30 :
      #clear chat instead of refreshing page
      send_msg(browser, "/clear")
      count =0
