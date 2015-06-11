'''The below code is written and maintained by Rishi Gaurav Bhatnagar  '''


''' All the modules you will are written here'''
#--------------------------------
import mraa
import requests
import json
import time
#--------------------------------
''' Declare the flags, using flags can help you do various talks more efficiently and
 you can fine tune the code to work perfectly. Using them can help you find bugs in certain cases too '''

flag1 = 0 #Initializing the value globaly.
flag2 = 1 #This so that it enters the else statement in the while loop
#---------------------------------
link = "localhost:3000/"
#---------------------------------
''' Mapping the GPIOs '''
''' 
x = mraa.Gpio(pinNumber)
x = dir(mraa.DIR_IN)

'''
''' Say if you need to use pinNumber 2 , this is how the code is going to look like '''
x = mraa.Gpio(2)
x.dir(mraa.DIR_IN)
#----------------------------------
''' Cloud Section '''
#----------------------------------
def postRequest(inp):
        headers = {'content-type': 'application/json'} #All this mentioned in the documents
        r = requests.post(link,data=json.dumps(inp),headers = headers) 
        print (r.text)
        checkResponse()
        s= requests.get(link)
        curValue = s.status_code
        #print curValue for debugging
        ''' We will use HTTP Response code to check if the value has been posted '''        
        if (curValue==200):
                print "Value Posted"
        else:
                print "Error Response Code",curValue

def cloudPost(cmd):
        ''' You can mention the conditions for posting values to the cloud here 
                For posting a value use the format : postRequest({"value":"whateverValue"})
        '''
        if "s" in cmd:
                #postvalue This has to be in a particular format as shown below.
                postRequest({"value":"0"})
        if "o" in cmd:
                #postvalue This has to be in a particular format as shown below.
                postRequest({"value":"1"})
#-------------------------------------------
''' Using a while True is not the most effective use of your processor, hence you should always go with Interrupt Driven Programming. More on it in a different example'''
#-------------------------------------------
while True:
        val =  x.read()
        #print (val)
        if (val== 1 and flag1):
                #Use some flags here to make the code more efficient
                #post the value to cloud and trigger the change.
                cloudPost('o') #sends1
                ''' We change the status of the flags here so that the same value is not posted continuously '''
                flag1 = 0
                flag2 = 1
        elif(val == 0 and flag2):
                cloudPost('s') #sends0
                flag2 = 0
                flag 1 = 1
