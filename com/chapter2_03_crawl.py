from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time


baseUrl = "https://www.instagram.com/explore/tags/"
plusUrl = input("검색할 태그를 입력하세요 : ")
url = baseUrl+quote_plus(plusUrl)

rootPath=".."
driver =webdriver.Chrome(
    executable_path="{}/webdriver/chromedriver.exe".format(rootPath)
)
driver.get(url)

time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html)

insta = soup.select(".v1Nh3.kIKUG._bz0w")

print(insta)

driver.close()