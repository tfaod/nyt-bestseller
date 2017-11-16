import json, requests
from datetime import timedelta, date
from sets import Set
from time import sleep

text_file = open("book-corpus1.txt", "w")

url = 'https://api.nytimes.com/svc/books/v3/lists.json'

isbns = set()

def daterange(start_date, end_date):
	for n in range(int ((start_date - end_date).days)):
		yield start_date - timedelta(n)
booktypes = ["combined-print-and-e-book-fiction", "advice-how-to-and-miscellaneous", "childrens-middle-grade-e-book", "childrens-middle-grade-hardcover", "childrens-middle-grade-paperback","picture-books","series-books","young-adult-e-book","young-adult-hardcover","young-adult-paperback" ]
start_date = date(2017, 11, 15)
#end_date = date(2017, 11, 12)
end_date = date(2008, 1, 1)
#end_date = date(2016, 11, 15)
for single_date in daterange(start_date, end_date):
	dateParam = single_date.strftime("%Y-%m-%d")
	for i in range(len(booktypes)):
		booktype = booktypes[i]
		params = {
			"api_key" : '0567a6ed99cf46ed8b113b0553378413',
			"date" : dateParam,
			"list" : bookType
		}

		try:
			resp = requests.get(url=url, params=params)
			data = json.loads(resp.text)
            sleep(.2)
		except ValueError:
			print("oh no, value error!")
			continue

		if "results" in data:
			for item in data["results"]: 
				if item["isbns"][0]["isbn10"] not in isbns:
					text_file.write(str(item))
					isbns.add(item["isbns"][0]["isbn10"])
				else:
					continue

text_file.close()
