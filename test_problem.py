import pytest
import random
from problem import word_score, player_tiles, BAG


def give_bag():
    return {
        'E': 12,
        'A': 9, 'I': 9,
        'O': 8,
        'N': 6, 'R': 6, 'T': 6,
        'L': 4, 'S': 4, 'U': 4, 'D': 4,
        'G': 3,
        'B': 2, 'C': 2, 'M': 2, 'P': 2, 'F': 2,
        'H': 2, 'V': 2, 'W': 2, 'Y': 2,
        'K': 1, 'J': 1, 'X': 1, 'Q': 1, 'Z': 1
    }


def test_return_word_score_valid():
    value = word_score("GUARDIAN")
    assert value == 10
    assert isinstance(value, int)


def test_return_word_score_invalid():
    with pytest.raises(TypeError):
        value = word_score(12345)

# if len of string <= 20


def test_return_player_tiles():
    value = player_tiles()
    assert len(value) == 7


def test_return_player_tiles_valid_bag():
    random.seed(12345)
    value = player_tiles()
    assert BAG["N"] == 5
    assert BAG["Z"] == 0


def test_return_player_tiles_valid_bag_2():
    random.seed(12345)
    bag = give_bag()
    value = player_tiles(bag)
    assert bag["N"] == 5
    assert bag["Z"] == 0


# def test_return_word_valid():
#     random.seed(12345)
#     value = ["H", "E", "L", "L", "O"]
#     result = return_word(value)
#     assert result == "HELLO"
