from libs.crawler import crawl

url="https://www.instagram.com/explore/tags/%EC%84%9C%EC%9A%B8%EB%A7%9B%EC%A7%91/"

pageString= crawl(url)
print(pageString)