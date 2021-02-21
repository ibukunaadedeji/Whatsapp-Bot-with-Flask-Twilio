#import library
from flask import Flask
import requests
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__) #instantiating a flask variable

@app.route('/bot',methods=['POST'])

#create a bot function
def bot():
  incoming_message = requests.values.get('Body','').lower()
  resp = MessagingResponse()
  msg = resp.Message()
  responded = False
  if 'quote' in incoming_message():
     r = requests.get('https://api.quotable.io/random')
     if r.status_code == 200:
       data = r.json()
       quote = f'{data["content"]} ({data["author"]})'
     else:
       quote ='I could not retrieve any quote(s) at this time.'
     msg.body(quote)
     responded = True

  if 'cat' in incoming_message():
    msg.media('https://cataas.com/cat')
    responded = True
  if not responded :
    msg.body('I only know famous quotes and cats')
    return str(resp)





if __name__ == '__main__':
  app.run()