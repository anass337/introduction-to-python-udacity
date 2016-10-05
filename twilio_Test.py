# -*- coding: cp1252 -*-
from twilio import rest

account_sid = "ACf80ee38d0f4c91ac65620233ceebf213"
auth_token  = "f8375cac27b469c69981ee1afa2fca18"  

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="bonsoir abir çava?",
    to="+212641746916",    
    from_="+17075952048")

print(message.sid)
