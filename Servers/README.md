#Server
The servers written here are the very basic sketch on how you can use NodeJs with your IOT application.
Before we start:
![alt tag]()

##Code Flow
#### Importing Modules
Typical server code starts with declaration of various modules. This line of code is going to import a module called expres and save it in the variable called express.

```
var express = require('express')
```
#### Creating a condition for POST requests to the server
When you have a post a value to a link , a post request has to be made. This is how to tell your server what to do on a post request

```
var cV = 0;
var app = express()
app.post('/postLink',function(req,res){
	console.log(req.body.value); //This will give you the value in the body
	cV = req.body.value; // Here is where you save the value
	res.json("Got Request") // sends back to the origin of POST request 
})
``` 
#### Creating a condition for GET requests to the server
When you have to retrieve a value from a link , a get request had to be made. This is how you tell your server what to do on a GET request.

```
app.get('/getLink',function(req,res){
	if (cv!=0){
		res.send(cV);
		//To make sure same value is not being sent reset cV
		cV ="none"
		}
})
```
#### Ask the server to start listening
```
var server = app.listen(process.env.PORT || 3000, function () { //Run the server

  var host = server.address().address
  var port = server.address().port

  console.log('Example app listening at http://%s:%s', host, port)

})

```

## Usage
The codes I will be writing here are written in NodeJs,like I mentioned earlier, with express .
####Install NodeJs on your system
Follow this [link](https://nodejs.org/) to get started with NodeJs on your system.
It is relatively easy to install on a Mac and a Linux system :)

####Install NodeJs on Heroku
Follow this [link] (https://devcenter.heroku.com/articles/getting-started-with-nodejs) .
I use Heroku to test all my applications. If you have installed NodeJs on your system, it won't be hard for you to install it on Heroku at all!  It is easy to use and has good support. You could use another service of your choice for testing stuff.
#### Run and Test the server
``` javascript
$node app.js
```
####Various examples that I have put up
1. Send Basic Text to a Server.

2. Send Images to a server(coming soon).

3. Socket IO Integration for your server(coming soon).

4. Writing an MQTT server for your application(coming soon).

### Questions?
But why write your own server when ThingSpeak and a bunch of really good services are already available?
>In your own product, you need control on everything that you will be working on.
>The servers can be tweeked to work whichever way you want.
>With a little bit experience you can scale it up
>It is always a better option to secure your data.
