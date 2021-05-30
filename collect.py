from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import time
from bs4 import BeautifulSoup
import re

# 在windows 平台下運作 執行前請將 chromedriver.exe 放入與本程式同資料夾

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

def get_doc(url):
    driver.get(url)
    time.sleep(3)
    html_doc = driver.page_source
    soup = BeautifulSoup(html_doc, 'html.parser')
    return soup

def get_post(soup):
    list = []
    for link in soup.find_all('a'):
        if("更多" in link ):
            list.append("https://mbasic.facebook.com"+link.get('href'))
    return list 

time.sleep(3)
pattern = re.compile(r'<.*?>')
f = open('output.txt', 'w',encoding="utf-8")

page_url_list = []
page_url_list.append("https://mbasic.facebook.com/2021師大資工週-101969802043439/")
page_url_list.append("https://mbasic.facebook.com/NVIDIAGeForceTW/")
page_url_list.append("https://mbasic.facebook.com/buy123TW/")
page_url_list.append("https://mbasic.facebook.com/miramarcinemas/")
page_url_list.append("https://mbasic.facebook.com/ShopeeTW/")
page_url_list.append("https://mbasic.facebook.com/ElevenSportsTaiwan/")
page_url_list.append("https://mbasic.facebook.com/HACweb/")
page_url_list.append("https://mbasic.facebook.com/TarokoSquare/")
page_url_list.append("https://mbasic.facebook.com/egmangaFiction/")
page_url_list.append("https://mbasic.facebook.com/trkfan/")
page_url_list.append("https://mbasic.facebook.com/Taiwanwashing/")
page_url_list.append("https://mbasic.facebook.com/seller.pcstore/")
page_url_list.append("https://mbasic.facebook.com/taiwanheadbrewers/")
page_url_list.append("https://mbasic.facebook.com/HOBBYEAST/")
page_url_list.append("https://mbasic.facebook.com/WeMoScooter/")
page_url_list.append("https://mbasic.facebook.com/GarminTaiwan/")

text_list = []

for url in page_url_list:
    soup = get_doc(url)
    post_url_list = get_post(soup)
    for i in post_url_list:
        driver.get(str(i))
        time.sleep(3)
        html_doc = driver.page_source
        soup = BeautifulSoup(html_doc,'html.parser')
        text = soup.get_text()
        f.write(i)
        f.write("\n")
        f.write(text[text.find("前往首頁"):text.find("所有人說這專頁讚 · 儲存 · 更多讚傳達心情留言分享")])
        f.write("\n\n")

driver.close()
f.close()