import unittest
from typing import Optional, List, Any


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# --- 将你的三个算法放在这里 ---
def merge_two_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    current.next = list1 if list1 else list2
    return dummy.next


def merge_two_lists_recursive(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val <= list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2


def merge_two_lists_in_place(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val > list2.val:
        list1, list2 = list2, list1
    head = list1
    while list1.next and list2:
        if list1.next.val <= list2.val:
            list1 = list1.next
        else:
            temp = list2.next
            list2.next = list1.next
            list1.next = list2
            list2 = temp
            list1 = list1.next
    if list2:
        list1.next = list2
    return head


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
class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        # 统一管理三种合并算法
        self.merge_funcs = [
            merge_two_lists,
            merge_two_lists_recursive,
            merge_two_lists_in_place,
        ]

    def test_examples(self):
        """测试题目给定的示例"""
        test_cases = [
            ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
            ([], [], []),
            ([], [0], [0]),
        ]
        for list1_vals, list2_vals, expected in test_cases:
            for func in self.merge_funcs:
                with self.subTest(
                    func=func.__name__, list1=list1_vals, list2=list2_vals
                ):
                    # 每次测试都需要重新构建链表，防止原地修改影响后续测试
                    l1 = build_linked_list(list1_vals)
                    l2 = build_linked_list(list2_vals)
                    merged_head = func(l1, l2)
                    self.assertEqual(linked_list_to_list(merged_head), expected)

    def test_no_overlap(self):
        """测试两个链表完全没有交集（一个全小于另一个）"""
        list1_vals = [1, 2, 3]
        list2_vals = [4, 5, 6]
        expected = [1, 2, 3, 4, 5, 6]
        for func in self.merge_funcs:
            with self.subTest(func=func.__name__):
                l1 = build_linked_list(list1_vals)
                l2 = build_linked_list(list2_vals)
                merged_head = func(l1, l2)
                self.assertEqual(linked_list_to_list(merged_head), expected)

    def test_identical_lists(self):
        """测试两个完全相同的链表"""
        list1_vals = [2, 2, 2]
        list2_vals = [2, 2, 2]
        expected = [2, 2, 2, 2, 2, 2]
        for func in self.merge_funcs:
            with self.subTest(func=func.__name__):
                l1 = build_linked_list(list1_vals)
                l2 = build_linked_list(list2_vals)
                merged_head = func(l1, l2)
                self.assertEqual(linked_list_to_list(merged_head), expected)

    def test_negative_numbers(self):
        """测试包含负数的链表"""
        list1_vals = [-5, -3, 0]
        list2_vals = [-4, -2, 1]
        expected = [-5, -4, -3, -2, 0, 1]
        for func in self.merge_funcs:
            with self.subTest(func=func.__name__):
                l1 = build_linked_list(list1_vals)
                l2 = build_linked_list(list2_vals)
                merged_head = func(l1, l2)
                self.assertEqual(linked_list_to_list(merged_head), expected)

    def test_different_lengths(self):
        """测试长度差异极大的链表"""
        list1_vals = [1]
        list2_vals = [2, 3, 4, 5, 6]
        expected = [1, 2, 3, 4, 5, 6]
        for func in self.merge_funcs:
            with self.subTest(func=func.__name__):
                l1 = build_linked_list(list1_vals)
                l2 = build_linked_list(list2_vals)
                merged_head = func(l1, l2)
                self.assertEqual(linked_list_to_list(merged_head), expected)


if __name__ == "__main__":
    unittest.main()
