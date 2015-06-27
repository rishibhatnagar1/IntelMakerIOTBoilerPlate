#Core Files written in Python
This section will have all the pseudo codes you would need to work on your next IOT project. This is all written in Python.

>All the codes above have been written in Python 2.7 and should work fine with most of your systems, Intel Edison /Galileo . These can also work on other boards like BBB or RaPi etc with a change in the GPIO libraries.

##Usage

####Mraa 
It is a low level library for Intel Edison and Galileo, this essentially helps you define GPIOs etc. 

Module `import mraa`

Declaration for Analog pins `x = mraa.Aio(0) #Analog Reading`

Declaration for Digital Pins 
```
x = mraa.Gpio(8)
x.dir(mraa.DIR_OUT)#Output
y = mraa.Gpio(7)
y.dir(mraa.DIR_INP) #Input
```

##Connecting Edison with the server
Before we connect the Edison with any kind of a server, it first needs to be communicating and connected with the Internet.
For connecting Edison with the Internet, search for a wifi 

`$ configure_edison --wifi`

To check if all is working fine, do a `$ ping google.com` 

>The server once running will be running at a link. It could look like 
`localhost:3000/` or 'blah.herokuapp.com/' or a custom link that you could have generated while using any other online services. 

To put it in simple terms, a server will <b>serve</b> the data. Edison is going to either <b>GET</b> data or <b>POST</b> data to the server.
When I say server next time read <b>link</b> .

###How linking edison and server works 
We use a library called <b>requests</b> to make the GET or POST requests.
#### Python Requests
To install this, all you have to do is `pip install requests` . However pip does not come installed with Intel Edison as of now.
To install pip do the following:

1. Download get-pip.py using `curl -OL https://bootstrap.pypa.io/get-pip.py`.

2. `$ python get-pip.py install`

This is how you make a GET request
``` import requests 
link ="localhost:3000/"
def makeGetreq():
    r = requests.get(link)
    curValue = r.text
    if curValue == "none":
        return None
    else:
        return curValue 
```

This is how you make a POST request
``` 
import requets
import json
link ="localhost:3000/"

def checkResponse():
        r = requests.get(link)
        curValue = r.status_code
        #print curValue
        if (curValue==200):
                print "Value Posted"
        else:
                print "Error Response Code",curValue

def postRequest(inp):
        headers = {'content-type': 'application/json'}         
        r = requests.post(link,data=json.dumps(inp),headers = headers) 
        print (r.text)
        checkResponse()
        
```