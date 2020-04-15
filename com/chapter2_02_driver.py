from selenium import webdriver

rootPath=".."
driver=webdriver.Chrome(
    executable_path="{}/webdriver/chromedriver.exe".format(rootPath)
)

url="https://www.instagram.com/explore/tags/%EC%84%9C%EC%9A%B8%EB%A7%9B%EC%A7%91/"
driver.get(url) #enter치는 것
#driver.close()