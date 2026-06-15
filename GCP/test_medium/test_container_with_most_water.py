from container_with_most_water import max_area, max_area_brute_force, max_area_optimized

def test_max_area():
    """Test max_area function with example 1 input"""
    height = [1,8,6,2,5,4,8,3,7]
    expected = 49
    assert max_area(height) == expected

def test_max_area_brute_force():
    """Test max_area_brute_force function with example 1 input"""
    height = [1,8,6,2,5,4,8,3,7]
    expected = 49
    assert max_area_brute_force(height) == expected

def test_max_area_optimized():
    """Test max_area_optimized function with example 1 input"""
    height = [1,8,6,2,5,4,8,3,7]
    expected = 49
    assert max_area_optimized(height) == expected

def test_max_area_empty_list():
    """Test max_area function with empty list"""
    height = []
    expected = 0
    assert max_area(height) == expected

def test_max_area_brute_force_empty_list():
    """Test max_area_brute_force function with empty list"""
    height = []
    expected = 0
    assert max_area_brute_force(height) == expected

def test_max_area_optimized_empty_list():
    """Test max_area_optimized function with empty list"""
    height = []
    expected = 0
    assert max_area_optimized(height) == expected

def test_max_area_single_element():
    """Test max_area function with single element list"""
    height = [1]
    expected = 0
    assert max_area(height) == expected

def test_max_area_brute_force_single_element():
    """Test max_area_brute_force function with single element list"""
    height = [1]
    expected = 0
    assert max_area_brute_force(height) == expected

def test_max_area_optimized_single_element():
    """Test max_area_optimized function with single element list"""
    height = [1]
    expected = 0
    assert max_area_optimized(height) == expected