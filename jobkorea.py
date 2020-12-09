import requests
from bs4 import BeautifulSoup

search_word_python = "python"
JOBKOREA_URL_PY = f"http://www.jobkorea.co.kr/Search/?stext={search_word_python}&tabType=recruit"

def extract_jobkorea_pages():
    result = requests.get(JOBKOREA_URL_PY)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class":"tplPagination"})
# 찾은 결과를 pagination 에 넣어줘서 리스트를 만든뒤에 pages 변수에 넣어줌.
    links = pagination.find_all("li")

    pages = []

    for link in links:
        pages.append(int(link.text))

    
#links를 가져온다음 빈 array를 만들고, links 안의 link 마다 span을 찾아서 pages 에 넣어줌.
#pages에 페이지 숫자만 넘겨주기 위해 문자열을 숫자로 바꾸어 삽입.

    max_page = pages[-1]
# 마지막페이지 
    return max_page

