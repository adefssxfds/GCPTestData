class Solution(object):
    def fourSum(self, nums, target):
        sumMapping = {}
        for index_i in range(len(nums)-1):
            for index_j in range(index_i+1, len(nums)):
                currSum = nums[index_i] + nums[index_j]
                if currSum in sumMapping:
                    sumMapping[currSum].append((index_i, index_j))
                else:
                    sumMapping[currSum] = [(index_i, index_j)]

        result = set()
        for key, value in sumMapping.items():
            diff = target - key
            if diff in sumMapping:
                firstSet = value
                secondSet = sumMapping[diff]

                for (i, j) in firstSet:
                    for (k, l) in secondSet:
                        fourlet = [i, j, k, l]
                        if len(set(fourlet)) != len(fourlet):
                            continue
                        fourlist = [nums[i], nums[j], nums[k], nums[l]]
                        fourlist.sort()
                        result.add(tuple(fourlist))

        return list(result)


import unittest

class TestFourSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # 示例 1
    def test_example1(self):
        nums = [1,0,-1,0,-2,2]
        target = 0
        expect = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        res = self.sol.fourSum(nums, target)
        # 排序后再断言，消除输出顺序影响
        self.assertEqual(sorted(res), sorted(expect))

    # 示例 2：全相同元素
    def test_example2(self):
        nums = [2,2,2,2,2]
        target = 8
        expect = [[2,2,2,2]]
        self.assertEqual(self.sol.fourSum(nums, target), expect)

    # 数组长度恰好为4，唯一解
    def test_exact_four(self):
        nums = [1,2,3,4]
        target = 10
        expect = [[1,2,3,4]]
        self.assertEqual(self.sol.fourSum(nums, target), expect)

    # 无解场景
    def test_no_answer(self):
        nums = [1,2,3,4,5]
        target = 100
        self.assertEqual(self.sol.fourSum(nums, target), [])

    # 含正负、多组重复四元组
    def test_mul_dup(self):
        nums = [-1,-2,0,0,1,2]
        target = 0
        expect = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        res = self.sol.fourSum(nums, target)
        self.assertEqual(sorted(res), sorted(expect))

if __name__ == '__main__':
    unittest.main()