from zlibrary import Zlibrary
z = Zlibrary()
z.login(email="mulanhuayun@163.com", password="7811204630zhym")
res = z.search(message="儒林外史",limit=10)
for book in res['books']:
  print(f'{book["title"]}|{book["extension"]}|{book["language"]}')
