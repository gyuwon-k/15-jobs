import requests
from bs4 import BeautifulSoup

keyword = "파이썬"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&page=1"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
soup.find_all()
#가상환경 : .\venv\Scripts\activate
lis = soup.find_all("li", class_="c_col")
# print(len(lis))
# print(lis)

for li in lis[0:1]:
	# company = li.find("a", class_="cpname")
	# title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text.strip()
	# location = li.find("div", class_="cl_mid").find_all("span")[0].text.strip()
	link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").get("href")
	print(link)
