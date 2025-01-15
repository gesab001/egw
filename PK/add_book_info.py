import json
import os
import subprocess
import re 


def addBookInfo(bookcode, booktitle, author, date_published, copyright_info):
   #bookcode = "DA"
   #booktitle = "Desire of Ages"
   #author = "Ellen G. White"
   #date_published = "1898"
   #copyright_info = "Public Domain"

   startFileNumber = 1

   files = os.listdir()
   jsonfiles = []
   jsonfiles.sort()   
   for f in files:
     if f.startswith("book_"+bookcode+"_id"):
        jsonfiles.append(f)
 
   print(len(jsonfiles))
   totalfiles = len(jsonfiles)

   for x in range(startFileNumber, totalfiles):
    filename = "book_"+bookcode+"_id_"+str(x)+".json"
    f = open(filename, "r")
    jsonobj = json.loads(f.read())
    f.close()
    page = str(jsonobj["page"])
    word = jsonobj["word"]

    jsonobj["author"] = author
    jsonobj["booktitle"] = booktitle
    jsonobj["date_published"] = date_published
    jsonobj["copyright_info"] = copyright_info
    print(jsonobj)     
    #proceed = input("continue?")
    with open(filename, "w") as outfile:
          json.dump(jsonobj, outfile, indent=4)   