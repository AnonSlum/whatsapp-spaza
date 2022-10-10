from twilio.rest import Client
from decouple import config

sid = config('SID')
auth = config('AUTH')


def send(mess):
    account_sid = sid
    auth_token = auth

    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(body=mess,
                            from_='+16785155520',
                            to='+27718408284')

    return message.sid


if __name__ == '__main__':
    print(send('Your order is ready'))
