'''The below code is written and maintained by Rishi Gaurav Bhatnagar '''


''' All the modules you will are written here'''
#--------------------------------
import requests
import json
import time
#---------------------------------
link = "localhost:3000/"
#----------------------------------
''' Cloud Section '''
#----------------------------------
def postRequest(inp):
        headers = {'content-type': 'application/json'}
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
#-------------------------------------------
''' Using a while True is not the most effective use of your processor, hence you should always go with Interrupt Driven Programming. More on it in a different example'''
#-------------------------------------------
while True:
        val = raw_input("Enter the value you want to post to cloud: ")
        #print val 
        postRequest({"value":str(val)})
        
        