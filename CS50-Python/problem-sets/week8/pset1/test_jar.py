import pytest
from jar import Jar


def test_init():
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0
    assert jar.is_empty() is True
    assert jar.is_full() is False
    
    # default value
    default_jar = Jar()
    assert default_jar.capacity == 12
    assert default_jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    # depositing negative number should raise ValueError
    with pytest.raises(ValueError):
        jar.deposit(-1)

    # depositing more than capacity should raise ValueError
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2

    # withdrawing negative number should raise ValueError
    with pytest.raises(ValueError):
        jar.withdraw(-1)

    # withdrawing more than current size should raise ValueError
    with pytest.raises(ValueError):
        jar.withdraw(10)


def test_reset():
    jar = Jar(5)
    jar.deposit(3)
    jar.reset("yes")
    assert jar.size == 0

    jar.deposit(2)
    jar.reset("no")
    assert jar.size == 2


def test_is_empty_and_is_full():
    jar = Jar(2)
    assert jar.is_empty() is True
    assert jar.is_full() is False

    jar.deposit(2)
    assert jar.is_empty() is False
    assert jar.is_full() is True
