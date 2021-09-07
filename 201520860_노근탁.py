import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import pyperclip

LOGIN_INFO = {
    'ID' : 'your naver id',
    'PASSWORD' : "your naver password"
}

delay=3

def crawler_with_login(login_url,page_url,filename):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path='./chromedriver',options=chrome_options)
    driver.get(login_url)
    driver.implicitly_wait(delay)
    tag_id = driver.find_element_by_name('id')
    tag_pw = driver.find_element_by_name('pw')
    tag_id.click()
    pyperclip.copy(LOGIN_INFO['ID'])
    tag_id.send_keys(Keys.CONTROL, 'v')
    time.sleep(delay)
    tag_pw.click()
    pyperclip.copy(LOGIN_INFO['PASSWORD']) 
    tag_pw.send_keys(Keys.CONTROL, 'v') 
    time.sleep(delay)
    login_btn = driver.find_element_by_xpath('//*[@id="log.login"]')
    login_btn.click() 
    time.sleep(delay)
    driver.get(page_url)
    driver.implicitly_wait(delay + 10)
    bsObject = BeautifulSoup(driver.page_source, "html.parser")    
    file = open(filename,"w")
    file.write(str(bsObject))
    file.close()
    print(bsObject)
    

def crawler(target_url,filename):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(executable_path='./chromedriver',options=chrome_options)
    driver.get(target_url)
    driver.implicitly_wait(delay)
    bsObject = BeautifulSoup(driver.page_source, "html.parser")    
    file = open(filename,"w")
    file.write(str(bsObject))
    file.close()
    print(bsObject)

def main():
    page = 2
    # target = f"https://book.naver.com/category/index.nhn?cate_code=100&tab=new_book&list_type=list&sort_type=publishday&page={page}"
    comic_target = f"https://comic.naver.com/genre/challenge?&page={page}"
    comic_mypage = "https://comic.naver.com/mypage/favorite"
    nav_login = "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
    comic_filename = f"naver_new_comic_page_{page}.html"
    comic_mypage_filename = f"naver_new_comic_mypage_page_{page}.html"
    crawler(comic_target,comic_filename)
    crawler_with_login(nav_login,comic_mypage,comic_mypage_filename)
    # filename = f"naver_new_book_page_{page}.html"
    # filename_with_login = f"naver_new_book_page_with_login_{page}.html"
    # crawler(target,filename)
    # crawler_with_login(nav_login,target,filename_with_login)


if __name__ == "__main__":
    main()
