import requests
from bs4 import BeautifulSoup

def search_incruit(keyword, page):


	for i in range(page+1):
		page = i * 30
		url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno=0&page={page}"
		# print(f"--- 현재 크롤링 중인 URL: {url} ---")

		# print("-" * 50)
		response = requests.get(url)
		soup = BeautifulSoup(response.text, "html.parser")
		# print(soup)
		# response = requests.get(url)
		# soup = BeautifulSoup(response.text, "html.parser")
		# 공고 리스트 추출
		lis = soup.find_all("li", class_="c_col")

		jobs = []
		for li in lis:
			# 각 요소 추출
			company_tag = li.find("a", class_="cpname")
			company = company_tag.text.strip() if company_tag else "회사명 없음"
			
			cell_mid = li.find("div", class_="cell_mid")
			title_tag = cell_mid.find("div", class_="cl_top").find("a")
			title = title_tag.text.strip()
			link = title_tag.get("href")
			
			# 지난번에 확인한 cl_md로 수정 반영
			cl_md = li.find("div", class_="cl_md")
			location = cl_md.find_all("span")[0].text.strip() if cl_md else "지역 정보 없음"

			job_data = {
				"company": company,
				"title": title,
				"location": location,
				"link": link
			}
			jobs.append(job_data)
			# print(f"수집 완료: {title}")

		# print(f"\n[페이지 {i+1} 결과 요약]")
		# print(jobs)
		# print("-" * 50)

	return jobs

def search_saramin(keyword, page):
	
	for i in range(page+1):
		page = i
		url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&keydownAccess=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&searchword={keyword}&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPage={page}&recruitSort=relation&recruitPageCount=40&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n"
		headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
					}
		response = requests.get(url, headers=headers)
		soup = BeautifulSoup(response.text, "html.parser") #response에 저장된 url 정보중 페이지소스보기 정보를 text메써드로 가져옴. bs4기능으로 html->python 객체로 변환(매써드사용을 위함)
		lis = soup.find_all("div", class_="item_recruit")

		jobs = []
		for li in lis:
			company_tag = li.find("strong", class_="corp_name")
			company = company_tag.text.strip() if company_tag else "회사명 없음"

			title_tag = li.find("h2", class_="job_tit")
			a_tag = title_tag.find("a")
			title = a_tag.text.strip() if title_tag else "공고명 없음"
			link = "https://www.saramin.co.kr" + a_tag.get("href") if title_tag else "상세보기 페이지 없음"


			location_tag = li.find("div", class_="job_condition")
			location = location_tag.find_all("span")[0].text.strip() if location_tag else "위치정보 없음"

			job_data = {
				"company" : company,
				"title" : title,
				"location": location,
				"link" : link
			}
			jobs.append(job_data)
	return jobs


