from abc import ABC, abstractmethod
from exceptions import CategoryNotFound
from terminaltables import AsciiTable


class AbstractView(ABC):

    def __init__(self):
        self.repositories = {}

    @abstractmethod
    def draw(self):
        pass

    def set_repository(self, name, repository):
        self.repositories[name] = repository


class AddView:
    def get_category_id(self, repository):
        found_category = False
        category_id = None
        while not found_category:
            try:
                category_name = input("Kategoria: ")
                category_id, name = repository.get_by_name(category_name)
                found_category = True
            except TypeError:
                print("typeError")
                found_category = False
        return category_id


class AddCost(AbstractView, AddView):
    SHORTCUT = "dk"
    LABEL = "Dodaj koszt"

    def draw(self):
        print(AddCost.LABEL)
        title = input("Tytul: ")
        amount = float(input("Wartosc: "))
        category_id = self.get_category_id(self.repositories["category"])
        self.repositories["entry"].save(title, category_id, amount * -1)


class ListCosts(AbstractView):
    SHORTCUT = "wk"
    LABEL = "Wypisz koszty"

    def draw(self):
        print(ListCosts.LABEL)
        rows = [
            ["name", "data dodania", "kwota", "kategoria"]
        ]
        for _, name, cost_id, created_at, amount, category in self.repositories["entry"].get_incomes():
            # print(created_at, amount, category),
            rows.append([name, created_at, amount, category])
        table = AsciiTable(rows)
        print(table.table)


class AddIncome(AbstractView, AddView):
    SHORTCUT = "DP"
    LABEL = "Dodaj przychodzy"

    def draw(self):
        print(AddIncome.LABEL)
        title = input("Tytul: ")
        amount = float(input("Wartosc: "))
        category_id = self.get_category_id(self.repositories["category"])
        self.repositories["entry"].save(title, category_id, amount)


class ListIncomes(AbstractView):
    SHORTCUT = "WP"
    LABEL = "Wypisz przychody"

    def draw(self):
        print(ListIncomes.LABEL)
        rows = [
            ["name", "data dodania", "kwota", "kategoria"]
        ]
        for _, name, created_at, amount, category in self.repositories["entry"].get_costs():
            # print(created_at, amount, category),
            rows.append([name, created_at, amount, category])
        table = AsciiTable(rows)
        print(table.table)

class Report(AbstractView):
    SHORTCUT = "r"
    LABEL = "Raport"

    def draw(self):
        repository = self.repositories["report"]
        quantity, saldo = repository.get_saldo()
        print(f"Ilosc operacji {quantity}")
        print(f"Saldo {quantity}")

        rows = [["Nazwa", "Ilosc", "Saldo"]]
        rows += [[category_name, quantity, saldo] for category_name, quantity, saldo in repository.get_by_category()]
        table = AsciiTable(rows)
        print(table.table)


class MainMenu:
    OPTIONS = {
        AddCost.SHORTCUT: AddCost(),
        ListCosts.SHORTCUT: ListCosts(),
        AddIncome.SHORTCUT: AddIncome(),
        ListIncomes.SHORTCUT: ListIncomes(),
        Report.SHORTCUT: Report()
    }

    def get_screen(self):
        option = None
        while option not in MainMenu.OPTIONS:
            option = input("Wybierz opcje: ")
        return MainMenu.OPTIONS[option]

    def draw(self):
        print("Powiedz co chcesz zrobic")
        for shortcut, objj in MainMenu.OPTIONS.items():
            print(f"{shortcut} - {objj.LABEL}")
