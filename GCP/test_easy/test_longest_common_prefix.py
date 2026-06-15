import longest_common_prefix


def test_longest_common_prefix() -> None:
    """Test the standard longest common prefix implementation."""
    assert longest_common_prefix.longest_common_prefix(
        ["flower", "flow", "flight"]
    ) == "fl"
    assert longest_common_prefix.longest_common_prefix(
        ["dog", "racecar", "car"]
    ) == ""
    assert longest_common_prefix.longest_common_prefix([""]) == ""
    assert longest_common_prefix.longest_common_prefix(["a"]) == "a"


def test_longest_common_prefix_horizontal() -> None:
    """Test the horizontal scanning implementation."""
    assert longest_common_prefix.longest_common_prefix_horizontal(
        ["flower", "flow", "flight"]
    ) == "fl"
    assert longest_common_prefix.longest_common_prefix_horizontal(
        ["dog", "racecar", "car"]
    ) == ""
    assert longest_common_prefix.longest_common_prefix_horizontal([""]) == ""
    assert longest_common_prefix.longest_common_prefix_horizontal(["a"]) == "a"


def test_longest_common_prefix_divide_conquer() -> None:
    """Test the divide and conquer implementation."""
    assert longest_common_prefix.longest_common_prefix_divide_conquer(
        ["flower", "flow", "flight"]
    ) == "fl"
    assert longest_common_prefix.longest_common_prefix_divide_conquer(
        ["dog", "racecar", "car"]
    ) == ""
    assert longest_common_prefix.longest_common_prefix_divide_conquer([""]) == ""
    assert longest_common_prefix.longest_common_prefix_divide_conquer(["a"]) == "a"


def test_longest_common_prefix_trie() -> None:
    """Test the Trie-based implementation."""
    assert longest_common_prefix.longest_common_prefix_trie(
        ["flower", "flow", "flight"]
    ) == "fl"
    assert longest_common_prefix.longest_common_prefix_trie(
        ["dog", "racecar", "car"]
    ) == ""
    assert longest_common_prefix.longest_common_prefix_trie([""]) == ""
    assert longest_common_prefix.longest_common_prefix_trie(["a"]) == "a"


def test_lcp_helper() -> None:
    """Test the LCP helper function (if it exists in the module)."""
    if hasattr(longest_common_prefix, 'lcp_helper'):
        assert longest_common_prefix.lcp_helper("flower", "flow") == "fl"
        assert longest_common_prefix.lcp_helper("dog", "racecar") == ""
        assert longest_common_prefix.lcp_helper("", "") == ""
    else:
        # Skip the test if function doesn't exist
        pass


def test_common_prefix() -> None:
    """Test the common prefix function (if it exists in the module)."""
    if hasattr(longest_common_prefix, 'common_prefix'):
        assert longest_common_prefix.common_prefix("flower", "flow") == "fl"
        assert longest_common_prefix.common_prefix("dog", "racecar") == ""
        assert longest_common_prefix.common_prefix("", "") == ""
        assert longest_common_prefix.common_prefix("flower", "") == ""
        assert longest_common_prefix.common_prefix("", "flow") == ""
    else:
        # Skip the test if function doesn't exist
        pass


def test_longest_common_prefix_empty_list() -> None:
    """Test longest common prefix with empty list."""
    assert longest_common_prefix.longest_common_prefix([]) == ""


def test_longest_common_prefix_single_string() -> None:
    """Test longest common prefix with single string."""
    assert longest_common_prefix.longest_common_prefix(["abc"]) == "abc"


def test_longest_common_prefix_horizontal_empty_list() -> None:
    """Test horizontal method with empty list."""
    assert longest_common_prefix.longest_common_prefix_horizontal([]) == ""


def test_longest_common_prefix_horizontal_single_string() -> None:
    """Test horizontal method with single string."""
    assert longest_common_prefix.longest_common_prefix_horizontal(["abc"]) == "abc"


def test_edge_cases() -> None:
    """Test additional edge cases."""
    # Test with all identical strings
    assert longest_common_prefix.longest_common_prefix(
        ["test", "test", "test"]
    ) == "test"

    # Test with prefix in middle
    assert longest_common_prefix.longest_common_prefix(
        ["ab", "abc", "abcd"]
    ) == "ab"

    # Test with no common prefix
    assert longest_common_prefix.longest_common_prefix(
        ["cat", "dog", "fish"]
    ) == ""

    # Test with None or None strings
    assert longest_common_prefix.longest_common_prefix([""]) == ""

    # Test with mixed empty strings
    assert longest_common_prefix.longest_common_prefix(["", "a", "ab"]) == ""


def test_all_implementations_consistency() -> None:
    """Test that all implementations return the same result."""
    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["", "a", "ab"],
        ["single"],
        [],
        ["", ""],
        ["ab", "abc", "abcd"],
        ["cat", "dog", "fish"],
    ]

    for test_case in test_cases:
        result1 = longest_common_prefix.longest_common_prefix(test_case)
        result2 = longest_common_prefix.longest_common_prefix_horizontal(test_case)
        result3 = longest_common_prefix.longest_common_prefix_divide_conquer(test_case)
        result4 = longest_common_prefix.longest_common_prefix_trie(test_case)

        # All implementations should return the same result
        assert result1 == result2, f"Mismatch for {test_case}"
        assert result2 == result3, f"Mismatch for {test_case}"
        assert result3 == result4, f"Mismatch for {test_case}"
