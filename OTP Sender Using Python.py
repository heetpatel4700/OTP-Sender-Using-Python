import requests 
import json
import math, random

 
url = "https://www.fast2sms.com/dev/bulk"
string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
lent =len(string)
otp=""
for i in range(6):
  otp+= string[math.floor(random.random()*lent)]
  
  
 
my_data = { 
     
    'sender_id': 'FSTSMS',  
    
    #Write your on message between  ''  
    'message': otp + ' is your OTP' ,  
    
    'language': 'english', 
    'route': 'p', 
    
     
    'numbers': '9999999999' ,'888888888'  , '7777777777'    
} 
  
# Write you api key from Fast2sms in authorization.
headers = { 
    'authorization': 'Write your api key', 
    'Content-Type': "application/x-www-form-urlencoded", 
    'Cache-Control': "no-cache"
}

 
response = requests.request("POST", 
                            url, 
                            data = my_data, 
                            headers = headers) 

returned_msg = json.loads(response.text) 
   
print(returned_msg['message'])