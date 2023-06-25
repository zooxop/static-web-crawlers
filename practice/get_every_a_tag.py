# 모든 링크의 텍스트와 주소 가져오기
# <a> 태그로 둘러싸인 텍스트와 <a> 태그의 href 속성을 출력.

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

html = urlopen("https://www.naver.com")
bsObject = bs(html, "html.parser")

for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))