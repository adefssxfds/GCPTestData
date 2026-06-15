from letter_combinations_phone_number import Solution

def test_letter_combinations_empty_digits():
    """Test with empty digits input."""
    solution = Solution()
    assert solution.letterCombinations("") == []

def test_letter_combinations_single_digit():
    """Test with a single digit input."""
    solution = Solution()
    assert solution.letterCombinations("2") == ["a", "b", "c"]

def test_letter_combinations_multiple_digits():
    """Test with multiple digits input."""
    solution = Solution()
    assert solution.letterCombinations("23") == ["d", "e", "f"]