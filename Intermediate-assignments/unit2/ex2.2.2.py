class Dog:
    def __init__(self):
        self.name = "Cacao"
        self.age = 6

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


def main():
    cacao = Dog()
    cacao.birthday()
    print(cacao.get_age())
    vanilla = Dog()
    print(vanilla.get_age())


if __name__ == '__main__':
    main()
