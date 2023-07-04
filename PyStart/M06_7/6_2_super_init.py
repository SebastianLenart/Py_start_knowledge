class Person:
    def __init__(self, first_name, last_name):
        self.details = f"{first_name} {last_name}"


class Student(Person):
    def __init__(self, first_name, last_name, semestr):
        super().__init__(first_name, last_name)
        self.semestr = semestr


jan = Student("Jan", "Kowalski", 2)
print(jan.details)
print(jan.semestr)