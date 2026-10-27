def add(a, b):
    return a + b


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_number():
    assert add(-2, 5) == 3


def test_add_zero():
    assert add(7, 0) == 7
