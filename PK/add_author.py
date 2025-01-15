import json
import os


def addAuthor(bookcode, author):
   #bookcode = "DA"
   #author = "Ellen G. White"
   startFileNumber = 1

   files = os.listdir()
   jsonfiles = []
   jsonfiles.sort()   
   for f in files:
     if f.startswith("book_"+bookcode+"_id"):
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
     jsonobj["author"] = author
     print(jsonobj)     
     #proceed = input("continue?")
     with open(filename, "w") as outfile:
          json.dump(jsonobj, outfile, indent=4)       
  
  
