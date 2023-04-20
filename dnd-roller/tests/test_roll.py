import pytest

from dnd_roller.dice import roll

SUPPORTED_SMALL_DICE = (4,6,8,10,12,20) 

@pytest.mark.parametrize("sides", SUPPORTED_SMALL_DICE)
def test_small_dice_return_valid_values(sides):
    result = roll(sides)
    assert 1 <= result <= sides

def test_d100_return_valid_value():
    result = roll(100)
    assert 1 <= result <= 100
    assert 100 % 10 == 0