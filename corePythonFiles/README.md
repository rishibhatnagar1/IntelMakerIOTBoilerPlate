#Core Files written in Python
This section will have all the pseudo codes you would need to work on your next IOT project. This is all written in Python.

####All the codes above have been written in Python 2.7 and should work fine with most of your systems, Intel Edison/Raspberry Pi/ BBB

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

#### Python Requests
To install this, all you have to do is `pip install requests` . However pip does not come installed with Intel Edison as of now.
To install pip do the following:
1. Download get-pip.py using `curl -OL https://bootstrap.pypa.io/get-pip.py`
2. `$ python get-pip.py install`

###For any questions/issues please reach out to @rishigb or raise them here
