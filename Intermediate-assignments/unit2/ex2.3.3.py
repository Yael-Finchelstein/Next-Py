class Dog:
    count_animals = 0

    def __init__(self, name="Octavio"):
        Dog.count_animals += 1
        self._name = name
        self._age = 6

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def set_name(self, new_name):
        self._name = new_name

    def get_name(self):
        return self._name


def main():
    cacao = Dog()
    cacao.set_name("Cacao")
    vanilla = Dog()
    print("First instance:", cacao.get_name())
    print("Second instance:", vanilla.get_name())
    vanilla.set_name("Vanilla")
    print("Second instance after changing its name:", vanilla.get_name())
    print("count_animals =", vanilla.count_animals)


if __name__ == '__main__':
    main()
