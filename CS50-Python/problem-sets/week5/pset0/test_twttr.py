from twttr import shorten

def test_lowercase_vowels():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_uppercase_vowels():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("INSTAGRAM") == "NSTGRM"
    
def test_punctuation_more():
    assert shorten("!!!") == "!!!"
    assert shorten(".,?!") == ".,?!"
    assert shorten("a!e?i.") == "!?."
    
def test_mixed_case():
    assert shorten("HELLO This is a Short VERSION OF Twitter") == "HLL Ths s  Shrt VRSN F Twttr"
    
def test_numbers():
    assert shorten("CS50") == "CS50"