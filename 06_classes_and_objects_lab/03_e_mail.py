class Email:

    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.message}. Sent: {self.is_sent}"


email_list = []

command = input()

while command != "Stop":
    command = command.split()
    email = Email(command[0], command[1], command[2])
    email_list.append(email)
    command = input()

[email_list[int(x)].send() for x in input().split(", ")]
print(f"\n".join([email.get_info() for email in email_list]))
