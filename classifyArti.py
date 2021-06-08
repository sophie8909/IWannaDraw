from classifyFunct import *
from nlppre import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
from bs4 import BeautifulSoup
import re
from filefunct import *

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values':{'notifications': 2}}
options.add_experimental_option('prefs', prefs)
options.add_argument("--incognito")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

#options.add_argument("--headless")

driver = webdriver.Chrome(options=options,executable_path=r"C:\Users\User\Desktop\chromedriver.exe")

driver.get("https://mbasic.facebook.com/")
element = driver.find_element_by_name("email")
element.send_keys("testforclass2021@gmail.com")
element = driver.find_element_by_name("pass")
element.send_keys("testforclass")
element = driver.find_element_by_name("login")
element.click()


def getArti(address):
    driver.get(address)
    time.sleep(3)
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc,'html.parser')
    text = soup.get_text()
    driver.close()
    return (text[text.find("前往首頁")+4:text.find("所有人說這專頁讚 · 儲存 · 更多讚傳達心情留言分享")].replace('\"', " "))

# 輸入一篇文章，判斷是不是抽獎文
if __name__ == '__main__':
    # 輸入欲判斷的 FB 網址
    address = input("輸入欲判斷的 FB 粉專貼文網址（限　https://mbasic.facebook.com/　文章）：\n")
    #address = "https://mbasic.facebook.com/story.php?story_fbid=118025430437876&id=101969802043439&refid=17&_ft_=mf_story_key.118025430437876%3Atop_level_post_id.118025430437876%3Atl_objid.118025430437876%3Acontent_owner_id_new.101969802043439%3Athrowback_story_fbid.118025430437876%3Apage_id.101969802043439%3Astory_location.4%3Astory_attachment_style.photo%3Atds_flgs.3%3Aott.AX8dwmUrG3YqrPGW%3Athid.101969802043439%3A306061129499414%3A2%3A0%3A1622530799%3A-4754782940264262493&__tn__=%2As-R"
    inputSTR = getArti(address)
    articut = articutLogIn("./account.info")
    cuttedDICT = articutProcessing(inputSTR,articut,"lv1")
    wordList = articut2cleanWordList(cuttedDICT["result_segmentation"])
    if classify_lv1( wordList) == True:
        print( "他可能是抽獎文喔！！\n")
    else:
        print("我覺得他跟抽獎文沒有關係\n")