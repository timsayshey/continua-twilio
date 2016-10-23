#!/usr/bin/python

from flask import Flask
import twilio.twiml


application = Flask(__name__)

@application.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Thank you for calling Continua. Please leave a message.")
    resp.record(maxLength="120", action="/handle-recording", transcribe=True)
    return str(resp)

@application.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
	"""After a recording, this is called."""
	resp = twilio.twiml.Response()
	resp.say("Thank you.  Someone will reach out to you shortly.")

	return str(resp)

if __name__ == "__main__":
	application.run(host='0.0.0.0')




