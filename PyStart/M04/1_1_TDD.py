def count_letters(text, start='(', end=')'):
    should_count = False
    counter = 0
    temp_counter = 0
    for char in text:

        if char == end:
            should_count = False
            counter += temp_counter
            temp_counter = 0

        if should_count:
            temp_counter += 1

        if char == start:
            should_count = True

    return counter


def test_cout_letters_once():
    assert count_letters('Samuraj (programowania)') == 13


def test_count_letters_none():
    assert count_letters('Samuraj') == 0
    assert count_letters('Py(th)on', '<', '>') == 0


def test_multiple_brackets():
    assert count_letters('<Nauka> <Programowanie>', '<', '>') == 18
    assert count_letters('(Nauka) (Programowanie)') == 18

# jak nie ma ( to zwraca 0
