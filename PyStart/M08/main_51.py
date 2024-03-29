from views_51 import MainMenu
from repositories_53 import EntryRepository, CategoryRepository, ReportRepository
from exceptions import CategoryNotFound

class Application:

    def main(self):
        menu = MainMenu()
        menu.draw()
        category_repository = self.get_category_repository()
        entry_repository = self.get_entry_repository()
        report_repository = self.get_report_repository()

        screen = menu.get_screen()
        screen.set_repository("category", category_repository)
        screen.set_repository("entry", entry_repository)
        screen.set_repository("report", report_repository)
        screen.draw()

    def get_entry_repository(self):
        return EntryRepository()

    def get_category_repository(self):
        return CategoryRepository()

    def get_report_repository(self):
        return ReportRepository()


if __name__ == "__main__":
    try:
        app = Application()
        app.main()
    except CategoryNotFound:
        print("Brak kategorii")

