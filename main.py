from twilio.rest import Client
import os

account_sid = os.environ["TWACCOUNTSID"]
auth_token = os.environ["TWAUTHTOKEN"]
client = Client(account_sid, auth_token)
def send_love():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='I love you',
        to='whatsapp:+447432133438'
    )

    print(message.sid)

