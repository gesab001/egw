import json
import os

bookcode = input("bookcode: " ) 
bookcode = bookcode.upper() #"DA"


files = os.listdir()
jsonfiles = []
jsonfiles.sort()
for f in files:
  if f.startswith("book_"+bookcode+"_id"):
     jsonfiles.append(f)
     
print(len(jsonfiles))
totalfiles = len(jsonfiles)
filenamecount = 31
startfilenumber = 1
for x in range(startfilenumber, totalfiles+1):
  old_filename = "book_"+bookcode+"_id_"+str(x)+".json"
  new_filename = "renamed_files/"+ "book_"+bookcode+"_id_"+str(filenamecount)+".json"
  filenamecount = filenamecount + 1
  print(old_filename)
  print(new_filename)
  os.rename(old_filename, new_filename)
  #proceed = input("continue? ")
  #if proceed=="y":
  #  continue
  #else: 
  #  break
