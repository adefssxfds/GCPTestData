from interleaving_string_copy import Solution

def test_isInterleave_empty_s1_s2_s3():
    """Test with empty strings s1, s2, and s3"""
    solution = Solution()
    s1, s2, s3 = "", "", ""
    assert solution.isInterleave(s1, s2, s3) == True

def test_isInterleave_s1_s2_s3_with_only_s1():
    """Test with s3 formed only by s1"""
    solution = Solution()
    s1, s2, s3 = "abc", "", "abc"
    assert solution.isInterleave(s1, s2, s3) == True

def test_isInterleave_s1_s2_s3_with_only_s2():
    """Test with s3 formed only by s2"""
    solution = Solution()
    s1, s2, s3 = "", "abc", "abc"
    assert solution.isInterleave(s1, s2, s3) == True

def test_isInterleave_s1_s2_s3_with_both_s1_s2():
    """Test with s3 formed by interleaving s1 and s2"""
    solution = Solution()
    s1, s2, s3 = "abc", "def", "adbcef"
    assert solution.isInterleave(s1, s2, s3) == True

def test_isInterleave_s1_s2_s3_with_non_interleaving():
    """Test with s3 not formed by interleaving s1 and s2"""
    solution = Solution()
    s1, s2, s3 = "abc", "def", "abdef"
    assert solution.isInterleave(s1, s2, s3) == False

def test_isInterleave_s1_s2_s3_with_different_length():
    """Test with s3 length different from s1 + s2 length"""
    solution = Solution()
    s1, s2, s3 = "abc", "def", "abcdef"
    assert solution.isInterleave(s1, s2, s3) == False