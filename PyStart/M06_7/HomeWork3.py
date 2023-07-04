from abc import ABC, abstractmethod


class Actor(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @abstractmethod
    def hello(self):
        return f"Hello, My name is {self.first_name} {self.last_name}"


class Student(Actor):
    def hello(self):
        return Actor.hello(self) + " a student"


class Employee(Actor):
    def hello(self):
        return Actor.hello(self) + " an employee"


class Teacher(Actor):
    def hello(self):
        return Actor.hello(self) + " an teacher"


class Person:
    @staticmethod
    def create_new(class_name: str, first_name: str, last_name: str):
        """
        if class_name == "Teacher":
            return Teacher(first_name, last_name)
        else:
            print("cos tam")
        """
        try:  # jakby sie wpisało nieistaniejaca klase
            class_ = globals()[class_name]  # tylko jezeli kod znajduje sie w tym samum module, inaczej get artibiute
            return class_(first_name, last_name)  # nowy obiekt klasy class_name
        except KeyError:
            print(f"Unknown class name {class_name}.")


stanislaw = Teacher("Stas", "Lem")
print(stanislaw.hello())

stani = Person.create_new("Student", "Stass", "Kola")
print(stani.hello())
