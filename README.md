# Temp-Mail Client

Python TempMail client using https://temp-mail.org/ with cloudflare bypass

### Requirements

:warning: `node-js` is required for the cloudflare client to run

Running `email.py` requires:

* Python `3.10.5` *(tested under Python 3.10.5)*
* node-js `16.17.0` *(tested under node-js 16.17.0)*

### Using the TempMail Client

1. Download `email.py` and the `client` folder
2. You can use this following template code

```py
from mail import TempMail

email_client = TempMail()
token, email = email_client.get_mail()
print(email)
print(token)

while True:
    time.sleep(5)
    messages = email_client.fetch_inbox()
    print(messages)
    
    if len(messages["messages"]) > 0:

        email_content = email_client.get_message_content(messages["messages"][0]["_id"])
        print(email_content)
```
