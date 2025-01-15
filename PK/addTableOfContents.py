import json


def addTOC():
   filename = "complete_book.json"
   fobj = open(filename, "r")
   jsonobj = json.loads(fobj.read())
   fobj.close()
   chaptertitles = []
   for x in jsonobj["chapters"]:
     chapterTitle = jsonobj["chapters"][x]["chapterTitle"]
     chapterObj = {"chapterN": x, "chapterTitle": chapterTitle}
     chaptertitles.append(chapterObj)
     jsonobj["toc"] = chaptertitles
   with open(filename, "w") as outfile:
    json.dump(jsonobj, outfile, indent=4)
    
    