from parse_rest.connection import register
from parse_rest.datatypes import Object
import time
from apns import APNs, Frame, Payload
from twilio.rest import TwilioRestClient
register("lkHCX43bL8tqi0kpiICrOdXLlcx6yxDs3k9rUE5A", "uIE9zOF0dsbr5N9uPrtF2eBDiuGiIhuffvFsdaaA", master_key="ikropQhezf8HiYJKg0ZidOJ0Oa2I9RLRsdzP16Zt")

account_sid = "ACa4d40581688ac7d51dc5c16b3c7e2137" #twilio
auth_token  = "c8538afb552415cf2fa302df659d91c3" #twilio
client = TwilioRestClient(account_sid, auth_token) #twilio

class Users(Object):
	self.name = "" 			#user's name
	self.contacts = "" 		#contacts.split(',') to convert to list. storing all emergency contacts here. looks like only phone numbers are necessary?
	#self.emails = [] 		#maybe we can do something like this?
	self.lastPing = 99 		#unix time, seconds
	self.lastResponse = 99 	#unix time, seconds
	self.latitude = 30
	self.longitude = 30
	self.onTrip = False
	self.pingInterval = 30 	#in MINUTES


#NOTE: ONLY IOS APP WILL BE ADDING/EDITTING THE Users TABLE. WE ARE RETRIEVING DATA FROM PARSE.
cur_time = time.now() #in unix time
while True:
	time.sleep(60) #so we don't overload the db
	users = Users.Query.all()
	for user in users:
		if user.onTrip: 	#skips users who aren't on a trip
			cur_time = time.now()

			#check if response was late, i.e. time is up and last response was before last ping
			#if yes, send twilio stuff
			#else if now is ping + pinginterval*60, send another ping, update values

			if cur_time >= user.lastPing + user_pintInterval*60 and user.lastResponse < user.lastPing:
				#user hasn't responded to last ping, i.e. in an emergency
				nums = users.contacts.split(',')
				for num in nums:
					#twilio code for sending emergency msg to all emergency contacts. include info about gps and current time
					message = client.messages.create(body= "%s did not check in, person was last at GPS Coordinates [%.3f, %.3f]" % (user.name, user.latitude, user.longitude)
													to= "+1"+ num,    # Replace with your phone number
													from_="+19099627422") #twilio phone number
			elif cur_time >= user.lastPing + user.pingInterval*60:
				#update lastPing
				user.lastPing = cur_time
				#send push notification to iphone
				token_hex = '2ae38011b9d95323b090a0905dbce4f0b61341b0409892343b21330e976572c8'
				payload = Payload(alert="Hello! Please check-in", sound="default", badge=1)
				apns.gateway_server.send_notification(token_hex, payload)
