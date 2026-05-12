import csv
from scrapper import search_incruit, search_saramin

def save_to_csv(jobs):

	with open("downloads.csv", "w", encoding="cp949") as file:
		csv_writer = csv.writer(file)
		csv_writer.writerow(["NO","회사명", "공고명", "지역", "상세보기 페이지"])
		for i, job in enumerate(jobs):
			csv_writer.writerow([i+1, job["company"], job["title"], job["location"], job["link"]])
    