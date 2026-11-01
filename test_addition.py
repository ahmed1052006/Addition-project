from addition import addition


def test_positive_numbers():
    assert addition(5, 3) == 8


def test_negative_number():
    assert addition(-5, 3) == -2
