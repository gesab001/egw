import json

fobj = open("gc.json", "r")
jsonobj = json.loads(fobj.read())
fobj.close()
chaptertitles = []
for x in jsonobj["chapters"]:

  chapterTitle = jsonobj["chapters"][x]["chapterTitle"]
  chapterObj = {"chapterN": x, "chapterTitle": chapterTitle}
  chaptertitles.append(chapterObj)

jsonobj["toc"] = chaptertitles

with open("gc2.json", "w") as outfile:
    json.dump(jsonobj, outfile, indent=4)