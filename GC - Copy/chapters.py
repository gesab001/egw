import json
import os

bookcode = "GC"
chapterT = "Luther's Separation From Rome"
chapterN = 7
startFileNumber = 298
startPage = 120
newPage = 145

files = os.listdir()
jsonfiles = []
jsonfiles.sort()
for f in files:
  if f.endswith("json"):
     jsonfiles.append(f)
     
print(len(jsonfiles))
totalfiles = len(jsonfiles)

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
  
  
