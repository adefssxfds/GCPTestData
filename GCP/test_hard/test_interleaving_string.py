from interleaving_string import Solution

def test_isInterleave_empty():
    """Test with empty strings s1, s2, s3."""
    solution = Solution()
    s1, s2, s3 = "", "", ""
    assert solution.isInterleave(s1, s2, s3) == True

def test_isInterleave_same_length():
    """Test with equal length strings s1, s2, s3."""
    solution = Solution()
    s1, s2, s3 = "abc", "def", "abcdef"
    assert solution.isInterleave(s1, s2, s3) == True

def test_isInterleave_different_length():
    """Test with different length strings s1, s2, s3."""
    solution = Solution()
    s1, s2, s3 = "abc", "def", "defabc"
    assert solution.isInterleave(s1, s2, s3) == True

def test_isInterleave_not_interleaved():
    """Test with s3 not formed by interleaving s1 and s2."""
    solution = Solution()
    s1, s2, s3 = "abc", "def", "abcdefg"
    assert solution.isInterleave(s1, s2, s3) == False

def test_isInterleave_reverse_interleaving():
    """Test with s3 formed by reverse interleaving s1 and s2."""
    solution = Solution()
    s1, s2, s3 = "abc", "def", "defcba"
    assert solution.isInterleave(s1, s2, s3) == True

def test_isInterleave_both_reversed():
    """Test with s3 formed by both s1 and s2 reversed."""
    solution = Solution()
    s1, s2, s3 = "abc", "def", "fedcba"
    assert solution.isInterleave(s1, s2, s3) == False