from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACeb3d26462aaf25561b2b48f19f81ec8e'
auth_token = '849b3bfee0fd1c07f70c3f06a7941fa6'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Nurul Haque.",
                     from_='+12016251678',
                     to='+917381483057'
                 )

print(message.sid)
