from twilio.rest import Client
from credentials import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid, auth_token)
my_msg = 'hello da nanthagopal this is me'
message = client.messages.create(to=my_cell, from_=my_twilio, body=my_msg)

print(client)
print(my_msg)
print(message)
