import json
import os
import subprocess
import re 

bookcode = "GC"
files = os.listdir()
jsonfiles = []
jsonfiles.sort()
for f in files:
  if f.startswith("book_GC_id"):
     jsonfiles.append(f)
     
print(len(jsonfiles))
totalfiles = len(jsonfiles)
book_data = {"chapters": {}, "book_info": {}}
for x in range(1, totalfiles+1):
  filename = "book_"+bookcode+"_id_"+str(x)+".json"
  f = open(filename, "r")
  jsonobj = json.loads(f.read())
  f.close()
  page = str(jsonobj["page"])
  paragraph = str(jsonobj["paragraph"])
  word = jsonobj["word"]
  chapterTitle = jsonobj["chapter"]
  chapter = jsonobj["chapter"]
  bookcode = jsonobj["bookcode"]
  author = jsonobj["author"]
  booktitle = jsonobj["booktitle"]
  date_published = jsonobj["date_published"]
  copyright_info = jsonobj["copyright_info"]
  book_data["book_info"]["author"] = author
  book_data["book_info"]["booktitle"] = booktitle
  book_data["book_info"]["date_published"]  = date_published
  book_data["book_info"]["copyright_info"] = copyright_info
  book_data["book_info"]["bookcode"] = bookcode
  paragraph_item = {"word": word, "page": page, "paragraph": paragraph, "file_number": x, "file_name": filename}
  
  try:
   chapterN = jsonobj["chapterN"]
   #print((str(x)) +". " + chapter)
   if chapterN not in book_data["chapters"]:
       book_data["chapters"][chapterN] = {"chapterTitle": "", "paragraphs": []}
       book_data["chapters"][chapterN]["chapterTitle"] = chapterTitle
       book_data["chapters"][chapterN]["paragraphs"].append(paragraph_item)
       
       
   else:
       book_data["chapters"][chapterN]["paragraphs"].append(paragraph_item)
   
  except KeyError:
    print(chapter + " has no chapter number")
    print(filename)

print(book_data)  
with open("complete_book.json", "w") as outfile:
   json.dump(book_data, outfile, indent=4)
