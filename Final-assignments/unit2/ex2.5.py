# יצירת מחלקה בשם Animal
class Animal:
    # הוספת תכונה מסוג תכונת-מחלקה zoo_name במחלקה Animal עם הערך "Hayaton"
    zoo_name = "Hayaton"

    # יצירת מתודת אתחול (__init__) במחלקת Animal שמקבלת כפרמטרים תכונות: שם ומידת רעב
    # מתן ערך ברירת מחדל 0 לתכונה hunger_ ואתחול התכונה name_
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    # מימוש מתודה get_name במחלקה Animal שמחזירה את שם החיה
    def get_name(self):
        return self._name

    # מימוש מתודה is_hungry במחלקה Animal שמחזירה ערך בוליאני (האם החיה רעבה?)
    def is_hungry(self):
        if self._hunger > 0:
            return True
        else:
            return False

    # מימוש מתודה feed שמורידה ממידת הרעב של החיה נקודה אחת
    def feed(self):
        self._hunger -= 1

    # מימוש מתודה talk במחלקה Animal שלא עושה כלום (pass)
    def talk(self):
        pass


# יצירת תת מחלקה בשם Dog שיורשת ממחלקה Animal
class Dog(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    # מימוש מתודה talk במחלקה Dog שמדפיסה woof woof
    def talk(self):
        print("woof woof")

    # מימוש המתודה fetch_stick במחלקה Dog המדפיסה !There you go, sir
    def fetch_stick(self):
        print("There you go, sir!")


# יצירת תת מחלקה בשם Cat שיורשת ממחלקה Animal
class Cat(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    # מימוש מתודה talk במחלקה Cat שמדפיסה meow
    def talk(self):
        print("meow")

    # מימוש המתודה chase_laser במחלקה Cat שמדפיסה Meeeeow
    def chase_laser(self):
        print("Meeeeow")


# יצירת תת מחלקה בשם Skunk שיורשת ממחלקה Animal
class Skunk(Animal):
    # הוספת התכונה stink_count_ במחלקה Skunk ואתחול בערך ברירת מחדל = 6
    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    # מימוש מתודה talk במחלקה Skunk שמדפיסה tsssss
    def talk(self):
        print("tsssss")

    # מימוש המתודה stink במחלקה Skunk שמדפיסה Dear Lord!
    def stink(self):
        print("Dear lord!")


# יצירת תת מחלקה בשם Unicorn שיורשת ממחלקה Animal
class Unicorn(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    # מימוש מתודה talk במחלקה Unicorn שמדפיסה Good day, darling
    def talk(self):
        print("Good day, darling")

    # מימוש המתודה sing במחלקה Unicorn שמדפיסה i'm not your toy...
    def sing(self):
        print("I’m not your toy...")


# יצירת תת מחלקה בשם Dragon שיורשת ממחלקה Animal
class Dragon(Animal):
    # הוספת התכונה color_ למחלקה Dragon ואתחול בערך ברירת מחדל = "'Green"
    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    # מימוש מתודה talk במחלקה Dragon שמדפיסה Raaaawr
    def talk(self):
        print("Raaaawr")

    # מימוש המתודה breath_fire במחלקה Dragon שמדפיסה $@#$#@$
    def breath_fire(self):
        print("$@#$#@$")


# מימוש פונקציה ראשית בשם main
def main():
    Brownie = Dog("Brownie", 10)  # יצירת מופע Dog עם הערכים Brownie ו-10
    Zelda = Cat("Zelda", 3)  # יצירת מופע Cat עם הערכים Zelda ו-3
    Stinky = Skunk("Stinky")  # יצירת מופע Skunk עם הערכים Stinky ו-0
    Keith = Unicorn("Keith", 7)  # יצירת מופע Unicorn עם הערכים Keith ו-7
    Lizzy = Dragon("Lizzy", 1450)  # יצירת מופע Dragon עם הערכים Lizzy ו-1450
    Doggo = Dog("Doggo", 80)  # יצירת מופע של המחלקה Dog עם הערכים Doggo ו-80
    Kitty = Cat("Kitty", 80)  # יצירת מופע של המחלקה Cat עם הערכים Kitty ו-80
    Stinky_Jr = Skunk("Stinky Jr.", 80)  # יצירת מופע של המחלקה Skunk עם הערכים Stinky Jr. ו-80
    Clair = Unicorn("Clair", 80)  # יצירת מופע של המחלקה Unicorn עם הערכים Clair ו-80
    McFly = Dragon("McFly", 80)  # יצירת מופע של המחלקה Dragon עם הערכים McFly ו-80
    # יצירת רשימה בשם zoo_lst והוספת 10 המופעים
    zoo_lst = [Brownie, Zelda, Stinky, Keith, Lizzy, Doggo, Kitty, Stinky_Jr, Clair, McFly]
    # מעבר על הרשימה zoo_lst בלולאה
    for animal in zoo_lst:
        print(type(animal).__name__, animal.get_name())  # הדפסת סוג של כל חיה ושמה
        while animal.is_hungry():  # האכלת כל חיה באמצעות המתודה feed עד שהיא לא רעבה יותר
            animal.feed()
        animal.talk()  # קריאה למתודה talk עבור כל המופעים שבתוך zoo_list
        # קריאה לכל אחת מהמתודות המיוחדות עבור כל המופעים שבתוך zoo_list
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()
    print(zoo_lst[0].zoo_name)  # הדפסת התכונה zoo_name פעם אחת בסוף התוכנית


if __name__ == '__main__':
    main()
