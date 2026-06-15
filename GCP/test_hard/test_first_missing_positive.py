from first_missing_positive import Solution

# Test cases for firstMissingPositive
def test_firstMissingPositive_empty():
    """Test with empty list."""
    solution = Solution()
    assert solution.firstMissingPositive([]) == 1

def test_firstMissingPositive_all_negatives():
    """Test with all negative numbers."""
    solution = Solution()
    assert solution.firstMissingPositive([-1, -2, -3]) == 4

def test_firstMissingPositive_missing_positive():
    """Test with missing positive number."""
    solution = Solution()
    assert solution.firstMissingPositive([1, 2, 4]) == 3

def test_firstMissingPositive_all_positive():
    """Test with all positive numbers and no missing number."""
    solution = Solution()
    assert solution.firstMissingPositive([1, 2, 3, 4, 5]) == 6

def test_firstMissingPositive_all_duplicates():
    """Test with all duplicate numbers."""
    solution = Solution()
    assert solution.firstMissingPositive([1, 1, 1, 2, 2, 3]) == 4

# Test cases for all public methods of the Solution class
# Assuming the class has only one method, firstMissingPositive
# Here we test the same cases as above
def test_solution_all_methods():
    """Test all methods of the Solution class."""
    test_firstMissingPositive_empty()
    test_firstMissingPositive_all_negatives()
    test_firstMissingPositive_missing_positive()
    test_firstMissingPositive_all_positive()
    test_firstMissingPositive_all_duplicates()