def euklides_gd(a: int, b: int) -> int:
    if 0 == b:
        return a
    return euklides_gd(b, a % b)


    # while b != 0:
    #     c = a % b
    #     a, b = b, c
    # return a

def test_euklides_while():
    assert euklides_gd(8, 4) == 4
    assert euklides_gd(27, 36) == 9