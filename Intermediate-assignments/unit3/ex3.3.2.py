class UnderAge(Exception):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return "Your age is less than 18. Your current age is {}, and in {} years you will be able to arrive Ido's birthday.".format(self._age, 18 - self._age)


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(name, age)
    except UnderAge as e:
        print(e)
    else:
        print("You should send an invite to " + name)


send_invitation("Yael", 17)
send_invitation("Yael", 20)
