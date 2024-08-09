import json
import os
import subprocess
import re 

bookcode = "GC"
files = os.listdir()
jsonfiles = []
jsonfiles.sort()

chapterT = "The Bible and the French Revolution"
chapterN = 15
startFileNumber = 720
startPage = 265
newPage = 289
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
  if "Chap." in word:
     print(word)
     print("page: " + page)
     print("filename: " + filename)
     print(filename)
     print(command)
     regexString = "Chap. [0-9]+ - [a-zA-Z\s?']+[\n]+" 
     
     chapterT = re.search(regexString, word).group()     
     regexString = "Chap. [0-9]+ - "
     replacedChapterT = re.sub(regexString, "", chapterT).strip() 
     
     print("chapterT = " + '"' + replacedChapterT + '"')
     regexString = "Chap. [0-9]+"
     chapterN = re.search(regexString, chapterT).group()    
     chapterN = chapterN.replace("Chap. ", "")
     print("chapterN = " + chapterN )
     startFileNumber = x
     print("startFileNumber = " + str(startFileNumber))
     startPage = page
     print("startPage = " + startPage)
     
     """     
     subprocess.call(command, shell=True)     
     regexString = "\n\s+"+ str(int(page)+1) + "[\n]*" 
     replacedWord = re.sub(regexString, "", word).strip() 

     jsonobj["word"] = replacedWord
     print(jsonobj)
     with open(filename, "w") as outfile:
       json.dump(jsonobj, outfile) 
     subprocess.call(command, shell=True)
     """
     proceed = input("continue?")
     if proceed=="n":
        break
  """
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
  """   