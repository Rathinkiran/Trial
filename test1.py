from email.message import EmailMessage
message=EmailMessage()
sender = "me@example.com"
recipient = "you@example.com"
message['From'] = sender
message['To'] = recipient
message['body']='Greetings from {} to {}'.format(sender,recipient)
body="Hey there!"
message.set_content(body)
print(message)
