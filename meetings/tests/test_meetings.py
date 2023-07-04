from datetime import datetime, timedelta
from meetings.Meetings import Meeting
from meetings.Calendar import Calendar


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
    next_time_slot = calendar.next_availabe_slot(datetime(2020, 11, 9, 13, 0))

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
    # given
    birthday1 = Meeting(datetime(2020, 11, 9, 12, 0), "Urodziny")
    birthday2 = Meeting(datetime(2020, 11, 9, 12, 0), "Urodziny")

    # when
    calendar = Calendar()
    calendar.add_meeting(birthday1)
    calendar.add_meeting(birthday2)

    # then
    assert len(calendar.meetings) == 1
