import json
import os

bookcode = input("bookcode: " ) #"DA"
bookcode = bookcode.upper()


files = os.listdir()
jsonfiles = []
jsonfiles.sort()
for f in files:
  if f.startswith("book_"+bookcode+"_id"):
     jsonfiles.append(f)
     
print(len(jsonfiles))
totalfiles = len(jsonfiles)

def addChapters(totalfiles, chapterT, chapterN, startFileNumber, startPage, newPage):
 for x in range(startFileNumber, totalfiles+1):
  filename = "book_"+bookcode+"_id_"+str(x)+".json"
  f = open(filename, "r")
  jsonobj = json.loads(f.read())
  f.close()
  page = str(jsonobj["page"])
  word = jsonobj["word"]
  #proceed = input("continue?")
  
  if int(page)>=startPage: 
      if page==str(newPage):
       break
      else:
       #print(word)
       print(page)
       print(filename)
       jsonobj["chapter"] = chapterT
       jsonobj["chapterN"] = chapterN     
       print(jsonobj)     
       with open(filename, "w") as outfile:
          json.dump(jsonobj, outfile, indent=4)       
  
fopen = open("chapter_marks.json", "r")
chapter_marks_json = json.loads(fopen.read())

for item in chapter_marks_json:
 print(item)
 chapterT = item["chapterT"]
 chapterN = item["chapterN"]
 startFileNumber = item["startFileNumber"]
 startPage = int(item["startPage"])
 newPage = int(item["newPage"])
 addChapters(totalfiles, chapterT, chapterN, startFileNumber, startPage, newPage)