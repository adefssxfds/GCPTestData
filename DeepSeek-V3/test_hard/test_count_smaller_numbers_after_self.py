import unittest
from typing import List


# ---------- 原题提供的 Solution 类（BST 解法） ----------
class TreeNode(object):
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val
        self.count = 1  # 以当前节点为根的子树中的节点总数（包括自身和左子树）


class Solution(object):
    def countSmaller(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        node = TreeNode(nums[-1])
        result = [0]  # 最后一个元素右侧没有元素，计数为 0
        for index in range(len(nums) - 2, -1, -1):
            result.append(self.insertNode(node, nums[index]))
        return result[::-1]  # 逆序后即为从左到右的结果

    def insertNode(self, node: TreeNode, val: int) -> int:
        """将 val 插入 BST，并返回树中小于 val 的节点个数（即右侧比 val 小的个数）"""
        totalCount = 0
        while True:
            if val <= node.val:
                node.count += 1
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
            else:
                totalCount += node.count  # 当前节点及其左子树全部小于 val
                if node.right is None:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
        return totalCount


# ---------- 暴力解法（用于对比验证） ----------
def brute_force_count_smaller(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [0] * n
    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                count += 1
        result[i] = count
    return result


# ---------- 测试类 ----------
class TestCountSmaller(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example1(self):
        """示例1: [5,2,6,1] -> [2,1,1,0]"""
        nums = [5, 2, 6, 1]
        expected = [2, 1, 1, 0]
        self.assertEqual(self.sol.countSmaller(nums), expected)

    def test_example2(self):
        """示例2: [-1] -> [0]"""
        nums = [-1]
        expected = [0]
        self.assertEqual(self.sol.countSmaller(nums), expected)

    def test_example3(self):
        """示例3: [-1,-1] -> [0,0]"""
        nums = [-1, -1]
        expected = [0, 0]
        self.assertEqual(self.sol.countSmaller(nums), expected)

    def test_empty_array(self):
        """空数组: [] -> []"""
        nums = []
        expected = []
        self.assertEqual(self.sol.countSmaller(nums), expected)

    def test_increasing_sequence(self):
        """递增序列: [1,2,3,4] -> [0,0,0,0]"""
        nums = [1, 2, 3, 4]
        expected = [0, 0, 0, 0]
        self.assertEqual(self.sol.countSmaller(nums), expected)

    def test_decreasing_sequence(self):
        """递减序列: [4,3,2,1] -> [3,2,1,0]"""
        nums = [4, 3, 2, 1]
        expected = [3, 2, 1, 0]
        self.assertEqual(self.sol.countSmaller(nums), expected)

    def test_duplicate_values(self):
        """包含重复值: [2,2,2,2] -> [0,0,0,0]"""
        nums = [2, 2, 2, 2]
        expected = [0, 0, 0, 0]
        self.assertEqual(self.sol.countSmaller(nums), expected)

    def test_mixed_positive_negative(self):
        """混合正负数: [5,-1,3,0,2] -> 手动计算验证"""
        nums = [5, -1, 3, 0, 2]
        # 5右边比5小的: -1,3,0,2 -> 4个（全部）
        # -1右边比-1小的: 没有（0,2,3都大于-1）-> 0
        # 3右边比3小的: 0,2 -> 2个
        # 0右边比0小的: 没有 -> 0
        # 2右边比2小的: 没有 -> 0
        expected = [4, 0, 2, 0, 0]
        self.assertEqual(self.sol.countSmaller(nums), expected)

    def test_all_same_negative(self):
        """全相同负数: [-5,-5,-5] -> [0,0,0]"""
        nums = [-5, -5, -5]
        expected = [0, 0, 0]
        self.assertEqual(self.sol.countSmaller(nums), expected)

    def test_single_element_with_zero(self):
        """单元素0: [0] -> [0]"""
        nums = [0]
        expected = [0]
        self.assertEqual(self.sol.countSmaller(nums), expected)

    def test_large_numbers(self):
        """大数值: [1000, 500, 1500, 0] -> [2,1,1,0]"""
        nums = [1000, 500, 1500, 0]
        # 1000右边比1000小的: 500,0 -> 2
        # 500右边比500小的: 0 -> 1
        # 1500右边比1500小的: 0 -> 1
        # 0右边比0小的: 无 -> 0
        expected = [2, 1, 1, 0]
        self.assertEqual(self.sol.countSmaller(nums), expected)

    def test_random_vs_bruteforce(self):
        """随机生成数组，对比 BST 解法与暴力法的结果（保证正确性）"""
        import random

        for _ in range(100):
            length = random.randint(1, 50)
            nums = [random.randint(-100, 100) for _ in range(length)]
            expected = brute_force_count_smaller(nums)
            self.assertEqual(
                self.sol.countSmaller(nums), expected, f"Failed for {nums}"
            )

    def test_performance_large_input(self):
        """性能测试：长度 30000 的随机数组，应在合理时间内完成"""
        import random
        import time

        nums = [random.randint(-1000, 1000) for _ in range(30000)]
        start_time = time.time()
        result = self.sol.countSmaller(nums)
        elapsed = time.time() - start_time
        # 确保计算完成且结果长度正确
        self.assertEqual(len(result), len(nums))
        self.assertLess(elapsed, 5.0, f"BST took {elapsed:.2f}s, too slow")
        # 简单检查结果是否合理（非严格，仅作验证）
        for i in range(len(nums)):
            # 结果必须 <= 右侧元素数量
            self.assertLessEqual(result[i], len(nums) - i - 1)


if __name__ == "__main__":
    unittest.main()
