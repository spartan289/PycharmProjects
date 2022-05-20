from twilio.rest import Client

account_sid = 'AC68670b4fae13f8d09770df687c7260c5'
auth_token = '83ddbc0cdea235d26a97f21c98644ffd'
client = Client(account_sid, auth_token)
call = client.calls.create(
    twiml='<Response><Say>Hello there! your website is updated and i think there is a new notification</Say></Response>',
    to='+919310399182',
    from_='+18608314588'
)
# message = client.messages.create(
#     to='+919310399182',
#     from_='+18608314588',
#     body='Hello there! your website is updated and i think there is a new notification'
# )
print(call.sid)