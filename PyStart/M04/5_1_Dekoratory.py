def rount_it(func):
    def wrapper(*args, **kwargs):
        return round(func(*args, **kwargs), 2)

    return wrapper


def test_round_it():
    @rount_it
    def function(value):
        return value

    assert function(3.567) == 3.57
    assert function(3.5000) == 3.5