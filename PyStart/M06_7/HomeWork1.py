from datetime import datetime


class Application:
    @staticmethod
    def main():
        first_name = input("First name: ")
        last_name = input("Last name: ")
        date_of_employment = datetime.strptime(input("Date of employment: "), "%Y.%m.%d")  # y - 22, Y - 2022
        if not Application.check_date_of_employment(datetime.today(), date_of_employment):
            raise InvalidDateOfEmployment()

        employee = BaseEmployee(first_name, last_name, date_of_employment)

    @staticmethod
    def check_date_of_employment(today: datetime, date: datetime):
        difference = today - date
        difference_in_years = round(difference.days / 365.25)  # co 4 lata rok przestepny
        return difference_in_years < 50 or difference_in_years > 0


class InvalidDateOfEmployment(Exception):
    print("blad")


class BaseEmployee:
    def __init__(self, first_name: str, last_name: str, date_of_employment: datetime):
        self.date_of_employment = date_of_employment
        self.last_name = last_name
        self.first_name = first_name

    @property  # bez nawiasow
    def employment_time(self):
        today = datetime.today()
        difference = today - self.date_of_employment
        return difference.days

    # do sortowania
    def __lt__(self, other):
        return self.employment_time < other.employment_time
    # do wyswietlania - sortowania
    def __repr__(self):
        return self.first_name


if __name__ == "__main__":
    Application.main()


def test__sort_employment():
    # given
    a = BaseEmployee("A", "A", datetime(2020, 12, 10))
    b = BaseEmployee("B", "B", datetime(2020, 11, 10))
    employees = [a, b]

    # when
    sorted_employees = sorted(employees)

    # then
    assert sorted_employees[0] == a
