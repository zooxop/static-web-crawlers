# <title> 태그 값만 출력.
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen("http://www.naver.com")
bsObject = bs(html, "html.parser")

print(bsObject.head.title)