<!DOCTYPE html>
<html lang="en">
  <head>
  <meta charset="utf-8"> 
   <title>Schema.org Editor</title>
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <meta name="description" content="Schema.org Entity Editor allows for CRUD operations on schema.org entities; serialization operations uses JSON-LD">

   <meta name="author" content="Jeremy Nelson">
   <link href="/assets/css/bootstrap.min.css" rel="stylesheet">
   <link href="/assets/css/bootstrap-responsive.min.css" rel="stylesheet">
   <style>
   body {
        padding-top: 60px; 
   }
   </style>
  </head>
  <body>
  <div class="navbar navbar-fixed-top">
   <div class="navbar-inner">
    <a class="brand" href="/">Schema.org Editor</a>
    <ul class="nav">
     <li class="active"><a href="#">Create</a></li>
     <li><a href="#">Update</a></li>
     <li><a href="#">Remove</a></li>
    </ul>
   </div>
  </div>
  %include
  <script src="/assets/js/jquery.js"></script>
  <script src="/assets/js/bootstrap.min.js"></script>
  <script src="/assets/js/knockout.js"></script> 
  </body>
</html>
