# Create a crawling site

python을 이용하여 매번 검색하기 번거로운 취업사이트의 검색자료를 크롤링하는 사이트를 구현했습니다.

---

### screen

<img src="https://user-images.githubusercontent.com/59306143/102274677-9c378e00-3f67-11eb-9375-69c2a8d11f46.gif" alt="Untitled" width="700" height="500"/>

### explanation

- 매번 찾아보는 잡코리아와 사람인을 로컬로 한번에 찾아보기 위해 만들었습니다.
- 같은 직업을 찾았을 때 같은 작업을 반복하지 않도록 임의로 만든 db에 저장하여 우선적으로 검색하도록 했습니다.
- csv파일로 저장하여 다운로드 할 수 있도록 했습니다.
- 진짜 데이터베이스는 필요없으므로, flask를 이용하여 간단히 구현했습니다.
