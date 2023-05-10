from twilio.rest import Client

account_sid = 'account_sid'
auth_token = 'auth_token'
client = Client(account_sid, auth_token)

def send_sms(number, body):
    message = client.messages.create(
        from_='+number',
        body=body,
        to=number
    )
    return message.sid
