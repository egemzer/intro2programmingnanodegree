
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC75a1766e52f1a9e4c488cd319afea9d1"
# Your Auth Token from twilio.com/console
auth_token  = "591fa2cda3885b45bd21975d4273066a"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14043883521", 
    from_="+14158535565",
    body="Hi, this is artocrat. Want to buy a painting?")

print(message.sid)
