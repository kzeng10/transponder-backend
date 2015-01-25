import time
from twilio.rest import TwilioRestClient
from apns import APNs, Frame, Payload

account_sid = "ACa4d40581688ac7d51dc5c16b3c7e2137"
auth_token  = "c8538afb552415cf2fa302df659d91c3"
client = TwilioRestClient(account_sid, auth_token)


run = raw_input("Start? > ")
mins = 0
if run == "start": #change this to when trip ends
    token_hex = '*******'
    payload = Payload(alert="Hello! Please check-in", sound="default", badge=1)
    apns.gateway_server.send_notification(token_hex, payload)
    while mins != 15:
        time.sleep(60)
        mins += 1
        if #user takes action on push notification:
            break
        else:
            message = client.messages.create(body="test",
                to="+14155496801",    # Replace with your phone number
                from_="+19099627422") # Replace with your Twilio number
            print message.sid
