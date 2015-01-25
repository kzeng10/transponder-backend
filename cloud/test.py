import time
from twilio.rest import TwilioRestClient
from apns import APNs, Frame, Payload
from parse_rest.connection import register
from parse_rest.datatypes import Object

register(<application_id>, <rest_api_key>[, master_key=None])

account_sid = "ACa4d40581688ac7d51dc5c16b3c7e2137"
auth_token  = "c8538afb552415cf2fa302df659d91c3"
client = TwilioRestClient(account_sid, auth_token)

class User(Object):
    pass

run = 0
mins = raw_input("Mins?") #change this to whatever sets the time of the trip
while mins != 0:
    time.sleep(60)
    mins -= 1
if mins == 0:
    token_hex = '*******'
    payload = Payload(alert="Hello! Please check-in", sound="default", badge=1)
    apns.gateway_server.send_notification(token_hex, payload)
    while mins != 15:
        time.sleep(60)
        mins += 1
        if #user takes action on push notification:
            isVerified = true;
            break
        else:
            message = client.messages.create(body= user.name "did not check in, person was last at" user.location,
                to="+14155496801",    # Replace with your phone number
                from_="+19099627422") # Replace with your Twilio number
            print message.sid
