# 웹문서에서 메타 태그를 찾아서 content 속성값을 가져옵니다.

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen("https://www.python.org/about")
bsObject = bs(html, "html.parser")

for meta in bsObject.find_all('meta'):
    print(meta.get('content'))