import requests
from bs4 import BeautifulSoup

LIMIT = 50
search_word_python = "python"
SARAMIN_URL_PY = f"http://www.saramin.co.kr/zf_user/search/recruit?search_area=main&search_done=y&search_optional_item=n&searchType=default_popular&searchword={search_word_python}&recruitPage=1&recruitSort=relation&recruitPageCount={LIMIT}&inner_com_type=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&quick_apply=&except_read="


def extract_saramin_pages():
    result = requests.get(SARAMIN_URL_PY)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "pagination"})
    # 찾은 결과를 pagination 에 넣어줘서 리스트를 만든뒤에 pages 변수에 넣어줌.
    links = pagination.find_all("a")

    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    # links를 가져온다음 빈 array를 만들고, links 안의 link 마다 span을 찾아서 pages 에 넣어줌.
    # pages에 페이지 숫자만 넘겨주기 위해 문자열을 숫자로 바꾸어 삽입.

    max_page = pages[-1]
    # 마지막페이지
    return max_page


def extract_job(html):
    title = html.find("h2", {"class": "job_tit"}).find("a")["title"]
    company = html.find("strong", {"class": "corp_name"}).find("a")["title"]
    location = html.find("div", {"class": "job_condition"}).find("a").string
    job_id = html["value"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"http://www.saramin.co.kr/zf_user/jobs/relay/view?isMypage=no&rec_idx={job_id}&recommend_ids=eJxVkLEVxDAIQ6e5HjAgqDOI99%2FinPglhlL%2BQhaMMB8JTEv%2F4RpFTr0fUpTTZYLGlgRhW9xe6kqHfvKbXm5tPKPK0ENJkIyajbRCOZwKFeYsUa88vQPWvtpy81h5nm2RUPRmKPbIdRKtdkPdS8j7tFnrllwp4jH%2FAX0HU3I%3D&view_type=search&searchword={search_word_python}&searchType=default_popular&gz=1&t_ref_content=generic&t_ref=search&paid_fl=n#seq=0",
    }


def extract_saramin_jobs(last_page):
    jobs = []
    for page in range(last_page):
        # print(f"Scrapping page {page}")
        result = requests.get(f"{SARAMIN_URL_PY}&recruitPageCount={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "item_recruit"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_saramin_page = extract_saramin_pages()
    saramin_jobs = extract_saramin_jobs(last_saramin_page)
    return saramin_jobs