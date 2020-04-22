<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="./css/bootstrap.min.css">
<!--<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">-->
<script src="./js/jquery.min.js"></script>
<script src="./js/bootstrap.min.js"></script>

    <title>Title</title>
    <script src="egw.js"></script>

    <!--
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
-->
</head>
<body onload="startTime()">

<!-- Navbar --
<div class="w3-top">
    <div class="w3-bar w3-black w3-card">
        <a class="w3-bar-item w3-button w3-padding-large w3-hide-medium w3-hide-large w3-right" href="javascript:void(0)" onclick="myFunction()" title="Toggle Navigation Menu"><i class="fa fa-bars"></i></a>
        <a href="#" class="w3-bar-item w3-button w3-padding-large">HOME</a>
        <a href="https://bible.onecloudapps.net" class="w3-bar-item w3-button w3-padding-large w3-hide-small">Bible</a>
        <a href="https://egw.onecloudapps.net" class="w3-bar-item w3-button w3-padding-large w3-hide-small">EGW</a>
        <a href="https://hymns.onecloudapps.net" class="w3-bar-item w3-button w3-padding-large w3-hide-small">Hymns</a>
        <a href="https://stories.onecloudapps.net" class="w3-bar-item w3-button w3-padding-large w3-hide-small">Stories</a>
        <a href="https://giovanni.saberon.onecloudapps.net" class="w3-bar-item w3-button w3-padding-large w3-hide-small">Videos</a>

        <div class="w3-dropdown-hover w3-hide-small">
            <button class="w3-padding-large w3-button" title="More">MORE <i class="fa fa-caret-down"></i></button>
            <div class="w3-dropdown-content w3-bar-block w3-card-4">
                <a href="#" class="w3-bar-item w3-button">Merchandise</a>
                <a href="#" class="w3-bar-item w3-button">Extras</a>
                <a href="#" class="w3-bar-item w3-button">Media</a>
            </div>
        </div>
        <a href="javascript:void(0)" class="w3-padding-large w3-hover-red w3-hide-small w3-right"><i class="fa fa-search"></i></a>
    </div>
</div>
-->
<!-- Navbar on small screens (remove the onclick attribute if you want the navbar to always show on top of the content when clicking on the links) 
<div id="navDemo" class="w3-bar-block w3-black w3-hide w3-hide-large w3-hide-medium w3-top" style="margin-top:46px">
    <a href="https://bible.onecloudapps.net" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">Bible</a>
    <a href="https://egw.onecloudapps.net" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">EGW</a>
    <a href="https://hymns.onecloudapps.net" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">Hymns</a>
    <a href="https://stories.onecloudapps.net" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">Stories</a>
    <a href="https://giovanni.saberon.onecloudapps.net" class="w3-bar-item w3-button w3-padding-large" onclick="myFunction()">Videos</a>
</div>
-->
<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">Giovanni</a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">Home</a></li>
        <li class="dropdown">
          <a class="dropdown-toggle" data-toggle="dropdown" href="#">Bible<span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="../bible/">Jump Verse</a></li>
            <li><a href="../bible.onecloudapps.net/">Topics</a></li>
            <li><a href="#">Page 1-3</a></li>
          </ul>
        </li>
        <li><a href="../egw.onecloudapps.net">EGW</a></li>
        <li><a href="../hymns.onecloudapps.net">Hymn</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
        <li><a href="#"><span class="glyphicon glyphicon-log-in"></span> Login</a></li>
      </ul>
    </div>
  </div>
</nav>

<br><br><br>

<div id="error"></div>
<div id="currentID"></div>
<div id="timeDisplay"></div>
<div id="dateDisplay"></div>
<div id="paragraphDisplay"></div>
</body>
</html>

