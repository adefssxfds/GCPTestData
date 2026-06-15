import unittest


class Solution(object):
    def jump(self, nums):
        if len(nums) <= 1:
            return 0
        if nums[0] <= 0:
            return 0
        steps, currentEnd, farthest = 0, 0, 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == currentEnd:
                steps += 1
                currentEnd = farthest
                if currentEnd >= len(nums) - 1:
                    break
        return steps if farthest >= len(nums) - 1 else 0


class TestJumpGameII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # ---------- 题目示例 ----------
    def test_example1(self):
        nums = [2, 3, 1, 1, 4]
        self.assertEqual(self.sol.jump(nums), 2)  # 2 -> 3 -> 4

    def test_example2(self):
        nums = [2, 3, 0, 1, 4]
        self.assertEqual(self.sol.jump(nums), 2)  # 2 -> 3 -> 4

    # ---------- 边界情况 ----------
    def test_single_element(self):
        self.assertEqual(self.sol.jump([0]), 0)
        self.assertEqual(self.sol.jump([5]), 0)

    def test_two_elements_reachable(self):
        nums = [1, 0]
        self.assertEqual(self.sol.jump(nums), 1)  # 从0跳1步到1
        nums = [2, 0]
        self.assertEqual(
            self.sol.jump(nums), 1
        )  # 从0直接跳2步（实际只能到1）也只需要1步
        nums = [1, 1]
        self.assertEqual(self.sol.jump(nums), 1)  # 0->1

    def test_two_elements_unreachable(self):
        nums = [0, 1]
        self.assertEqual(self.sol.jump(nums), 0)  # 无法离开起点
        nums = [0, 0]
        self.assertEqual(self.sol.jump(nums), 0)

    # ---------- 逐渐增加跳跃 ----------
    def test_linear_sequence(self):
        nums = [1, 1, 1, 1, 1]
        self.assertEqual(self.sol.jump(nums), 4)  # 每次跳1步
        nums = [2, 2, 2, 2, 2]
        # 最优: 0->2->4，2步
        self.assertEqual(self.sol.jump(nums), 2)

    def test_big_jump_at_start(self):
        nums = [5, 1, 1, 1, 1]
        self.assertEqual(self.sol.jump(nums), 1)  # 直接从0跳到末尾
        nums = [5, 0, 0, 0, 0]
        self.assertEqual(self.sol.jump(nums), 1)

    def test_zero_in_middle(self):
        nums = [3, 2, 0, 1, 4]
        # 0->1->4 或 0->2? 0->2是到索引2值为0，不行；0->1=2，然后从1跳2步到3，再从3跳1步到4？实际最少2步：0->1->4
        self.assertEqual(self.sol.jump(nums), 2)
        nums = [3, 1, 0, 2, 4]
        # 0->1->3->4 需要3步？实际上0->3=2，从3跳2步到4？索引3的值为2，可以到4，所以0->3->4，2步
        self.assertEqual(self.sol.jump(nums), 2)

    def test_unreachable(self):
        nums = [1, 0, 2]
        self.assertEqual(self.sol.jump(nums), 0)  # 卡在索引1
        nums = [2, 0, 0, 1]
        self.assertEqual(self.sol.jump(nums), 0)  # 0->2后无法前进
        nums = [0]
        self.assertEqual(self.sol.jump(nums), 0)

    # ---------- 更大范围测试 ----------
    def test_always_reachable(self):
        # 题目保证可到达，但测试极端
        nums = [2, 1, 1, 1, 4]
        self.assertEqual(
            self.sol.jump(nums), 3
        )  # 0->1->2->3->4? 实际需要4步？0->2(索引2)，2->3，3->4，三步？0->2(2),2->3(1步),3->4(1步)，合计3步。检查：0:2, 2:1, 3:1, 4终点，共3步。正确。
        # 手动：0->2 (步数1), 2->3 (步数2), 3->4 (步数3) 到达

    # ---------- 随机测试与暴力DP对比（小规模）----------
    def test_random_compare_with_dp(self):
        """随机生成小数组，与动态规划结果对比"""
        import random

        def min_jumps_dp(nums):
            n = len(nums)
            dp = [float("inf")] * n
            dp[0] = 0
            for i in range(n):
                for j in range(1, nums[i] + 1):
                    if i + j < n:
                        dp[i + j] = min(dp[i + j], dp[i] + 1)
            return dp[n - 1] if dp[n - 1] != float("inf") else 0

        for _ in range(100):
            length = random.randint(1, 10)
            # 生成随机非负整数，确保可达性不好保证，但我们可以比较两者结果
            nums = [random.randint(0, length) for _ in range(length)]
            expected = min_jumps_dp(nums)
            result = self.sol.jump(nums)
            self.assertEqual(result, expected, f"Failed for {nums}")

    # ---------- 性能测试 ----------
    def test_performance_large(self):
        import time

        # 构造一个需要最优跳跃的大数组，长度10^4
        n = 10000
        nums = [1] * n  # 最坏情况，每次跳1步，需要n-1步
        start = time.time()
        result = self.sol.jump(nums)
        elapsed = time.time() - start
        self.assertEqual(result, n - 1)
        self.assertLess(elapsed, 1.0, f"Performance too slow: {elapsed:.2f}s")

        # 大跳跃情况
        nums = [n] + [0] * (n - 1)
        start = time.time()
        result = self.sol.jump(nums)
        elapsed = time.time() - start
        self.assertEqual(result, 1)
        self.assertLess(elapsed, 0.5)


if __name__ == "__main__":
    unittest.main()
