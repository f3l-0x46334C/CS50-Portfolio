from um import count


def test_basic_word():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1


def test_multiple_occurrences():
    assert count("um um um") == 3
    assert count("Um, thanks, um, regular expressions make sense now.") == 2


def test_with_punctuation():
    assert count("Hello, um, world!") == 1
    assert count("Um... what are regular expressions?") == 1
    assert count("Well, um... maybe, um!") == 2


def test_inside_other_words():
    assert count("plumber album alums") == 0
    assert count("summary aluminum") == 0
    assert count("alum? Um!") == 1


def test_mixed_cases():
    assert count("Um, um, UM, uM") == 4


def test_edge_cases():
    assert count("um at start") == 1
    assert count("at end um") == 1
    assert count("um!") == 1
    assert count("(um)") == 1
    assert count("um...") == 1
    assert count("") == 0
