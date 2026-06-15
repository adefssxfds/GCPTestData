from longest_substring_without_repeating import length_of_longest_substring, length_of_longest_substring_set

def test_length_of_longest_substring_example_1():
    assert length_of_longest_substring("abcabcbb") == 3

def test_length_of_longest_substring_example_2():
    assert length_of_longest_substring("bbbbb") == 1

def test_length_of_longest_substring_example_3():
    assert length_of_longest_substring("pwwkew") == 3

def test_length_of_longest_substring_empty_string():
    assert length_of_longest_substring("") == 0

def test_length_of_longest_substring_all_repeating():
    assert length_of_longest_substring("aaaaaa") == 1

def test_length_of_longest_substring_mixed_characters():
    assert length_of_longest_substring("aAbBcC1234") == 10

def test_length_of_longest_substring_set_example_1():
    assert length_of_longest_substring_set("abcabcbb") == 3

def test_length_of_longest_substring_set_example_2():
    assert length_of_longest_substring_set("bbbbb") == 1

def test_length_of_longest_substring_set_example_3():
    assert length_of_longest_substring_set("pwwkew") == 3

def test_length_of_longest_substring_set_empty_string():
    assert length_of_longest_substring_set("") == 0

def test_length_of_longest_substring_set_all_repeating():
    assert length_of_longest_substring_set("aaaaaa") == 1

def test_length_of_longest_substring_set_mixed_characters():
    assert length_of_longest_substring_set("aAbBcC1234") == 10