#!/usr/bin/python

# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
auth_token = "c54a1b9fcbf4a60e286f95783f73158e"
account_sid  = "AC58f97b4fd7f58037617e5504eab52968"
client = TwilioRestClient(account_sid, auth_token)

#transcriptions = client.transcriptions.list()
#print(transcriptions)

# put your own credentials here
#ACCOUNT_SID = "AC051869050b6df8eaa020a31503ec8082"
#AUTH_TOKEN = "295a3570bbd5e10d18b0b43f0b0aa844"

#client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

print("================ TRANSCRIPTS =====================")


transcriptions = client.transcriptions.list()
for t in transcriptions:
	print t.transcription_text

print("================= CALLS ========================")

# Get Call log
calls = client.calls.list()
for call in calls:
	print("TO: {}, FROM:{}".format(call.to, call.from_))
