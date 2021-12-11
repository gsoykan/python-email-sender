# python-email-sender
Email Sender via Python (GMAIL) 

## Example Usage

```
mails = ["grkansoykan@gmail.com"]
subject = "test subject"
content = "test content"
sender_mail = "grkansoykan@gmail.com"
password = "miavv"

mail = MailSender(sender_mail=sender_mail, sender_password=password)
mail.send(mails, subject, content)
```
