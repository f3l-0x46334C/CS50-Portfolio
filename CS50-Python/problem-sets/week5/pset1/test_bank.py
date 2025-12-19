from bank import value

def test_hello_exact():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO there") == 0

def test_h_not_hello():
    assert value("hi") == 20
    assert value("Howdy") == 20
    assert value("hmmmm") == 20
    assert value("hELLOO") == 0
    assert value("hey") == 20
    assert value("hola") == 20

def test_other_greetings():
    assert value("good morning") == 100
    assert value("bonjour") == 100
