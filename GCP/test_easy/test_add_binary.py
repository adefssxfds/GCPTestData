from add_binary import Solution

def test_addBinary_example1():
    """Test case based on Example 1 from the requirement"""
    solution = Solution()
    assert solution.addBinary("11", "1") == "100"

def test_addBinary_example2():
    """Test case based on Example 2 from the requirement"""
    solution = Solution()
    assert solution.addBinary("1010", "1011") == "10101"

def test_addBinary_empty_string():
    """Test with empty string input"""
    solution = Solution()
    assert solution.addBinary("", "1") == "1"
    assert solution.addBinary("0", "") == "0"

def test_addBinary_same_length():
    """Test with same length input"""
    solution = Solution()
    assert solution.addBinary("11", "10") == "101"

def test_addBinary_different_length():
    """Test with different length input"""
    solution = Solution()
    assert solution.addBinary("1", "11") == "100"

def test_addBinary_all_zeros():
    """Test with all zeros input"""
    solution = Solution()
    assert solution.addBinary("0", "0") == "0"

def test_addBinary_all_ones():
    """Test with all ones input"""
    solution = Solution()
    assert solution.addBinary("1", "1") == "10"