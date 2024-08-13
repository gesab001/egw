import json
import os

bookcode = "GC"
chapterT = "Introduction"
chapterN = "Introduction"
startFileNumber = 1
lastFileNumber = 24

files = os.listdir()
jsonfiles = []
jsonfiles.sort()
for f in files:
  if f.startswith("book_GC_id"):
     jsonfiles.append(f)
     
print(len(jsonfiles))
totalfiles = len(jsonfiles)

for x in range(startFileNumber, lastFileNumber+1):
  filename = "book_"+bookcode+"_id_"+str(x)+".json"
  f = open(filename, "r")
  jsonobj = json.loads(f.read())
  f.close()
  #proceed = input("continue?")
  jsonobj["chapter"] = chapterT
  jsonobj["chapterN"] = chapterN     
  print(jsonobj)     
  with open(filename, "w") as outfile:
     json.dump(jsonobj, outfile, indent=4)       
  
  
