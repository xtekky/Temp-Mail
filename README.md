# Temp Mail
 Python TempMail client using https://temp-mail.org/ with cloudflare bypass


email_client = TempMail()
token, email = email_client.get_mail()
print(email)
print(token)

```py

while True:
    time.sleep(5)
    messages = email_client.fetch_inbox()
    print(messages)
    
    if len(messages["messages"]) > 0:

        email_content = email_client.get_message_content(messages["messages"][0]["_id"])
        print(email_content)
```
