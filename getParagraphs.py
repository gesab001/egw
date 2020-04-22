import sqlite3
import json
import os

json_data = {"AA" :[{"filename": "1.json", "page": "1", "paragraph": "1", "word": "hello"}]}
def getEGWBooks(book):
    filename = book + ".js"
    db = sqlite3.connect('egw_writings_complete.db')
    cursor = db.cursor()
    query = "select BOOKCODE, PAGE, PARAGRAPH, WORD from egw_writings_complete where BOOKCODE='"+ book +"'"
    cursor.execute(query)
    rows = cursor.fetchall()
    count = 1
    json_data = {"paragraphs" : []}
    for row in rows:
        bookCode = row[0]
        page = row[1]
        paragraph = row[2]
        word = '"' + row[3] + '"'
        item = {}
        item["title"] = book
        item["type"] = "book"
        item["filename"] = str(count) + ".json"
        item["bookCode"] = bookCode
        item["page"] = page
        item["paragraph"] = paragraph
        item["word"] = word 
        print(bookCode)
        print(page)
        print(paragraph)
        print(word)
        json_data["paragraphs"].append(item)
        count+=1
    json_data["total"] = count
    data = "export function getbook(){\n var book="+str(json_data)+";\nreturn book;\n}" 
    f = open("jsbooks/"+filename, "w")
    f.write(data)
    f.close()
    db.close()

def getEGWTopics(topic):
    filename = topic + ".js"
    db = sqlite3.connect('egw_writings_complete.db')
    cursor = db.cursor()
    #query = "select BOOKCODE, PAGE, PARAGRAPH, WORD from egw_writings_complete where WORD like '%"+ topic +"%' OR WORD like '%christmas%' OR WORD LIKE '%new year%'"
    query = "select BOOKCODE, PAGE, PARAGRAPH, WORD from egw_writings_complete where WORD like '%"+ topic +"%'"

    cursor.execute(query)
    rows = cursor.fetchall()
    count = 1
    json_data = {"paragraphs" : []}
    for row in rows:
        bookCode = row[0]
        page = row[1]
        paragraph = row[2]
        word = '"' + row[3] + '"'
        item = {}
        item["topic"] = topic
        item["type"] = "topic"
        item["filename"] = str(count) + ".json"
        item["bookCode"] = bookCode
        item["page"] = page
        item["paragraph"] = paragraph
        item["word"] = word 
        print(bookCode)
        print(page)
        print(paragraph)
        print(word)
        json_data[topic].append(item)
        count+=1
    data = "export function get"+topic + "(){\n var book="+str(json_data)+";\nreturn book;\n}" 
    f = open("jsbooks/"+filename, "w")
    f.write(data)
    f.close()
    db.close()


json_file = open("../egw/devotional.json")
json_data = json.load(json_file)

def getEGWBooksFromJson(book):
   filename = book + ".js"
   book_json = json_data[book]
   title = book_json["title"]
   code = book
   total = book_json["totalParagraphs"]
   startingDate = book_json["startingDate"]
   paragraphs = book_json["paragraphs"]
   new_json_data = {"bookcode": code, "title": title, "total": total, "startingDate": startingDate, "paragraphs":paragraphs}
   data = "export function getbook(){\n var book="+str(new_json_data)+";\nreturn book;\n}" 
   f = open("jsbooks/"+filename, "w")
   f.write(data)
   f.close()
   print("finished " + book)
   
def books():
 books = ["AA", "DA", "CG", "CD", "Ed", "1MCP", "2MCP", "PP", "PK", "MH", "GC", "LDE", "CL"]
 for x in books: 
     getEGWBooks(x)


def topics():
  topics = ["politics", "sports"]
#books = ["AA", "DA", "CG", "CD", "Ed", "1MCP", "2MCP", "PP", "PK", "MH", "GC", "LDE", "CL"]
  for x in topics: 
     getEGWTopics(x)

books = ["AA", "DA", "CG", "CD", "Ed", "1MCP", "2MCP", "PP", "PK", "MH", "GC", "LDE", "CL"]
for x in books: 
     getEGWBooksFromJson(x)

