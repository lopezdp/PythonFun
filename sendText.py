from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC00ff568b5d1ef3414aba48171940c8f0"
# Your Auth Token from twilio.com/console
auth_token  = "8a40318de19505e55c74f8e10681c22b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+15077666336", 
    from_="+17866591787",
    body="A computer program written in Python is fucking with you right now. This text is from God bitch. Let me know when you get this so I can see what it looks like on your end...")

print(message.sid)
