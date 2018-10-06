/* basic skeleton for the web_server:
get location and print it to web page*/

const http=require('http');//loads http module
const url =require('url');//loads url module

http.createServer(function(req,res){
  //processing request
  res.writeHead(200, {'Content-Type': 'text/html'});
  var query=url.parse(req.url,true).query;
  var location=query.location;

  //find way to pass location to map api and display
  if(location)
    res.write("The location is "+location);
  else {
    res.write("not found")
  }

  //if map location given, find gps cordinates using  the api

    res.end();
  }).listen(3000);//port to listen
