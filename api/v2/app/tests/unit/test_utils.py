from app.utils import generate_key


def test_generate_key():
    """
    Given an input string,
    When the generate key function is called,
    Then it returns the sha1
    """
    str_input = 'foo'
    key = generate_key(str_input)
    assert len(key) == 40
    assert str_input not in key


def test_generate_key_strips_and_lowercases():
    """
    Given strings with different capitalizations,
    When the key is generated,
    Then the keys are the same
    """
    str_input_1 = 'foo'
    str_input_2 = 'fOo'
    str_input_3 = ' FOo '
    key_1 = generate_key(str_input_1)
    key_2 = generate_key(str_input_2)
    key_3 = generate_key(str_input_3)
    assert key_1 == key_2
    assert key_2 == key_3
