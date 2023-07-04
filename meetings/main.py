from json import load, dump
from datetime import datetime, timedelta
from meetings.Meetings import Meeting
from meetings.Calendar import Calendar

calendar = Calendar()

# odczyt
with open("meetings.json") as file:
    data = load(file)
    # lista slownikow
    for item in data:
        meeting = Meeting(datetime.strptime(item["date"], "%d.%m.%Y %H:%M"),
                          item["title"])
        calendar.add_meeting(meeting)

# klucz to data a wartosc to obiekt !!!

while True:
    if __name__ == "__main__":
        # print("Kalendarz 2020")
        option = input("(l)ista, (d)odaj, (q)uit: ")
        if option == "l":
            for _, meeting in calendar.meetings.items():
                print(f"{meeting.date}: {meeting.title}")
        elif option == "d":
            name = input("Tytul spotkania? ")
            date = input("Data spotkania dd.mm.rrrr h:m")  # ewentualnie bez godziny
            meeting_date = datetime.strptime(date, "%d.%m.%Y %H:%M")  # ewentualnie bez godziny
            calendar.add_meeting(Meeting(meeting_date, name))

            with open("meetings.json", "w") as file:
                data = []
                for meeting in calendar.meetings.values():
                    data.append({
                        "title": meeting.title,
                        "date": meeting.date.strptime(date, "%d.%m.%Y %H:%M")
                    })
                dump(data, file)

        elif option == "q":
            break
        else:
            print("nie wiem co wybrac")

