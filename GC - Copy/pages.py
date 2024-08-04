import json
import os
import subprocess
import re 

bookcode = "GC"
files = os.listdir()
jsonfiles = []
jsonfiles.sort()
for f in files:
  if f.endswith("json"):
     jsonfiles.append(f)
     
print(len(jsonfiles))
totalfiles = len(jsonfiles)
for x in range(1351, totalfiles+1):
  filename = "book_"+bookcode+"_id_"+str(x)+".json"
  f = open(filename, "r")
  jsonobj = json.loads(f.read())
  f.close()
  page = str(jsonobj["page"])
  word = jsonobj["word"]
  
  command = "notepad++ " + filename
  #proceed = input("next paragraph?")
  if page in word:
     print(word)
     print("page: " + page)
     print("filename: " + filename)
     print(filename)
     print(command)
     subprocess.call(command, shell=True)     
     regexString = "\n\s+"+ str(int(page)+1) + "[\n]*" 
     replacedWord = re.sub(regexString, "", word).strip() 
     #print(replacedWord)

     jsonobj["word"] = replacedWord
     print(jsonobj)
     with open(filename, "w") as outfile:
       json.dump(jsonobj, outfile) 
     subprocess.call(command, shell=True)

     proceed = input("continue?")
     if proceed=="n":
        break
  try:
   if str(int(page)+1) in word:
     print(word)
     print("page: " + page)
     print("filename: " + filename)
     print(filename)
     print(command) 
     subprocess.call(command, shell=True)
     regexString = "\n\s+"+ str(int(page)+1) + "[\n]*" 
     replacedWord = re.sub(regexString, "", word).strip() 
     replacedWord.strip()
     #print(replacedWord)
     jsonobj["word"] = replacedWord
     print(jsonobj)     
     with open(filename, "w") as outfile:
       json.dump(jsonobj, outfile)
     subprocess.call(command, shell=True)
     proceed = input("continue?")  
     if proceed=="n":
        break
  except:
     print("not a number")  