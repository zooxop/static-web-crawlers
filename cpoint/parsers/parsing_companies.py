# 기업 카테고리, 참여기업, 적립 방법
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

participating_companies_url = "https://cpoint.or.kr/netzero/entGuide/nv_entGuideList.do?menuId=9"

html = urlopen(participating_companies_url)
bsObject = bs(html, "html.parser")

# category 리스트 가져오기
def getCategories():
    categories = []

    for category in bsObject.find_all('a', {"class":"cate_btn"}):
        categories.append(category.text.strip())

    return categories

# 참여 기업 리스트 및 tips 가져오기
def getCompanies():
    companies = []

    for button in bsObject.find_all('button', {"class":"companies_btn"}):
        company = []
        company.append(button.find('span', {"class":"companies_title"}).text.strip())
        company.append(button.find('span', {"class":"companies_text"}).text.strip())
        companies.append(company)

    return companies
    