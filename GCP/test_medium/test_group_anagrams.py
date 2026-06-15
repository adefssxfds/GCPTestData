from group_anagrams import group_anagrams, group_anagrams_counting, group_anagrams_prime

# Test for group_anagrams function
def test_group_anagrams_example1():
    """Test group_anagrams with example 1 input."""
    input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert group_anagrams(input_data) == expected_output

def test_group_anagrams_empty_string():
    """Test group_anagrams with empty string input."""
    input_data = [""]
    expected_output = [[""]]
    assert group_anagrams(input_data) == expected_output

def test_group_anagrams_single_character():
    """Test group_anagrams with single character input."""
    input_data = ["a"]
    expected_output = [["a"]]
    assert group_anagrams(input_data) == expected_output

# Test for group_anagrams_counting function
def test_group_anagrams_counting_example1():
    """Test group_anagrams_counting with example 1 input."""
    input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert group_anagrams_counting(input_data) == expected_output

def test_group_anagrams_counting_empty_string():
    """Test group_anagrams_counting with empty string input."""
    input_data = [""]
    expected_output = [[""]]
    assert group_anagrams_counting(input_data) == expected_output

def test_group_anagrams_counting_single_character():
    """Test group_anagrams_counting with single character input."""
    input_data = ["a"]
    expected_output = [["a"]]
    assert group_anagrams_counting(input_data) == expected_output

# Test for group_anagrams_prime function
def test_group_anagrams_prime_example1():
    """Test group_anagrams_prime with example 1 input."""
    input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert group_anagrams_prime(input_data) == expected_output

def test_group_anagrams_prime_empty_string():
    """Test group_anagrams_prime with empty string input."""
    input_data = [""]
    expected_output = [[""]]
    assert group_anagrams_prime(input_data) == expected_output

def test_group_anagrams_prime_single_character():
    """Test group_anagrams_prime with single character input."""
    input_data = ["a"]
    expected_output = [["a"]]
    assert group_anagrams_prime(input_data) == expected_output