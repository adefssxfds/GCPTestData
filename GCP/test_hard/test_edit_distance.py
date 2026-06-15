from edit_distance import Solution

def test_minDistance_single_insert():
    """测试插入操作的情况，例如 'abc' 到 'ab'"""
    solution = Solution()
    assert solution.minDistance("abc", "ab") == 1

def test_minDistance_single_delete():
    """测试删除操作的情况，例如 'abc' 到 'ac'"""
    solution = Solution()
    assert solution.minDistance("abc", "ac") == 1

def test_minDistance_single_replace():
    """测试替换操作的情况，例如 'abc' 到 'acc'"""
    solution = Solution()
    assert solution.minDistance("abc", "acc") == 1

def test_minDistance_multiple_operations():
    """测试需要多个操作的情况，例如 'abc' 到 'acc'"""
    solution = Solution()
    assert solution.minDistance("abc", "acc") == 1

def test_minDistance_empty_to_non_empty():
    """测试从空字符串到非空字符串的情况，例如 '' 到 'a'"""
    solution = Solution()
    assert solution.minDistance("", "a") == 1

def test_minDistance_non_empty_to_empty():
    """测试从非空字符串到空字符串的情况，例如 'a' 到 ''"""
    solution = Solution()
    assert solution.minDistance("a", "") == 1

def test_minDistance_same_strings():
    """测试两个相同字符串的情况，例如 'abc' 到 'abc'"""
    solution = Solution()
    assert solution.minDistance("abc", "abc") == 0

def test_minDistance_long_to_short():
    """测试长字符串到短字符串的情况，例如 'abcde' 到 'ab'"""
    solution = Solution()
    assert solution.minDistance("abcde", "ab") == 3

def test_minDistance_short_to_long():
    """测试短字符串到长字符串的情况，例如 'ab' 到 'abcde'"""
    solution = Solution()
    assert solution.minDistance("ab", "abcde") == 3

def test_minDistance_mixed_operations():
    """测试需要混合操作的情况，例如 'abc' 到 'abcd'"""
    solution = Solution()
    assert solution.minDistance("abc", "abcd") == 1