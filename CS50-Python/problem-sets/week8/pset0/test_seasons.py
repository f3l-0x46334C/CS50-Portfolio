import pytest
from seasons import calc_days, convert, remove_and, input_validation

def test_input_validation_valid():
    valid_date = ["1990-10-05","2000-01-01","2020-01-15","2025-01-01"]
    for date in valid_date:
        input_validation(date)

def test_input_validation_invalid():
    invalid_date = "1800-13-32"
    with pytest.raises(SystemExit):
        input_validation(invalid_date)

def test_calc_days_known():
    birth = "2000-01-01"
    days = calc_days(birth)
    assert days > 0

def test_convert_minutes():
    assert convert(1) == 24 * 60
    assert convert(0) == 0
    assert convert(2) == 2 * 24 * 60
