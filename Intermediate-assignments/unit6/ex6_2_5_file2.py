from ex6_2_5_file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, sender_age=0, recipient="Dana Ev", sender="Eyal Ch"):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_message(self):
        super().greeting_message()
        print("Happy birthday! The sender age is {} years old!".format(self._sender_age))

