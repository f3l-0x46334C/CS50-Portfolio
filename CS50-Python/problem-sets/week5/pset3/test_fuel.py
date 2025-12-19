from fuel import convert, gauge

# ---------- convert ----------

def test_convert_correct():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/1") == 0


def test_convert_value_error():
    try:
        convert("3/2")
        assert False
    except ValueError:
        pass


def test_convert_negative():
    try:
        convert("-1/2")
        assert False
    except ValueError:
        pass


def test_convert_zero_division():
    try:
        convert("1/0")
        assert False
    except ZeroDivisionError:
        pass


# ---------- gauge ----------

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
