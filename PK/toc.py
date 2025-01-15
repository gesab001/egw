import json

f = open("toc.txt", "r")
strings = f.readlines()

jsondata = {"items": []}
for l in strings:
 itemL = l.split(".......")
 
 titleL = itemL[0].split(".")
 chapterN = titleL[0]
 title = titleL[1].strip()
 pageL = itemL[len(itemL)-1].split(".")
 page = pageL[len(pageL)-1].strip()
 print(chapterN + " " + title + " " + page)
 jsonObj = {"chapterN": chapterN, "title": title, "page": page}
 jsondata["items"].append(jsonObj)

print(jsondata) 
with open("toc.json", "w") as outfile:
  json.dump(jsondata, outfile, indent=4)