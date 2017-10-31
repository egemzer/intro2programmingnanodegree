
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "TBD"
# Your Auth Token from twilio.com/console
auth_token  = "TBD"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+14043883521", 
    from_="+14158535565",
    body="Hi, this is artocrat. Want to buy a painting?")

print(message.sid)
