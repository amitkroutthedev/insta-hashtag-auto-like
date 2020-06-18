from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
#secretig.py is for storing username and password
from secretig import username,pw
import random

class InstaBot:
    def __init__(self,username, pw):
        self.bot = webdriver.Chrome()
        self.username = username
        self.pw=pw
    #auto-login with username and password    
    def login(self):
        bot=self.bot
        bot.get("https://instagram.com")
        sleep(3)
        bot.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        bot.find_element_by_xpath("//input[@name='password']").send_keys(self.pw)
        bot.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
        sleep(4)
        bot.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        sleep(2)
        bot.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        sleep(2)
    #searhcing a random hashtag from the list
    def searchHashtag(self,hashtag):
        bot = self.bot
        bot.find_element_by_class_name('XTCLo').send_keys(hashtag)
        bot.get('https://www.instagram.com/explore/tags/' + hashtag)

    def likePhotos(self,amount):
        bot = self.bot
        bot.find_element_by_class_name('v1Nh3').click()
        i = 1
        while i<=amount:
            sleep(4)
            bot.find_element_by_class_name('fr66n').click()
            sleep(2)
            bot.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            sleep(2)
            i += 1

        
    #closing of automation browser
    def closeBrowser(self):
        self.bot.get('https://www.instagram.com/'+self.username)
        self.bot.close()
        

b=InstaBot(username,pw)
b.login()
#different tags
hT=['mobile_click','mobilephotograph','phonography','mobile_photography', 
           'mobilephotographyclub','phonephotography','mobilephotos' ,
           'mobilecapture', 'mobilephoto']
#for a single random hashtag and clicking like in 8 photos
tag=random.choice(hT)
b.searchHashtag(tag)
b.likePhotos(8)
b.closeBrowser()

#for getting all random hashtags
#while(True):
#    try:
#        tag=random.choice(hT)
#        b.searchHashtag(hT)
#        b.likePhotos(50)
#    except Exception:
#        b.closeBrower()
#       sleep(60)
#        b=InstaBot(username,pw)
#       b.login()


