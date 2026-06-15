from distinct_subsequences import Solution

def test_numDistinct_with_common_subsequence():
    """Test with common subsequence present in s."""
    s = "abab"
    t = "ab"
    solution = Solution()
    assert solution.numDistinct(s, t) == 3

def test_numDistinct_without_subsequence():
    """Test with no subsequence present in s."""
    s = "abab"
    t = "ba"
    solution = Solution()
    assert solution.numDistinct(s, t) == 1

def test_numDistinct_with_empty_subsequence():
    """Test with empty subsequence t."""
    s = "abab"
    t = ""
    solution = Solution()
    assert solution.numDistinct(s, t) == 1

def test_numDistinct_with_longer_s():
    """Test with t longer than s."""
    s = "ab"
    t = "abab"
    solution = Solution()
    assert solution.numDistinct(s, t) == 0

def test_numDistinct_with_single_character_subsequence():
    """Test with single character subsequence in s."""
    s = "aabb"
    t = "b"
    solution = Solution()
    assert solution.numDistinct(s, t) == 2

def test_numDistinct_with_multiple_subsequences():
    """Test with multiple subsequences in s."""
    s = "aabb"
    t = "ba"
    solution = Solution()
    assert solution.numDistinct(s, t) == 0