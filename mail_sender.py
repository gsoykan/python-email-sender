import smtplib, ssl


# sources: https://geekflare.com/send-gmail-in-python/
# https://stackoverflow.com/questions/57715289/how-to-fix-ssl-sslerror-ssl-wrong-version-number-wrong-version-number-ssl
# https://stackoverflow.com/questions/16512592/login-credentials-not-working-with-gmail-smtp
class MailSender:

    def __init__(self,
                 sender_mail: str,
                 sender_password: str):
        self.port = 587
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender_mail = sender_mail
        self.password = sender_password

    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP(self.smtp_server_domain_name, self.port)
        service.ehlo()
        service.starttls(context=ssl_context)
        service.ehlo()
        service.login(self.sender_mail, self.password)

        for email in emails:
            result = service.sendmail(self.sender_mail, email, f"Subject: {subject}\n{content}")

        service.quit()
