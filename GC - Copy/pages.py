import json
import os

bookcode = "GC"
files = os.listdir()
jsonfiles = []
jsonfiles.sort()
for f in files:
  if f.endswith("json"):
     jsonfiles.append(f)
     
print(len(jsonfiles))
totalfiles = len(jsonfiles)
for x in range(179, totalfiles+1):
  filename = "book_"+bookcode+"_id_"+str(x)+".json"
  f = open(filename, "r")
  jsonobj = json.loads(f.read())
  f.close()
  page = str(jsonobj["page"])
  word = jsonobj["word"]

  #proceed = input("next paragraph?")
  if page in word:
     print(word)
     print("page: " + page)
     print("filename: " + filename)
     print(filename)
     proceed = input("continue?")
     if proceed=="n":
        break
  try:
   if str(int(page)+1) in word:
     print(word)
     print("page: " + page)
     print("filename: " + filename)
     print(filename)
     proceed = input("continue?")  
     if proceed=="n":
        break
  except:
     print("not a number")  