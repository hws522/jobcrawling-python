import requests
from bs4 import BeautifulSoup

search_word_python = "python"
JOBKOREA_URL_PY = (
    f"http://www.jobkorea.co.kr/Search/?stext={search_word_python}&tabType=recruit"
)


def get_last_page():
    result = requests.get(JOBKOREA_URL_PY)

    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.find("div", {"class": "tplPagination"}).find_all("li")
    # 찾은 결과를 pagination 에 넣어줘서 리스트를 만든뒤에 pages 변수에 넣어줌.
    last_page = pagination[-1].text
    return int(last_page)


def extract_job(html):
    title = html.find("div", {"class": "post-list-info"}).find("a")["title"]
    company = html.find("div", {"class": "post-list-corp"}).find("a")["title"]
    location = (
        html.find("div", {"class": "post-list-info"})
        .find("p", {"class": "option"})
        .find("span", {"class": "long"})
        .string
    )
    job_id = html["data-gno"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"http://www.jobkorea.co.kr/Recruit/GI_Read/{job_id}?Oem_Code=C1&logpath=1",
    }


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        result = requests.get(f"{JOBKOREA_URL_PY}&Page_No={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        soup = soup.find("div", {"class": "recruit-info"})
        results = soup.find_all("li", {"class": "list-post"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs
