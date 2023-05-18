from ex6_2_5_file1 import GreetingCard
from ex6_2_5_file2 import BirthdayCard


def main():
    greeting = GreetingCard("Tomer", "Maya")
    birthday = BirthdayCard(sender_age=18, sender="Yael")

    greeting.greeting_message()
    birthday.greeting_message()


if __name__ == '__main__':
    main()
