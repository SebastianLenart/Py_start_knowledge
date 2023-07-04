class User:
    def login(self):
        return "jestem zalogowany"

class Teacher(User):
    def run(self):
        return "nauczam"

class Student(User):
    def run(self):
        return "studiuje"

johny = Student()
print(johny.login())

# przeciazanie to metoda dziecka o tej samej nazwie co rodzica