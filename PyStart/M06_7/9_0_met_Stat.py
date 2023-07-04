"""
metody statyczne to zwykle funkce wrzucone do klasy
nie trtzeba tworzyc obiektu aby ja wywolac
WIELKIE LITERY jako wlasciwosc statyczne

"""
class Student:
    NEXT_ID = 1

    def __init__(self, first_name, last_name):
        self.id = Student.NEXT_ID
        self.first_name = first_name
        self.last_name = last_name
        Student.NEXT_ID += 1 # z kazdym nowym obiektem sie inkrementuje

    def hello(self):
        return f"{self.id}. {self.first_name} {self.last_name}"

# prywatna wlasciwosc statyczna
print("*"*10)
class Singleton:
    _INSTANCE = None

    @staticmethod
    def get_instance():
        if Singleton._INSTANCE is None:
            Singleton._INSTANCE = Singleton() # utworzenie klasy w klasie

        return Singleton._INSTANCE

app = Singleton.get_instance() # wew tego tworzony jest obiekt
print(app)









