from abc import ABC, abstractmethod


class EmailServiceInterface(ABC):

    @abstractmethod
    def send_verification_email(self, email: str, token: str):
        pass