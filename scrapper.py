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
		response = requests.get("keyword")
		
		url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchType=search&keydownAccess=&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&searchword={keyword}&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPage={page}&recruitSort=relation&recruitPageCount=40&inner_com_type=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n"






















