# test driven development

def add_numbers(a: int, b: int) -> int:
    return a + b


def test_add_numbers():
    # given
    a = 2
    b = 3
    # when
    value = add_numbers(a, b)
    assert value == 5  # czy zadziala
    # lub krocej
    # assert add_numbers(2, 3) == 5


 # python -m pytest 1_0_TDD.py -vvv

