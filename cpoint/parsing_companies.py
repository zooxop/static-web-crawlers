# 기업 카테고리, 참여기업, 적립 방법
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

participating_companies_url = "https://cpoint.or.kr/netzero/entGuide/nv_entGuideList.do?menuId=9"

html = urlopen(participating_companies_url)
bsObject = bs(html, "html.parser")

print('카테고리 : ')
for category in bsObject.find_all('a', {"class":"cate_btn"}):
    print(category.text.strip())

print('')

for button in bsObject.find_all('button', {"class":"companies_btn"}):
    title = button.find('span', {"class":"companies_title"}).text.strip()
    tips = button.find('span', {"class":"companies_text"}).text.strip()
    print(title)
    print(tips)
    print('')
    