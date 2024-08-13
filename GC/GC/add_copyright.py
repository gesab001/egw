import json
import os

bookcode = "GC"
copyright_info = "Public Domain"
startFileNumber = 1

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

  jsonobj["copyright_info"] = copyright_info
  print(jsonobj)     
  #proceed = input("continue?")
  with open(filename, "w") as outfile:
          json.dump(jsonobj, outfile, indent=4)       
  
  
