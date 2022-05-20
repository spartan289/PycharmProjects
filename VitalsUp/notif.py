import requests

from twilio.rest import Client
import time

account_sid = 'AC68670b4fae13f8d09770df687c7260c5'
auth_token = '83ddbc0cdea235d26a97f21c98644ffd'
client = Client(account_sid, auth_token)
HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
while(True):

    page = requests.get('http://www.du.ac.in/index.php?page=news',headers=HEADERS)
    current_length =163532
    print(page.text)
    print(len(page.text))
    # if len(page.text)!=163532:
    #     print("New notification")
    #     time.sleep(10)
    #     call = client.calls.create(
    #         twiml='<Response><Say>Hello there! your website is updated and i think there is a new notification</Say></Response>',
    #         to='+919310399182',
    #         from_='+18608314588'
    #     )
    #     message = client.messages.create(
    #         to='+919310399182',
    #         from_='+18608314588',
    #         body='Hello there! your website is updated and i think there is a new notification'
    #     )
    #     print(message.sid)
    #     print(call.sid)
    #     break
    print("No new notification")
    time.sleep(10)