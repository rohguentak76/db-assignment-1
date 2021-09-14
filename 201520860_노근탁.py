import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import pyperclip
import json
from collections import OrderedDict

LOGIN_INFO = {
    'ID' : 'mmnani',
    'PASSWORD' : "Mjoh!031223@"
}

delay=3
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path='./chromedriver',options=chrome_options)

def crawler(target_url):
    driver = webdriver.Chrome(executable_path='./chromedriver',options=chrome_options)
    driver.get(target_url)
    bsObject = BeautifulSoup(driver.page_source, "html.parser")    
    webtoonInfoDivs = bsObject.find_all("div",{"class":"challengeInfo"})
    for webtoonInfoDiv in webtoonInfoDivs:
        title = webtoonInfoDiv.find("a").text.strip()
        user = webtoonInfoDiv.find("a",{"class":"user"}).text.strip()
        summary = webtoonInfoDiv.find("div",{"class":"summary"}).text.strip()
        star = float(webtoonInfoDiv.find("strong").text)
        objForJson = OrderedDict()
        objForJson["title"] = title
        objForJson["user"] = user
        objForJson["summary"] = summary
        objForJson["star"] = star
        with open(title + ".json","w",encoding="utf-8") as make_json_file:
            json.dump(objForJson,make_json_file,ensure_ascii=False)

def main():
    start_page = 3
    end_page = 6
    comic_mypage = "https://comic.naver.com/mypage/favorite"
    nav_login = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
    for page in range(start_page,end_page + 1):
        target_url = f"https://comic.naver.com/genre/challenge?&page={page}"
        crawler(target_url)
    

if __name__ == "__main__":
    main()