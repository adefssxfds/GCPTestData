import unittest
from typing import Optional


# 链表节点定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 三种实现（复制自题目）
def add_two_numbers(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        digit = total % 10
        carry = total // 10
        current.next = ListNode(digit)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    return dummy_head.next


def add_two_numbers_recursive(
    l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0
) -> Optional[ListNode]:
    if not l1 and not l2 and carry == 0:
        return None
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    total = val1 + val2 + carry
    digit = total % 10
    new_carry = total // 10
    result = ListNode(digit)
    next_l1 = l1.next if l1 else None
    next_l2 = l2.next if l2 else None
    result.next = add_two_numbers_recursive(next_l1, next_l2, new_carry)
    return result


def add_two_numbers_optimized(
    l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    head = ListNode(0)
    current = head
    carry = 0
    while l1 or l2 or carry:
        sum_val = carry
        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next
        current.next = ListNode(sum_val % 10)
        current = current.next
        carry = sum_val // 10
    return head.next


# 辅助函数：将列表转换为链表
def list_to_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# 辅助函数：将链表转换为列表（用于比较）
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# 测试类
class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.algorithms = [
            ("迭代", add_two_numbers),
            ("递归", add_two_numbers_recursive),
            ("优化迭代", add_two_numbers_optimized),
        ]

    def test_example1(self):
        l1 = list_to_linked_list([2, 4, 3])
        l2 = list_to_linked_list([5, 6, 4])
        expected = [7, 0, 8]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(l1, l2)
                self.assertEqual(linked_list_to_list(result), expected)

    def test_example2(self):
        l1 = list_to_linked_list([0])
        l2 = list_to_linked_list([0])
        expected = [0]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(l1, l2)
                self.assertEqual(linked_list_to_list(result), expected)

    def test_example3(self):
        l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = list_to_linked_list([9, 9, 9, 9])
        expected = [8, 9, 9, 9, 0, 0, 0, 1]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(l1, l2)
                self.assertEqual(linked_list_to_list(result), expected)

    # 不同长度
    def test_different_lengths(self):
        l1 = list_to_linked_list([1, 8])
        l2 = list_to_linked_list([0])
        expected = [1, 8]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(l1, l2)
                self.assertEqual(linked_list_to_list(result), expected)

        l1 = list_to_linked_list([5])
        l2 = list_to_linked_list([5, 9, 9])
        expected = [0, 0, 0, 1]  # 5 + 995 = 1000 -> 反转 [0,0,0,1]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(l1, l2)
                self.assertEqual(linked_list_to_list(result), expected)

    # 进位传播
    def test_carry_propagation(self):
        l1 = list_to_linked_list([9, 9, 9])
        l2 = list_to_linked_list([1])
        expected = [0, 0, 0, 1]  # 999+1=1000
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(l1, l2)
                self.assertEqual(linked_list_to_list(result), expected)

    # 全零
    def test_all_zeros(self):
        l1 = list_to_linked_list([0, 0, 0])
        l2 = list_to_linked_list([0, 0])
        expected = [0, 0, 0]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                result = func(l1, l2)
                self.assertEqual(linked_list_to_list(result), expected)

    # 随机测试：对比三种实现结果一致，并与整数加法验证
    def test_random_consistency(self):
        import random

        for _ in range(100):
            # 随机生成长度 1~10 的链表
            len1 = random.randint(1, 10)
            len2 = random.randint(1, 10)
            arr1 = [random.randint(0, 9) for _ in range(len1)]
            arr2 = [random.randint(0, 9) for _ in range(len2)]
            l1 = list_to_linked_list(arr1)
            l2 = list_to_linked_list(arr2)
            # 计算整数和
            num1 = int("".join(map(str, arr1[::-1])))
            num2 = int("".join(map(str, arr2[::-1])))
            total = num1 + num2
            expected_arr = [int(d) for d in str(total)[::-1]]
            # 三种方法结果均应等于 expected_arr
            results = []
            for name, func in self.algorithms:
                result = func(l1, l2)
                result_arr = linked_list_to_list(result)
                self.assertEqual(
                    result_arr, expected_arr, f"{name} failed for {arr1} + {arr2}"
                )
                results.append(result_arr)
            # 额外验证结果一致（虽然上面已分别断言）
            self.assertTrue(all(r == results[0] for r in results))


if __name__ == "__main__":
    unittest.main()
