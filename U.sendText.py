from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "**"
# Your Auth Token from twilio.com/console
auth_token  = "**"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+**", 
    from_="+**",
    body="A computer program written in Python is fucking with you right now. This text is from God bitch. Let me know when you get this so I can see what it looks like on your end...")

print(message.sid)
