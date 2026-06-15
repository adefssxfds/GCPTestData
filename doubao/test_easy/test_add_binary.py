class Solution(object):
    def addBinary(self, a, b):
        result = ""

        carry = 0
        index_a, index_b = len(a) - 1, len(b) - 1
        while index_a >= 0 and index_b >= 0:
            result = str((int(a[index_a]) + int(b[index_b]) + carry) % 2) + result
            carry = (int(a[index_a]) + int(b[index_b]) + carry) // 2
            index_a -= 1
            index_b -= 1

        if index_a >= 0:
            while index_a >= 0:
                result = str((int(a[index_a]) + carry) % 2) + result
                carry = (int(a[index_a]) + carry) // 2
                index_a -= 1
        elif index_b >= 0:
            while index_b >= 0:
                result = str((int(b[index_b]) + carry) % 2) + result
                carry = (int(b[index_b]) + carry) // 2
                index_b -= 1

        if carry == 1:
            result = str(carry) + result
        return result


# 生成测试代码
if __name__ == "__main__":
    # 创建解决方案实例
    sol = Solution()

    # 测试用例列表：(a, b, 预期输出)
    test_cases = [
        # 题目官方示例
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        # 边界测试用例
        ("0", "0", "0"),  # 两个0相加
        ("0", "1", "1"),  # 0和1相加
        ("1", "1", "10"),  # 1和1相加（产生进位）
        ("1111", "1", "10000"),  # 连续进位
        ("111", "111", "1110"),  # 等长字符串相加
        ("1000", "10", "1010"),  # 长度不同的字符串相加
    ]

    # 遍历执行所有测试
    print("开始执行二进制加法测试...\n")
    for i, (a, b, expected) in enumerate(test_cases, 1):
        output = sol.addBinary(a, b)
        # 判定测试结果
        status = "通过" if output == expected else "失败"
        print(f"测试用例 {i}:")
        print(f"  输入: a = {a}, b = {b}")
        print(f"  输出: {output}")
        print(f"  预期: {expected}")
        print(f"  状态: {status}\n")

    print("所有测试执行完毕！")
