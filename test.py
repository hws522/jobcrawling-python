import requests
from bs4 import BeautifulSoup

saramin_result = requests.get("http://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=default_popular&searchword=python&recruitPage=1&recruitSort=relation&recruitPageCount=50&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&quick_apply=&except_read=")

saramin_soup = BeautifulSoup(saramin_result.text, "html.parser")

pagination = saramin_soup.find("div", {"class":"pagination"})
# 찾은 결과를 pagination 에 넣어줘서 리스트를 만든뒤에 pages 변수에 넣어줌.
links = pagination.find_all('a')

pages = []

for link in links[:-1]:
    pages.append(int(link.string))

#links를 가져온다음 빈 array를 만들고, links 안의 link 마다 span을 찾아서 pages 에 넣어줌.
#pages에 페이지 숫자만 넘겨주기 위해 문자열을 숫자로 바꾸어 삽입.

max_page = pages[-1]
# 마지막페이지 

