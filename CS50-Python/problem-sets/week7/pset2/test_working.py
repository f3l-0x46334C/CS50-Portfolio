import pytest
from working import convert


def test_convert_basic():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"


def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")

    with pytest.raises(ValueError):
        convert("09 AM to 5 PM")

    with pytest.raises(ValueError):
        convert("9:99 AM to 5 PM")
