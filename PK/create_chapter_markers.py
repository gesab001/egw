import json
import os
import subprocess
import re 

bookcode = input("bookcode: ").upper()
files = os.listdir()
jsonfiles = []
jsonfiles.sort()

chapterT = ""
chapterN = 15
startFileNumber = 1
startPage = 265
newPage = 289
for f in files:
  if f.startswith("book_"+bookcode+"_id"):
     jsonfiles.append(f)
     
print(len(jsonfiles))
totalfiles = len(jsonfiles)
chapter_marks = []
for x in range(1, totalfiles+1):
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
     regexString = "Chap. [0-9]+ [a-zA-Z,\s?'\"-]+[\n!]+" 
     
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
     item = {"chapterT": replacedChapterT, "chapterN": chapterN, "startFileNumber": startFileNumber, "startPage": startPage}
     chapter_marks.append(item)
     #command = "notepad++ " + filename
     #subprocess.call(command, shell=True)
     #proceed = input("continue?")  
     #if proceed=="n":
     #   break

print(chapter_marks)
proceed = input("contineU:?")
chapter_marks_with_newpage = []
def addNewPage(item, item1):     
    newpage = item1["startPage"]
    item["newPage"] = newpage
    return item    
 
for x in range(0, len(chapter_marks)-1):
   item = chapter_marks[x]
   item1 = chapter_marks[x+1]
   newpageItem = addNewPage(item, item1)
   chapter_marks_with_newpage.append(newpageItem)
    

def getLastPage():
   lastFile = totalfiles
   filename = "book_"+bookcode+"_id_"+str(lastFile)+".json"
   print(filename)     
   f  = open(filename, "r")
   jsonobj = json.loads(f.read())
   f.close()
   page = str(jsonobj["page"])
   print(page)
   return page

def editLastChapter():
   lastPage = getLastPage()
   totalChapters = len(chapter_marks)
   lastChapter = chapter_marks[totalChapters-1]
   lastChapter["newPage"] = int(lastPage)+1
   chapter_marks_with_newpage.append(lastChapter)
 
      
     #subprocess.call(command, shell=True)     
"""
     regexString = "\n\s+"+ str(int(page)+1) + "[\n]*" 
     replacedWord = re.sub(regexString, "", word).strip() 

     jsonobj["word"] = replacedWord
     print(jsonobj)
     with open(filename, "w") as outfile:
       json.dump(jsonobj, outfile) 
     subprocess.call(command, shell=True)
     """
     #proceed = input("continue?")
     #if proceed=="n":
     #   break

getLastPage()
editLastChapter()
with open("chapter_marks.json", "w") as outfile:
       json.dump(chapter_marks_with_newpage, outfile) 
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