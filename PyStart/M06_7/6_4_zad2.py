class Employee:
    def __init__(self, first_name: str, last_name: str, hourly_rate: float):
        self.hourly_rate = hourly_rate
        self.last_name = last_name
        self.first_name = first_name
        self._time_spent = 0

    def add_time(self, time: float):
        self._time_spent += time

    def pay(self):
        return self._time_spent * self.hourly_rate

class Manager(Employee):
    def __init__(self, first_name: str, last_name: str, hourly_rate: float):
        super().__init__(first_name, last_name, hourly_rate)
        self.bonus = 0

    def add_bonus(self, bonus):
        self.bonus += bonus

    def pay(self):
        return super().pay() * 2 + self.bonus

manager = Manager("Fred", "Silnoreki", 100)
manager.add_time(3)
manager.add_bonus(500)
print(manager.pay()) # 1100


worker = Employee("Fred", "SSH", 50)
worker.add_time(4)
print(worker.pay()) # 200




















