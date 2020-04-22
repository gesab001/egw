// Used to toggle the menu on small screens when clicking on the menu button
function myFunction() {
    var x = document.getElementById("navDemo");
    if (x.className.indexOf("w3-show") == -1) {
        x.className += " w3-show";
    } else {
        x.className = x.className.replace(" w3-show", "");
    }
}

function startTime() {

    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('timeDisplay').innerHTML =
        h + ":" + m + ":" + s;
    var timers = document.getElementsByClassName('timer');
    for (var x=0; x<timers.length; x++){
        timers[x].innerHTML = 24-h + " hours and " + (60-m) + " minutes and " + (60-s) + " seconds left" ;
    }
    var t = setTimeout(startTime, 500);
    if (h=="00" && m=="00"){
        loopNodesList();
    }

}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

var xhttp = new XMLHttpRequest();
var xmlDoc;
var nodesLengthList = [];

var books = ["BAN", "DA", "CG", "CD", "Ed", "1MCP", "2MCP", "PP", "PK", "AA", "MH", "GC", "LDE", "POLITICS", "SPORTS", "CL"];
var bookTitles = [];
bookTitles.push("Birthdays, Anniversaries, New Year");
bookTitles.push("Desire of Ages");
bookTitles.push("Child Guidance");
bookTitles.push("Counsels on Diets and Foods");
bookTitles.push("Education");
bookTitles.push("Mind, Character and Personality Volume 1");
bookTitles.push("Mind, Character and Personality Volume 2");
bookTitles.push("Patriarchs and Prophets");
bookTitles.push("Prophets and Kings");
bookTitles.push("Acts of the Apostles");
bookTitles.push("Ministry of Healing");
bookTitles.push("Great Controversy");
bookTitles.push("Last Day Events");
bookTitles.push("Politics");
bookTitles.push("Sports");
bookTitles.push("Country Living");

var startingDates = [];
var daDate = new Date(2016, 11, 30, 14, 45, 0, 0);
var otherDates = new Date(2018, 5, 22, 14, 45, 0, 0);
startingDates.push(otherDates); //BAN
startingDates.push(daDate); //DA
startingDates.push(otherDates); //CD
startingDates.push(otherDates); //CG
startingDates.push(otherDates); //Ed
startingDates.push(otherDates); //1MCP
startingDates.push(otherDates); //2MCP
startingDates.push(otherDates); //PP
startingDates.push(otherDates); //PK
startingDates.push(otherDates); //AA
startingDates.push(otherDates); //MH
startingDates.push(otherDates); //GC
startingDates.push(otherDates); //LDE
startingDates.push(otherDates); //Politics
startingDates.push(otherDates); //Sports
startingDates.push(otherDates); //Country Living

var nodesList = [];
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        //        // Typical action to be performed when the document is ready:
        xmlDoc = xhttp.responseXML;
        loadNodesList();
        loopNodesList();
    }
    document.getElementById("error").innerHTML = this.status.toString();

};
xhttp.open("GET", "test.xml", true);
xhttp.send();


function loadNodesList() {
    try{
        for (var i=0; i<books.length; i++){
            getBook(i);
        }

    }  catch(err) {
        document.getElementById("error").innerHTML = err.message;
    }

}
function getBook(bookIndex){
    try{
        var book = books[bookIndex];
        var path = "//egw//item[@code='"+book+"']";
        var nodes = xmlDoc.evaluate(path, xmlDoc, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
        var length = nodes.snapshotLength;
        var paragraphs = [];
        for (var i=0; i<nodes.snapshotLength; i++){
            var bookSource = nodes.snapshotItem(i).childNodes[0].parentElement.getAttribute("source");
            var pageNumber = nodes.snapshotItem(i).childNodes[0].parentElement.getAttribute("page");
            var paragraphNumber = nodes.snapshotItem(i).childNodes[0].parentElement.getAttribute("paragraph");
            var word =  nodes.snapshotItem(i).childNodes[0].nodeValue;
            var full = word + " (" + bookSource + ", page " + pageNumber + ", paragraph " + paragraphNumber + ")";
            paragraphs.push(full);

        }
        nodesLengthList.push(length);
        nodesList.push(paragraphs);

    }
    catch(err) {
        document.getElementById("error").innerHTML = err.message;
    }
}

function loopNodesList(){
    var txt ="";
    txt += "<hr>";
    try{
        for (var i=0;i<nodesList.length; i++){
            var paragraph = displayMinuteParagraph(i);
            txt+= paragraph;

        }
        document.getElementById("paragraphDisplay").innerHTML = txt;
    }    catch(err) {
        document.getElementById("error").innerHTML = err.message;
    }

}
function displayMinuteParagraph(nodesIndex){
    try{
        var txt = "";
        var total = nodesLengthList[nodesIndex];
        var currentID = getCurrentID(total, nodesIndex);
        // document.getElementById("currentID").innerHTML = currentID;
        var heading = bookTitles[nodesIndex];
        var word = nodesList[nodesIndex][currentID];
        var title = "<h1>" + heading + "</h1><p class='timer'></p>";
        var counter = "<p>" + currentID + " of " +  total + " paragraphs </p>";
        txt += title + "<div id='"+nodesIndex +"'>" + counter + word  + "<br><br>";
        var previousParagraph = "previousParagraph(";
        previousParagraph += nodesIndex + "," + currentID;
        previousParagraph += ")";
        var nextParagraph = "nextParagraph(";
        nextParagraph += nodesIndex + "," + currentID;
        nextParagraph += ")";
        txt += "<button onclick='"+previousParagraph+"'>previous</button>";
        txt += "<button onclick='"+nextParagraph+"'>next</button>";
        txt += "<hr></div>";
        return txt;

    }
    catch(err) {
        document.getElementById("error").innerHTML = err.message;
    }

}

function previousParagraph(nodesIndex, currentID){
    try{
        var txt = "";
        var total = nodesLengthList[nodesIndex];
        var currentID = currentID - 1;
        // document.getElementById("currentID").innerHTML = currentID;
        var heading = bookTitles[nodesIndex];
        var word = nodesList[nodesIndex][currentID];
        // var title = "<h1>" + heading + "</h1><p class='timer'></p>";
        var counter = "<p>" + currentID + " of " +  total + " paragraphs </p>";
        txt += "<div id='"+nodesIndex +"'>" + counter + word  + "<br><br>";
        var previousParagraph = "previousParagraph(";
        previousParagraph += nodesIndex + "," + currentID;
        previousParagraph += ")";
        var nextParagraph = "nextParagraph(";
        nextParagraph += nodesIndex + "," + currentID;
        nextParagraph += ")";
        txt += "<button onclick='"+previousParagraph+"'>previous</button>";
        txt += "<button onclick='"+nextParagraph+"'>next</button>";
        txt += "<hr></div>";
        document.getElementById(nodesIndex).innerHTML = txt;

    }
    catch(err) {
        document.getElementById("error").innerHTML = err.message;
    }
}

function nextParagraph(nodesIndex, currentID){
    try{
        var txt = "";
        var total = nodesLengthList[nodesIndex];
        var currentID = currentID + 1;
        // document.getElementById("currentID").innerHTML = currentID;
        var heading = bookTitles[nodesIndex];
        var word = nodesList[nodesIndex][currentID];
        // var title = "<h1>" + heading + "</h1><p class='timer'></p>";
        var counter = "<p>" + currentID + " of " +  total + " paragraphs </p>";
        txt += "<div id='"+nodesIndex +"'>" + counter + word  + "<br><br>";
        var previousParagraph = "previousParagraph(";
        previousParagraph += nodesIndex + "," + currentID;
        previousParagraph += ")";
        var nextParagraph = "nextParagraph(";
        nextParagraph += nodesIndex + "," + currentID;
        nextParagraph += ")";
        txt += "<button onclick='"+previousParagraph+"'>previous</button>";
        txt += "<button onclick='"+nextParagraph+"'>next</button>";
        txt += "<hr></div>";
        document.getElementById(nodesIndex).innerHTML = txt;

    }
    catch(err) {
        document.getElementById("error").innerHTML = err.message;
    }
}

function getCurrentID(totalVerses, dateIndex){

    const monthNames = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    var date1 = new Date();
    var year = date1.getFullYear();
    var month = date1.getMonth();
    var day = date1.getDate();
    document.getElementById("dateDisplay").innerHTML = monthNames[month] + " " + day + ", " + year;
    var date2 = startingDates[dateIndex];
    var difference = date1.getTime() - date2.getTime();
    var minutesDifference = Math.floor(difference/1000/60/60/24);
    var currentID=minutesDifference;
    // difference -= minutesDifference*1000*60;
    while (currentID > totalVerses){
        currentID = currentID - totalVerses;
    }
    //     document.getElementById("demo").innerHTML = "hello";
    // }
    // catch (e) {
    //     document.getElementById("demo").innerHTML = "hello1";
    //
    //

    return currentID;
}

