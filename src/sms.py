from twilio.rest import Client
import os

def send(body='Some body', to=''):

    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("account_token")
    client = Client(account_sid,auth_token)

    message = client.messages.create(    
        body=body,
        from_='+19073121481',
        to="+1"+to
        )

    print(message.sid)

