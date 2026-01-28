

"""Add 2+2=4 and expect test to pass"""

def test_two_plus_two_pass():
    assert 2+2 == 4

"""Add 3 and five and expect test to fail"""

def test_three_plus_five_fail():
    assert 3+5 == 7