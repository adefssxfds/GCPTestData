from maximum_subarray import (max_sub_array, max_sub_array_divide_conquer,
                             max_sub_array_with_indices)


# 测试 max_sub_array 函数
def test_max_sub_array_example1():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_sub_array(nums) == 6


def test_max_sub_array_example2():
    nums = [1]
    assert max_sub_array(nums) == 1


def test_max_sub_array_example3():
    nums = [5, 4, -1, 7, 8]
    assert max_sub_array(nums) == 23


def test_max_sub_array_empty():
    nums = []
    assert max_sub_array(nums) == 0


def test_max_sub_array_all_negative():
    nums = [-1, -2, -3, -4]
    assert max_sub_array(nums) == -1


# 测试 max_sub_array_divide_conquer 函数
def test_max_sub_array_divide_conquer_example1():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_sub_array_divide_conquer(nums) == 6


def test_max_sub_array_divide_conquer_example2():
    nums = [1]
    assert max_sub_array_divide_conquer(nums) == 1


def test_max_sub_array_divide_conquer_example3():
    nums = [5, 4, -1, 7, 8]
    assert max_sub_array_divide_conquer(nums) == 23


def test_max_sub_array_divide_conquer_empty():
    nums = []
    assert max_sub_array_divide_conquer(nums) == 0


def test_max_sub_array_divide_conquer_all_negative():
    nums = [-1, -2, -3, -4]
    assert max_sub_array_divide_conquer(nums) == -1


# 测试 max_sub_array_with_indices 函数
def test_max_sub_array_with_indices_example1():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_sub_array_with_indices(nums) == (6, 3, 6)


def test_max_sub_array_with_indices_example2():
    nums = [1]
    assert max_sub_array_with_indices(nums) == (1, 0, 0)


def test_max_sub_array_with_indices_example3():
    nums = [5, 4, -1, 7, 8]
    assert max_sub_array_with_indices(nums) == (23, 0, 4)


def test_max_sub_array_with_indices_empty():
    nums = []
    assert max_sub_array_with_indices(nums) == (0, -1, -1)


def test_max_sub_array_with_indices_all_negative():
    nums = [-1, -2, -3, -4]
    # 注意：这里测试代码预期的结果是 (3, 3, 3)，但实际应该是 (-1, 0, 0)
    # 因为当所有数都是负数时，最大子数组是第一个元素
    assert max_sub_array_with_indices(nums) == (-1, 0, 0)


# ===== 补充测试（迭代优化） =====
def test_max_sub_array_example4():
    assert max_sub_array([-2, -3, 4, -1, -2, 1, 5, -3]) == 7, "Test case 1 failed"


def test_max_sub_array_example5():
    assert max_sub_array([1, -1, -1, 2, 1, -1, 1, 1, -1, -2]) == 3, "Test case 2 failed"


def test_max_sub_array_example6():
    assert max_sub_array([-1, -2, -3, -4, -5]) == -1, "Test case 3 failed"


# 测试 max_sub_array_divide_conquer
def test_max_sub_array_divide_conquer_example4():
    assert max_sub_array_divide_conquer([-2, -3, 4, -1, -2, 1, 5, -3]) == 7, "Test case 1 failed"


def test_max_sub_array_divide_conquer_example5():
    assert max_sub_array_divide_conquer([1, -1, -1, 2, 1, -1, 1, 1, -1, -2]) == 3, "Test case 2 failed"


def test_max_sub_array_divide_conquer_example6():
    assert max_sub_array_divide_conquer([-1, -2, -3, -4, -5]) == -1, "Test case 3 failed"


# 测试 max_sub_array_with_indices
def test_max_sub_array_with_indices_example4():
    assert max_sub_array_with_indices([-2, -3, 4, -1, -2, 1, 5, -3]) == (7, 2, 6), "Test case 1 failed"


def test_max_sub_array_with_indices_example5():
    assert max_sub_array_with_indices([1, -1, -1, 2, 1, -1, 1, 1, -1, -2]) == (3, 3, 7), "Test case 2 failed"


def test_max_sub_array_with_indices_example6():
    assert max_sub_array_with_indices([-1, -2, -3, -4, -5]) == (-1, 0, 0), "Test case 3 failed"

