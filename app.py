from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from sms import send

# initializing app
app = Flask(__name__)

## setup our routes
@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=["POST"])
def sms():
    incoming_msg = request.values.get('Body', '').lower()
    client = request.values.get('From').replace('whatsapp:', '')
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg == 'help':
        msg.body('Just type "Help" to see this menu:\nOr type "Kota" to see our kota menu:\nOr type "Steak" to see our stake menu:\nOr type "About" to find out more info about u')

    elif 'hello' in incoming_msg:
    	msg.body('Hello, how can I help you today?\nJust type "Help" to see this menu:\nOr type "Kota" to see our kota menu:\nOr type "Steak" to see our stake menu:\nOr type "About" to find out more info about us')
    	
    elif 'hi' in incoming_msg:
    	msg.body('Hi, how can I help you today?\nJust type "Help" to see this menu:\nOr type "Kota" to see our kota menu:\nOr type "Steak" to see our stake menu:\nOr type "About" to find out more info about us')
    	
    elif 'kota' in incoming_msg:
    	msg.body('Thanks for asking about our Kota menu.\n1. R12 French, Chips, Vienna\n2. R15 French, Chips, Vienna, Russian\n\n*To order a kota, type "Order" followed by a product\ne.g. Order 12 kota')
    	
    elif 'steak' in incoming_msg:
    	msg.body('Thanks for asking about our Steak menu.\n3. R12 Medium steak, pap, gravvy\n4. R15 Large steak, pap, gravvy, salads\n\n*To order a steak, type "Order" followed by a product\ne.g. Order 12 steak')
    	
    elif 'about' in incoming_msg:
    	msg.body('We are Senzo Fast Food and we are situated at 3730 Mofutsanyane Street, Orlando East.\n We open from 8 am to 8 pm. call us @ 071 840 8284') 
    elif 'order' in incoming_msg:
    	order = f'{client} {incoming_msg}'
    	send(order)
    	msg.body('Your order was submitted successfully')
    	
    else:
    	msg.body('Oops I did not get that.\nJust type "Help" to see this menu:\nOr type "Kota" to see our kota menu:\nOr type "Steak" to see our stake menu:\nOr type "About" to find out more info about u')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
