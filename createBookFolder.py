import sqlite3
import xml.etree.ElementTree as ET
import time

bookCodes = ["DA", "CD", "CG", "Ed", "1MCP", "2MCP", "PP", "PK", "AA", "MH", "GC", "LDE"]

def addBooks(bookName):

    tree = ET.parse('egw.xml')
    root = tree.getroot()
    book = ET.Element("book", name=bookName)
    root.append(book)
    tree.write('egw.xml')

def addBookChapters(bookNumber, chapterNumber):

    tree = ET.parse('egw.xml')
    root = tree.getroot()
    book = root[bookNumber] #0 is genesis
    chapter = ET.SubElement(book, "chapter", number=chapterNumber)
    root.append(book)
    tree.write('egw.xml')

def addVerses(rows):
    tree = ET.parse('egw.xml')
    root = tree.getroot()
    books = getEGWBooks()
    for bookCode in books:
       bookName = ET.Element("book", code=bookCode)
       pages = getTotalPages(bookCode)
       for page in pages:
           pageNumber = str(page)
           pageElement = ET.SubElement(bookName, "page", number=pageNumber)
           #bookName.append(pageElement)
           paragraphs = getTotalParagraphs(bookCode, pageNumber)
           for paragraph in paragraphs:
              paragraphNumber = str(paragraph[0])
              paragraphElement = ET.SubElement(pageElement, "paragraph", number=paragraphNumber)
              paragraphElement.text = paragraph[1]
              print(paragraph[1])
       root.append(bookName)
    tree.write('egw.xml')

def addVerses2(rows, bookCode):
    tree = ET.parse('test.xml')
    root = tree.getroot()
    for row in rows:
        book = bookCode
        sourceName = str(row[1])
        pageNumber = str(row[2])
        paragraphNumber = str(row[3])
        word = row[4].strip()
        print(book + pageNumber + paragraphNumber + word)
        item = ET.Element("item", code=book, page=pageNumber, paragraph=paragraphNumber, source=sourceName)
        item.text = word
        root.append(item)
    tree.write('test.xml')

def addVerses3(rows, bookCode):
    tree = ET.parse('test.xml')
    root = tree.getroot()
    sourceName = str(rows[0][1])
    bookItem = ET.Element("book", source=sourceName)
    for row in rows:
        book = bookCode
        pageNumber = str(row[2])
        paragraphNumber = str(row[3])
        word = row[4].strip()
        print(book + pageNumber + paragraphNumber + word)
        item = ET.SubElement(bookItem, "item", code=book, page=pageNumber, paragraph=paragraphNumber, source=sourceName)
        item.text = word
    root.append(bookItem)
    tree.write('test.xml')

def getTotalPages(code):
    db = sqlite3.connect('../EGWSqlite/egw_writings_complete.db')
    cursor = db.cursor()
    query = "select distinct PAGE from egw_writings_complete where WORD LIKE '%"+code+"'"
    cursor.execute(query)
    rows = cursor.fetchall()
    books = []
    for row in rows:
        bookCode = row[0]
        books.append(bookCode)
    for book in books:
      print(book)
    return books


def getTotalParagraphs(bookCode, pageNumber):
    db = sqlite3.connect('../EGWSqlite/egw_writings_complete.db')
    cursor = db.cursor()
    query = "select PARAGRAPH, WORD from egw_writings_complete where BOOKCODE='"+bookCode+"'" + "and PAGE='"+pageNumber+"'"
    cursor.execute(query)
    rows = cursor.fetchall()
    books = []
    return rows

def getEGWBooks():
    db = sqlite3.connect('../EGWSqlite/egw_writings_complete.db')
    cursor = db.cursor()
    query = "select distinct BOOKCODE from egw_writings_complete limit 1"
    cursor.execute(query)
    rows = cursor.fetchall()
    books = []
    for row in rows:
        bookCode = row[0]
        books.append(bookCode)
    books.sort()
    for book in books:
      print(book)
    return books

def createBooks():
    #print (tableName)
    db = sqlite3.connect('egw_writings_complete.db')
    for bookCode in bookCodes:
        cursor = db.cursor()
        query = "select ID, BOOKCODE, PAGE, PARAGRAPH, WORD from egw_writings_complete where BOOKCODE='" + bookCode + "'"
        cursor.execute(query)
        rows = cursor.fetchall()
        addVerses3(rows, bookCode)
        db.commit()
    db.close()

def addABook():
    bookCode = "CL"
    db = sqlite3.connect('egw_writings_complete.db')
    cursor = db.cursor()
    query = "select ID, BOOKCODE, PAGE, PARAGRAPH, WORD from egw_writings_complete where BOOKCODE='" + bookCode + "'"
    cursor.execute(query)
    rows = cursor.fetchall()
    addVerses2(rows, bookCode)
    db.commit()
    db.close()

topics = {"BAN": ["birthday", "christmas", "new year", "anniversary"]}
topics["BAN"] = ["birthday", "christmas", "new year", "anniversary"]

def createTopics():
    #print (tableName)
    db = sqlite3.connect('egw_writings_complete.db')
    #topicCode = "BAN"
    #topicCode = "POLITICS"
    topicCode = "SPORTS"
    cursor = db.cursor()
    #query = "select ID, BOOKCODE, PAGE, PARAGRAPH, WORD from egw_writings_complete where WORD LIKE '%birthday%' OR WORD LIKE '%christmas%' OR WORD LIKE '%new year%' OR WORD LIKE '%anniversary%'"
    #query = "select ID, BOOKCODE, PAGE, PARAGRAPH, WORD from egw_writings_complete where WORD LIKE '%politic%'"
    query = "select ID, BOOKCODE, PAGE, PARAGRAPH, WORD from egw_writings_complete where WORD LIKE '%football%' OR WORD LIKE '%chess%' OR WORD LIKE '%game%' OR WORD LIKE '%sport%' OR WORD LIKE '%cricket%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    addVerses2(rows, topicCode)
    db.commit()
    db.close()

#createBooks()
#createTopics()
#addABook()

#getEGWBooks()
def insertBook(book): #shortnames
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    cursor.execute('''INSERT INTO books(shortName) VALUES(?)''', (book,))
    db.commit()
    db.close()

def updateBook(book, id): #abbNames
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    cursor.execute('''UPDATE books SET abbName = ? where bookID = ?''', (book, id))
    db.commit()
    db.close()

def updateBookID(id): #update bookID in kjv table
    print (id, book)
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    cursor.execute(''' update fullNames set bookID = ? where book=?''', (id, book,))
    db.commit()
    db.close()

def updateID(tableName, id):
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    #query = "drop table " + name
    #query = "update kjv set bookID= " + id + " where book like +  
    query = "update table " + tableName + " set id= " + id 
    cursor.execute(query)
    db.commit()
    db.close()
    print (id + " " + name + " added")

#updates bookID of kjv table
def setBookID(lines):
    x = 1
    for line in lines:
       updateBookID(line, x)
       x = x + 1

def createABook(newname, oldname):
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    #query = "drop table " + name
    #query = "update kjv set bookID= " + id + " where book like +  
    query = "create table " + newname + " (id integer primary key autoincrement, bookID int, book text, chapter text, verse text, word text, image text, testament text, shortName text, abbName text)" 
    cursor.execute(query)
    db.commit()
    query2 = "insert into " + newname + " (bookID, book, chapter, verse, word, image, testament, shortName, abbName) select bookID, book, chapter, verse, word, image, testament, shortName, abbName from " + oldname
    cursor.execute(query2)
    db.commit()
    query3 = "drop table " + oldname
    cursor.execute(query3)
    db.commit()
    query4 = "create table " + oldname + " as select * from " + newname
    cursor.execute(query4)
    db.commit()
    query5 = "drop table " + newname
    cursor.execute(query5)
    db.commit()
    db.close()
    
    print (str(id) + " " + oldname + " added")

def updateFullName(bookID, tableName):
    #print (tableName)
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    query = "select count(*) as totalVerses from " + tableName
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        totalVerses = row[0]

        updateTotalVerses(bookID, tableName, totalVerses)
    db.commit()
    db.close()

def getTotalChapters(bookID, tableName):
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    query = "select distinct chapter from " + tableName
    cursor.execute(query)
    rows = cursor.fetchall()
    totalChapters = ""
    for row in rows:
       totalChapters = row[0]
    updateTotalChapters(bookID, totalChapters)
    db.commit()
    db.close()    

def getAbbName():
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    query = "select bookID, abbName from books"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        bookID = row[0]
        abbName = row[1]
        print(str(bookID) + abbName)
        updateAbbName(bookID, abbName)
    db.commit()
    db.close()
    

def updateAbbName(bookID, abbName):
   db = sqlite3.connect('kjvios.db')
   cursor = db.cursor()
   query = "update fullNames2 set abbName ='" + str(abbName) + "' where bookID=" + str(bookID)
   cursor.execute(query)
   db.commit()
   db.close()


def updateTotalChapters(bookID, totalChapters):
   db = sqlite3.connect('kjvios.db')
   cursor = db.cursor()
   query = "update fullNames2 set totalChapters = " + str(totalChapters) + " where bookID=" + str(bookID)
   cursor.execute(query)
   db.commit()
   db.close()

def updateTotalVerses(bookID, tableName, totalVerses):
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    query = "update fullNames2 set totalVerses = " + str(totalVerses) + " where bookID=" + str(bookID)
    cursor.execute(query)
    db.commit()
    db.close()

def getBookNames():
    booklist = []
    db = sqlite3.connect('kjvios.db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM BibleInfo''')
    rows = cursor.fetchall()
    for row in rows:
        #shortName = row[1]
        tableName = row[2]
        tableName_copy = tableName + "_copy" 
        #shortName = shortName.replace(" ", "")
        #shortName = "_" + shortName
        #pair = [bookID, tableName]
        createABook(tableName_copy, tableName)
        #booklist.append(tableName)
    db.commit()
    db.close()
    #for name in booklist:
        #print(name)
        #updateFullName(id, name)
     #   updateFullName(name)

shortNames = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1 Samuel', 
'2 Samuel', '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalms', 'Proverbs', 
'Ecclesiastes', 'Song of Solomon', 'Isaiah', 'Jeremiah', 'Lamentations', 
'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 
'Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts (of the Apostles)', 
'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 
'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 
'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Revelation']

#getBookNames()
#getBookNames()
#getTotalChapters("Book_1")
#setBookID(shortNames)
#print(lines)

#updates abb names to books of the bible
def setAbbNames():
    file = open("abbNames", "r")
    lines = file.readlines()
    x = 1
    for line in lines:
       line = line.split("\t")
       name = (line[1].strip())
       updateBookID(name, x)
       x = x +1
