class Student:
    def __init__(self, semestr: int, data: str):
        self._data = data
        self._semestr = semestr  # prywatny atrybut

    def __str__(self):
        return f"{self._data}, semestr: {self._semestr}"


student = Student(1, "Sebastian")
print(student)
print(student._data)  # niby dziala
print(student._semestr)  # niby dziala
