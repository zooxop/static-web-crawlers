# 웹페이지 전체 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen("http://www.naver.com")
bsObject = bs(html, "html.parser")

print(bsObject)
