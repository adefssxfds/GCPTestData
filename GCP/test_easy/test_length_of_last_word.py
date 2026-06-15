from length_of_last_word import length_of_last_word, length_of_last_word_split

def test_length_of_last_word_example1():
    """Test the length of the last word in 'Hello World' is 5."""
    assert length_of_last_word("Hello World") == 5

def test_length_of_last_word_example2():
    """Test the length of the last word in '   fly me   to   the moon  ' is 4."""
    assert length_of_last_word("   fly me   to   the moon  ") == 4

def test_length_of_last_word_example3():
    """Test the length of the last word in 'luffy is still joyboy' is 6."""
    assert length_of_last_word("luffy is still joyboy") == 6

def test_length_of_last_word_empty_string():
    """Test the length of the last word in an empty string is 0."""
    assert length_of_last_word("") == 0

def test_length_of_last_word_only_spaces():
    """Test the length of the last word in a string with only spaces is 0."""
    assert length_of_last_word("     ") == 0

def test_length_of_last_word_split_example1():
    """Test the length of the last word in 'Hello World' is 5 using split method."""
    assert length_of_last_word_split("Hello World") == 5

def test_length_of_last_word_split_example2():
    """Test the length of the last word in '   fly me   to   the moon  ' is 4 using split method."""
    assert length_of_last_word_split("   fly me   to   the moon  ") == 4

def test_length_of_last_word_split_example3():
    """Test the length of the last word in 'luffy is still joyboy' is 6 using split method."""
    assert length_of_last_word_split("luffy is still joyboy") == 6

def test_length_of_last_word_split_empty_string():
    """Test the length of the last word in an empty string is 0 using split method."""
    assert length_of_last_word_split("") == 0

def test_length_of_last_word_split_only_spaces():
    """Test the length of the last word in a string with only spaces is 0 using split method."""
    assert length_of_last_word_split("     ") == 0