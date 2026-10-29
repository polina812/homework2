catalog = [
{"title": "Мастер и Маргарита", "author": "Булгаков",
"year": 1967, "genre": "роман", "on_loan": True},
{"title": "Евгений Онегин", "author": "Пушкин",
"year": 1833, "genre": "роман", "on_loan": False},
{"title": "Стихотворения", "author": "Есенин",
"year": 1926, "genre": "поэзия", "on_loan": False},
{"title": "Вишнёвый сад", "author": "Чехов",
"year": 1904, "genre": "пьеса", "on_loan": True},
{"title": "Руслан и Людмила", "author": "Пушкин",
"year": 1820, "genre": "поэма", "on_loan": False},
{"title": "Три сестры", "author": "Чехов",
"year": 1901, "genre": "пьеса", "on_loan": False},
]

def find_by_author(catalog, author):
	book = []
	for d in catalog:
		if d["author"] == author: book.append(d["title"])
	return book

print(find_by_author(catalog, "Пушкин"))


def available_titles(catalog):
	book = []
	for d in catalog:
		if d["on_loan"] == False: book.append(d["title"])
	return book
print(available_titles(catalog))


def books_grouped_by_genre(catalog):
	return_d = {}
	for d in catalog:
		key = d["genre"]
		if d["on_loan"] == False: 
			if key not in return_d: return_d[key] = [d["title"]]
			else: return_d[key].append(d["title"])

		# в другом варианте порядок будет как при первом вхождении,но будут
		# создаваться ключи с пустыми значениями, если будет иные входные данные		
		# if key not in return_d: return_d[key] = []
		# if d["on_loan"] == False: return_d[key].append(d["title"])
		
	return return_d
print(books_grouped_by_genre(catalog))