from parse_rest.connection import register
from parse_rest.datatypes import Object
import time
from apns import APNs, Frame, Payload
from twilio.rest import TwilioRestClient
register("lkHCX43bL8tqi0kpiICrOdXLlcx6yxDs3k9rUE5A", "uIE9zOF0dsbr5N9uPrtF2eBDiuGiIhuffvFsdaaA", master_key="ikropQhezf8HiYJKg0ZidOJ0Oa2I9RLRsdzP16Zt")

account_sid = "ACa4d40581688ac7d51dc5c16b3c7e2137" #twilio
auth_token  = "c8538afb552415cf2fa302df659d91c3" #twilio
client = TwilioRestClient(account_sid, auth_token) #twilio

class EmergencyContacts(Object):
	#stores name of user's name and list of emergency phone numbers
	pass

class Confirmations(Object):
	#stores time sent, whether it is confirmed, gps coords, and interval (yes, redundant data, but how else do we store this value?)
	self.timeSent = datetime.datetime.now()
	self.isConfirmed = False
	self.reached = False
	self.user = "" 		#user's id, so we know who it is that just left
	self.interval = 60 	#number of minutes, user-configurable
	pass

#NOTE: ONLY IOS APP WILL BE ADDING ENTRIES TO EmergencyContacts AND Confirmations TABLES. WE ARE RETRIEVING DATA FROM PARSE.

#during setup, user inputs entry into EmergencyContacts with name= user's name and phonenumbers = list of emergency contacts
allEmergencyContacts = EmergencyContacts.Query.get(name=name).phoneNumbers #username is name of the iphone owner
lastConfirmation = Confirmations.Query.all().order_by("-createdAt").limit(1).createdAt #spits out Date of the most recent entry
while lastConfirmation != Confirmations.Query.all().order_by("-createdAt").limit(1).createdAt:
	#this is ridiculous lol
	#basically here it's continuously checking the most recent entry every 5 minutes
	time.sleep(300) 		#so we don't overload the db
	pass


#####################
#we reach here when we see that someone is leaving, i.e. we have a new most recent entry
while True:
	#calls this as often as indicated by Confirmations.interval (refer to time.sleep below) to check if the person is okay
	lastConfirmation = Confirmations.Query.all().order_by("-createdAt").limit(1).createdAt #spits out Date of the most recent entry
	time.sleep(lastConfirmation.interval * 60)
	mostRecent = Confirmations.Query.all().order_by("-createdAt").limit(1) #spits out Date of the most recent entry
	if not mostRecent.isConfirmed: 	#if user is in emergency
		for phone in allEmergencyContacts:
			message = client.messages.create(body= str(user.name) +  "did not check in, person was last at" + str(user.location),
				to= "+1"+ phone,    # Replace with your phone number
				from_="+19099627422")
		pass
	elif mostRecent.reached:
		system.exit(0)
	else:
		token_hex = '*******'
	    payload = Payload(alert="Hello! Please check-in", sound="default", badge=1)
	    apns.gateway_server.send_notification(token_hex, payload)
		pass

#run a checking script in another file?
