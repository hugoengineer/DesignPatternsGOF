class UserEmail:
    def __init__(self, email: str):
        self.email = email

    def notify(self, msg: str) -> None:
        print(f"Email sent to {self.email}: {msg}")


class EmailHandler:
    def __init__(self):
        self._emails = []

    def send_email(self, msg) -> None:
        if msg == "":
            return
        else:
            pass

    def add_observer(self, email) -> None:
        self._emails.append(email)

oberver1 = UserEmail("Ola")
oberver2 = UserEmail("Tudo bem")
sujeito = EmailHandler()
sujeito.add_observer(oberver1)
sujeito.add_observer(oberver2) 

sujeito.send_email("Mensagem importante")
sujeito.send_email("")  # Não deve notificar ninguém
sujeito.send_email("Outra mensagem importante")

print(f"Observers registrados: {len(sujeito._emails)}")
for observer in sujeito._emails:    
    print(f"- {observer.email}")
