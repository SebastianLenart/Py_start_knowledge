from datetime import datetime, timedelta


class Meeting:
    def __init__(self, date: datetime, title: str):
        self.date = date
        self.title = title


class Calendar:
    def __init__(self):
        self.meetings = {}

    def is_available(self, date: datetime):
        return date not in self.meetings # przemysl to !

    def add_meeting(self, meeting: Meeting):
        if self.is_available(meeting.date):
            self.meetings[meeting.date] = meeting


    def next_availabe_slot(self, date: datetime):
        meeting_date = date
        while not self.is_available(meeting_date):
            # import timedelta
            meeting_date += timedelta(minutes=60)
        return meeting_date
        # stworzenie zmiennej potencjanej godziny spotkania
        # while - dopoki potencjalna godzina nie jest wolna
        # dodawaj po 1 godzienie do poten godziny

#--------------------------------------------------------------------------------

def test_check_next_available_time_slot():
    # given
    birthday1 = Meeting(datetime(2020, 11, 9, 12, 0), "Urodziny")
    birthday2 = Meeting(datetime(2020, 11, 9, 13, 0), "Urodziny")
    birthday3 = Meeting(datetime(2020, 11, 9, 14, 0), "Urodziny")
    calendar = Calendar()
    calendar.add_meeting(birthday1)
    calendar.add_meeting(birthday2)
    calendar.add_meeting(birthday3)

    # when
    next_time_slot =calendar.next_availabe_slot(datetime(2020, 11, 9, 13, 0))

    # then
    assert next_time_slot == datetime(2020, 11, 9, 15, 0)


def test_is_given_datetime_available():
    # given
    calendar = Calendar()

    # when
    next_time_slot = calendar.next_availabe_slot(datetime(2020, 11, 9, 13, 0))

    # then
    assert next_time_slot == datetime(2020, 11, 9, 13, 0)


def test_add_meeting():
    #given
    birthday1 = Meeting(datetime(2020, 11, 9, 12, 0), "Urodziny")
    birthday2 = Meeting(datetime(2020, 11, 9, 12, 0), "Urodziny")

    #when
    calendar = Calendar()
    calendar.add_meeting(birthday1)
    calendar.add_meeting(birthday2)

    #then
    assert len(calendar.meetings) == 1





# NOWY PROJEKT MEETINGS W INNYM FOLDERZE PODZIELONY NA ODDZIELNE PLIKI
    




