def calculate_power(number):
    if number == 0:
        return 1
    return number * calculate_power(number-1)

def test_power_zero():
    assert calculate_power(0) == 1


def test_power():
    assert calculate_power(1) == 1
    assert calculate_power(5) == 5 * 4 * 3 * 2
