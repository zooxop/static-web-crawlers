# 탄소중립포인트 녹색생활 실천 기업 카테고리 가져오기
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

participating_companies_url = "https://cpoint.or.kr/netzero/entGuide/nv_entGuideList.do?menuId=9"

html = urlopen(participating_companies_url)
bsObject = bs(html, "html.parser")

for link in bsObject.find_all('a', {"class":"cate_btn"}):
    print(link.text.strip())
