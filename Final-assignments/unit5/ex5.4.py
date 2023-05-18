def check_id_valid(id_number):
    """
    Checks the validity of an ID number.
    Params:
    - id_number (int): The ID number to be checked.
    Returns:
    - bool: True if the ID number is valid, False otherwise.
    """
    return sum(int(digit) if i % 2 == 0 else sum(map(int, str(int(digit) * 2))) for i, digit in enumerate(str(id_number))) % 10 == 0


class IDIterator:
    """
    Iterator class for generating valid ID numbers in a given range.
    Attributes:
    - id_ (int): The starting ID number.
    Methods:
    - __iter__(): Returns the iterator object.
    - __next__(): Generates the next valid ID number.
    Raises:
    - StopIteration: If the iterator reaches the end of the range.
    """

    def __init__(self, id_):
        """
        Initialize the IDIterator object with the starting ID number.
        Params:
        - id_ (int): The starting ID number.
        """
        self._id = id_

    def __iter__(self):
        """
        Returns the iterator object.
        """
        return self

    def __next__(self):
        """
        Generates the next valid ID number.
        Returns:
        - int: The next valid ID number.
        Raises:
        - StopIteration: If the iterator reaches the end of the range.
        """
        self._id += 1
        while self._id <= 999999999:
            if check_id_valid(self._id):
                return self._id
            self._id += 1
        raise StopIteration


def id_generator(id_number):
    """
    Generator function for generating valid ID numbers in a given range.
    Params:
    - id_number (int): The starting ID number.
    Yields:
    - int: The next valid ID number.
    """
    current_id = id_number + 1
    while current_id <= 999999999:
        if check_id_valid(current_id):
            yield current_id
        current_id += 1


def main():
    """
    Main program to generate and print new valid ID numbers.

    Asks the user to input an ID number and choose between using an Iterator or a Generator.
    Generates and prints 10 new valid ID numbers based on the user's choice.
    """
    id_number = int(input("Please enter your ID: "))
    what_to_use = input("Generator or Iterator? (gen/it)? ")
    count = 10
    if what_to_use == "it":
        iterator = iter(IDIterator(id_number))
        for n in range(count):
            new_id = next(iterator)
            print(new_id)
    elif what_to_use == "gen":
        generator = id_generator(id_number)
        for n in range(count):
            new_id = next(generator)
            print(new_id)


if __name__ == '__main__':
    main()
