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
#chromedriver = "/home/pandey/chromedriver"
#os.environ["webdriver.chrome.driver"] = chromedriver
#browser = webdriver.Chrome(chromedriver)
browser = webdriver.Firefox()
cleverbot = webdriver.Firefox()
cleverbot.get('http://www.cleverbot.com/')
#cleverbot_driver = webdri
old_string = "asdsadsadasdsadsadas" 
#browser = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.HTMLUNITWITHJS)
#URL = 'http://ca.purvesh.net/chat/'
URL = 'http://www.edulix.com/forum/member.php?action=login'
browser.get(URL)
time.sleep(20)
#browser.find_element_by_id('pfc_promptbox_field').send_keys('bot-test')
#browser.find_element_by_id('pfc_promptbox_submit').click()
browser.find_element_by_name('username').send_keys('alice6')
browser.find_element_by_name('password').send_keys('password')
browser.find_element_by_class_name('button').click()
#filen = codecs.open('output.txt', encoding='utf-8', mode='w+')
browser.get('http://www.edulix.com/forum/chat/')
time.sleep(20)
while True:
   #browser.get('http://www.edulix.com/forum/chat/')
   time.sleep(15)
   #allelements = browser.find_elements_by_xpath("//*[starts-with(@id='pfc_msgwa')]")
   #allelements = browser.find_elements_by_xpath("//*[@id='pfc_msg_f6a004c8995926505f45498596dafcc8_3539']")
   allelements = browser.find_elements_by_xpath("//*[@id='pfc_chat_f6a004c8995926505f45498596dafcc8']")
   new_string = allelements[0].text
   #print "the string follows"
   #print old_string
   #print new_string
   remain = new_string
   index = new_string.rfind(old_string) 
   if index > -1:
      length = len(old_string)
      remain = new_string[index+length:]
      #global old_string
      #print remain
      #old_string = new_string
      #if remain.find('hnnghh,edugoogle') > -1:
      #   browser.find_element_by_id('pfc_words').send_keys('Here is the edugoogle link: https://www.google.com/cse/home?cx=005962135015314495706:z5kwyszeoi0')
      #   browser.find_element_by_id('pfc_send').click()
   #else :
   #   old_string = new_string
   #   if new_string.find('hnnghh,edugoogle') > -1:
   #      browser.find_element_by_id('pfc_words').send_keys('Here is the edugoogle link: https://www.google.com/cse/home?cx=005962135015314495706:z5kwyszeoi0')
   #      browser.find_element_by_id('pfc_send').click()
      #Profile evaluation guide? 
   if (remain.find('edugoogle') > -1):
   #if remain.find('alice6,edugoogle') > -1:
      send_msg(browser, "Here is the edulix-google link: https://www.google.com/cse/home?cx=005962135015314495706:z5kwyszeoi0") 
      #browser.find_element_by_id('pfc_words').send_keys('Here is the edugoogle link: https://www.google.com/cse/home?cx=005962135015314495706:z5kwyszeoi0')
      #browser.find_element_by_id('pfc_send').click()

   if (remain.find('alice6')  > -1) and (remain.find('noob guide') > -1) :
   #if remain.find('alice6,give profile evaluation guide') > -1:
      send_msg(browser,"Guide to profile evaluation: http://www.edulix.com/forum/showthread.php?tid=130448") 
   #browser.get('http://www.cleverbot.com/')
   #if remain.find('hnnghh,quit') > -1:
      #send_msg(browser,"okbai :\(")
      #quit_chat(browser)
      #browser.find_element_by_id('pfc_words').send_keys('Here is the profile evaluation link: http://www.edulix.com/forum/showthread.php?tid=130448' )
      #browser.find_element_by_id('pfc_send').click()
   
   remain_length = len(remain)
   index2 = remain.rfind('alice6,') 
   #unichar_index1 = remain.rfind('<')
   #unichar_index2 = remain.rfind('>')
   #sender_name = remain[unichar_index1+1:unichar_index2-1]
   #print "SENDER SENDER"
   #print sender_name
   if index2 > -1:
      cleverbot.find_element_by_id('stimulus').send_keys(remain[index2 + len('alice6,'):])
      cleverbot.find_element_by_id('sayit').click()
      time.sleep(10)
      #unichar_index1 = remain.find('<')
      #unichar_index2 = remain.find('>')
      #sender_name = remain[unichar_index1+1:unichar_index2-1]
      #print "SENDER SENDER"
      #print sender_name
      response = cleverbot.find_element_by_id('typArea').text
      send_msg(browser, response)
   #if remain_length >15 :
   #   cleverbot.find_element_by_id('stimulus').send_keys(remain[remain_length-15:remain_length-1])
   #   cleverbot.find_element_by_id('sayit').click()
   #else :
   #   cleverbot.find_element_by_id('stimulus').send_keys('Who is your daddy?')
   #   cleverbot.find_element_by_id('sayit').click()
   #wait for response from clverbot
   #time.sleep(10)
   #response = cleverbot.find_element_by_id('typArea').text
   #print "response"
   #print response
   old_string = new_string
   count = count+1
   if count == 30 :
      #browser.get(URL)
      browser.get('http://www.edulix.com/forum/chat/')
      count =0
   #allelements = browser.find_elements_by_xpath("//*[@id='pfc_channels_content']")
   #to quit or enter
   #browser.find_element_by_id('pfc_loginlogout').click()
   #print allelements[0].text
   #print "the string follows"
   #print s
   #if s.find('hnnghh,edugoogle') > -1:
   #   browser.find_element_by_id('pfc_words').send_keys('Here is the edugoogle link: https://www.google.com/cse/home?cx=005962135015314495706:z5kwyszeoi0')
   #   browser.find_element_by_id('pfc_send').click()
   #
   #browser.get(URL)
   #browser.get('http://www.edulix.com/forum/chat/')
   #allelements = browser.find_elements_by_xpath("//*[@id='pfc_msg_f6a004c8995926505f45498596dafcc8_3540']")
   #print allelements[0].text
   #print allelements.text
   #all_words = browser.find_element_by_class_name('pfc_message')
   #all_words = browser.find_element_by_class_name('pfc_words')
   #all_words = browser.find_elements(By.CLASS_NAME, "pfc_words")
   #all_words = browser.find_elements(By.CLASS_NAME, "pfc_message")
   #print all_words.text
   #all_words.getAttribute("innerHTML")
   #for options in all_words:
   #   print options
   #browser.find_element_by_id('pfc_words').send_keys('jimpu2 :loudspeaker:')
   #browser.find_element_by_id('pfc_send').click()
   #allelements = browser.find_elements_by_xpath("//*")
   ##if allelements.find('hnnghh,edugoogle') == -1:
#   ferdigtxt = []
#   for i in allelements:
#         if i.text in ferdigtxt:
#             pass
#         else:
#            ferdigtxt.append(i.text)
#            #filen.writelines(i.text)
#	    print i.text
   #if 'hnnghh,edugoogle' in filen.read():
   #for i in allelements:
      #if any("hnnghh,edugoogle" in s for s in i.text):
   #   browser.find_element_by_id('pfc_words').send_keys('Here is the edugoogle link: https://www.google.com/cse/home?cx=005962135015314495706:z5kwyszeoi0')
   #   browser.find_element_by_id('pfc_send').click()
   #else:
   #   continue 
#filen.close()

#def main():
#   br.select_form(nr=0)
#   br.form['username'] = 'hnnghh'
#   br.form["password"] = 'choker'
#   results = br.submit().read()
#   f = file('test.html', 'w')
#   f.write(results)
#   f.close()
#   #br = mechanize.Browser()
#   #br.set_handle_robots(False)
#   #br.open('http://www.edulix.com/forum/showthread.php?tid=137471')
#   #html = br.response().read()
#   #f1 = file('thread.html','w')
#   #f1.write(html)
#   #f1.close()
#   br.open('http://www.edulix.com/forum/chat/');
#   html = br.response().read()
#   assert br.viewing_html()
#   time.sleep(50)
#   f1 = file('thread.html','w')
#   f1.write(html)
#   f1.close()
#   
#    #session = requests.session(config={'verbose': sys.stderr})
#
#    ## This is the form data that the page sends when logging in
#    #login_data = {
#    #    'loginemail': EMAIL,
#    #    'loginpswd': PASSWORD,
#    #    'submit': 'login',
#    #}
#
#    ## Authenticate
#    #r = session.post(URL, data=login_data)
#
#    ## Try accessing a page that requires you to be logged in
#    #r = session.get('http://friends.cisv.org/index.cfm?fuseaction=user.fullprofile')
#
#if __name__ == '__main__':
#    main()
