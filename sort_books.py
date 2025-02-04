import json


file = open("booklist.json", "r")
json_obj = json.loads(file.read())["items"]
print(json_obj)
books_dic = {}
books_list = []
for x in range(0, len(json_obj)):
   item = json_obj[x]
   print(item)
   bookcode = item["bookcode"]
   title = item["title"]
   books_dic[bookcode] = title
   books_list.append(bookcode.lower())
print(books_dic)
books_list.sort()
print(books_list)   