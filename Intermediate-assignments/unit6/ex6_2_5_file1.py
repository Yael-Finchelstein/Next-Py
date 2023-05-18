class GreetingCard:
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_message(self):
        print("The sender is {} and the recipient is {} !".format(self._sender, self._recipient))
