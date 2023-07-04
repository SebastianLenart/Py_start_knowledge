from datetime import datetime, timedelta

from meetings.Meetings import Meeting


class Calendar:
    def __init__(self):
        self.meetings = {}

    def is_available(self, date: datetime):
        return date not in self.meetings  # przemysl to !

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
