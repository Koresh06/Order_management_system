from src.domain.services.user.send_email_intarface import EmailServiceInterface


class EmailService(EmailServiceInterface):
    def send_verification_email(self, email: str, token: str):
        print(f"Sending verification email to {email} with token {token}")