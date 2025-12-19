from plates import is_valid


# positive tests


def test_beginning_alphabetical():
    invalid_plates = ["1A", "12", "A1", "!A", "A!", "!", "1", " "]
    for plate in invalid_plates:
        assert is_valid(plate) == False

    valid_plates = ["AB123", "CS50", "XY"]
    for plate in valid_plates:
        assert is_valid(plate) == True


def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("AAA222") == True
    assert is_valid("AB123") == True


def test_invalid_length():
    assert is_valid("X") == False
    assert is_valid("ABCDEFG") == False


def test_start_with_number():
    assert is_valid("1XYZ") == False
    assert is_valid("12AB") == False


def test_first_number_zero():
    assert is_valid("CS05") == False
    assert is_valid("AB012") == False


def test_numbers_in_middle():
    assert is_valid("AB1CD") == False
    assert is_valid("CS50P") == False


def test_invalid_characters():
    assert is_valid("CS50?") == False
    assert is_valid("XY.ZX") == False
    assert is_valid("AB=CD") == False


def test_letters_only():
    assert is_valid("ABC") == True
    assert is_valid("ZZZZZZ") == True
    assert is_valid("abcdef") == True


"""
# negative tests


def test_invalid_plate_but_expect_true():
    assert is_valid("X") == True


def test_number_in_middle_but_expect_valid():
    assert is_valid("EF1KY") == True
    assert is_valid("CS50P") == True
"""
