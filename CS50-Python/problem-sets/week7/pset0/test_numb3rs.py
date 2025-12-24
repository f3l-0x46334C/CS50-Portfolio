from numb3rs import validate


def test_valid_ips():
    valid_ips = [
        "0.0.0.0",
        "127.0.0.1",
        "192.168.1.1",
        "255.255.255.255",
        "10.20.30.40",
    ]
    for ip in valid_ips:
        assert validate(ip), f"Valid IP failed: {ip}"


def test_invalid_ips_short_or_long():
    invalid_ips = ["192.168.1", "192.168.1.1.1"]
    for ip in invalid_ips:
        assert not validate(ip), f"Invalid IP passed: {ip}"


def test_invalid_ips_leading_zero():
    invalid_ips = ["192.168.01.1", "10.020.30.40"]
    for ip in invalid_ips:
        assert not validate(ip), f"Invalid IP passed: {ip}"


def test_invalid_ips():
    invalid_ips = ["1a2.1b8.0c.1", "0.0.00.00", "a.b.c.d", "123@34.2!10"]
    for ip in invalid_ips:
        assert not validate(ip), f"Invalid IP passed: {ip}"
