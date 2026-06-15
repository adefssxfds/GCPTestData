import unittest
from typing import Optional, List, Any


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# --- 将你的三个算法放在这里 ---
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


# --- 辅助工具函数 ---
def build_linked_list(values: List[Any]) -> Optional[ListNode]:
    """通过列表构建链表"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """将链表序列化为列表"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# --- 测试代码 ---
class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        # 统一管理三种求解算法
        self.add_funcs = [
            add_two_numbers,
            add_two_numbers_recursive,
            add_two_numbers_optimized,
        ]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ([2, 4, 3], [5, 6, 4], [7, 0, 8]),  # 342 + 465 = 807
            ([0], [0], [0]),  # 0 + 0 = 0
            (
                [9, 9, 9, 9, 9, 9, 9],
                [9, 9, 9, 9],
                [8, 9, 9, 9, 0, 0, 0, 1],
            ),  # 9999999 + 9999 = 10009998
        ]
        for l1_vals, l2_vals, expected in test_cases:
            for func in self.add_funcs:
                with self.subTest(func=func.__name__, l1=l1_vals, l2=l2_vals):
                    # 每次测试都需要重新构建链表，防止递归等算法的副作用影响
                    l1 = build_linked_list(l1_vals)
                    l2 = build_linked_list(l2_vals)
                    result_head = func(l1, l2)
                    self.assertEqual(linked_list_to_list(result_head), expected)

    def test_different_lengths(self):
        """测试两个链表长度差异较大的情况"""
        # 1000 + 99 = 1099 -> [0,0,0,1] + [9,9] = [9,9,0,1]
        l1_vals = [0, 0, 0, 1]
        l2_vals = [9, 9]
        expected = [9, 9, 0, 1]
        for func in self.add_funcs:
            with self.subTest(func=func.__name__):
                l1 = build_linked_list(l1_vals)
                l2 = build_linked_list(l2_vals)
                result_head = func(l1, l2)
                self.assertEqual(linked_list_to_list(result_head), expected)

    def test_carry_at_end(self):
        """测试最高位产生进位的情况"""
        # 99 + 1 = 100 -> [9,9] + [1] = [0,0,1]
        l1_vals = [9, 9]
        l2_vals = [1]
        expected = [0, 0, 1]
        for func in self.add_funcs:
            with self.subTest(func=func.__name__):
                l1 = build_linked_list(l1_vals)
                l2 = build_linked_list(l2_vals)
                result_head = func(l1, l2)
                self.assertEqual(linked_list_to_list(result_head), expected)

    def test_single_digit_no_carry(self):
        """测试单个数字且无进位的情况"""
        l1_vals = [3]
        l2_vals = [4]
        expected = [7]
        for func in self.add_funcs:
            with self.subTest(func=func.__name__):
                l1 = build_linked_list(l1_vals)
                l2 = build_linked_list(l2_vals)
                result_head = func(l1, l2)
                self.assertEqual(linked_list_to_list(result_head), expected)

    def test_single_digit_with_carry(self):
        """测试单个数字但有进位的情况"""
        l1_vals = [8]
        l2_vals = [7]
        expected = [5, 1]  # 8 + 7 = 15
        for func in self.add_funcs:
            with self.subTest(func=func.__name__):
                l1 = build_linked_list(l1_vals)
                l2 = build_linked_list(l2_vals)
                result_head = func(l1, l2)
                self.assertEqual(linked_list_to_list(result_head), expected)


if __name__ == "__main__":
    unittest.main()
