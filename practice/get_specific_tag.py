# 원하는 태그의 내용 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen("https://www.python.org/about")
bsObject = bs(html, "html.parser")

# <meta> 태그 중, "name" 속성갑싱 "description"인 태그의 "content" 속성 값을 가져온다.
print(bsObject.head.find("meta", {"name":"description"}).get('content'))