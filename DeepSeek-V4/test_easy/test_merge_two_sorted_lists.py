import unittest
from typing import Optional, List


# ---------- 链表节点定义 ----------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ---------- 三种合并实现（复制自题目） ----------
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


# ---------- 辅助函数：将列表转换为链表 ----------
def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# ---------- 辅助函数：将链表转换为列表 ----------
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ---------- 测试类 ----------
class TestMergeTwoLists(unittest.TestCase):
    def setUp(self):
        self.algorithms = [
            ("迭代", merge_two_lists),
            ("递归", merge_two_lists_recursive),
            ("原地合并", merge_two_lists_in_place),
        ]

    def test_examples(self):
        """题目提供的三个示例"""
        test_cases = [
            ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
            ([], [], []),
            ([], [0], [0]),
        ]
        for list1_vals, list2_vals, expected_vals in test_cases:
            for name, func in self.algorithms:
                with self.subTest(algorithm=name, list1=list1_vals, list2=list2_vals):
                    l1 = list_to_linked_list(list1_vals)
                    l2 = list_to_linked_list(list2_vals)
                    merged = func(l1, l2)
                    self.assertEqual(linked_list_to_list(merged), expected_vals)

    def test_both_single_element(self):
        """两个单节点链表"""
        test_cases = [([1], [2], [1, 2]), ([2], [1], [1, 2]), ([0], [0], [0, 0])]
        for list1_vals, list2_vals, expected in test_cases:
            for name, func in self.algorithms:
                with self.subTest(algorithm=name):
                    l1 = list_to_linked_list(list1_vals)
                    l2 = list_to_linked_list(list2_vals)
                    merged = func(l1, l2)
                    self.assertEqual(linked_list_to_list(merged), expected)

    def test_one_empty_one_nonempty(self):
        """一个空链表，一个非空"""
        test_cases = [([], [1, 2, 3], [1, 2, 3]), ([1, 2, 3], [], [1, 2, 3])]
        for list1_vals, list2_vals, expected in test_cases:
            for name, func in self.algorithms:
                with self.subTest(algorithm=name):
                    l1 = list_to_linked_list(list1_vals)
                    l2 = list_to_linked_list(list2_vals)
                    merged = func(l1, l2)
                    self.assertEqual(linked_list_to_list(merged), expected)

    def test_different_lengths(self):
        """长度不同的有序链表"""
        test_cases = [
            ([1, 5, 9], [2, 3, 4, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
            ([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6]),
        ]
        for list1_vals, list2_vals, expected in test_cases:
            for name, func in self.algorithms:
                with self.subTest(algorithm=name):
                    l1 = list_to_linked_list(list1_vals)
                    l2 = list_to_linked_list(list2_vals)
                    merged = func(l1, l2)
                    self.assertEqual(linked_list_to_list(merged), expected)

    def test_duplicate_values(self):
        """包含重复值的链表"""
        test_cases = [
            ([1, 1, 2], [1, 2, 2], [1, 1, 1, 2, 2, 2]),
            ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),
        ]
        for list1_vals, list2_vals, expected in test_cases:
            for name, func in self.algorithms:
                with self.subTest(algorithm=name):
                    l1 = list_to_linked_list(list1_vals)
                    l2 = list_to_linked_list(list2_vals)
                    merged = func(l1, l2)
                    self.assertEqual(linked_list_to_list(merged), expected)

    def test_negative_values(self):
        """包含负值的链表（已排序）"""
        test_cases = [
            ([-5, -3, -1], [-4, -2, 0], [-5, -4, -3, -2, -1, 0]),
            ([-10, -5], [-6, -1, 2], [-10, -6, -5, -1, 2]),
        ]
        for list1_vals, list2_vals, expected in test_cases:
            for name, func in self.algorithms:
                with self.subTest(algorithm=name):
                    l1 = list_to_linked_list(list1_vals)
                    l2 = list_to_linked_list(list2_vals)
                    merged = func(l1, l2)
                    self.assertEqual(linked_list_to_list(merged), expected)

    def test_large_values_up_to_100(self):
        """边界值 -100 和 100"""
        list1_vals = [-100, 0, 100]
        list2_vals = [-50, 50]
        expected = [-100, -50, 0, 50, 100]
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                l1 = list_to_linked_list(list1_vals)
                l2 = list_to_linked_list(list2_vals)
                merged = func(l1, l2)
                self.assertEqual(linked_list_to_list(merged), expected)

    def test_max_nodes_50(self):
        """测试最大节点数 50（每个链表 25 个节点）"""
        list1_vals = list(range(0, 50, 2))  # 0,2,4,...,48
        list2_vals = list(range(1, 50, 2))  # 1,3,5,...,49
        expected = list(range(50))
        for name, func in self.algorithms:
            with self.subTest(algorithm=name):
                l1 = list_to_linked_list(list1_vals)
                l2 = list_to_linked_list(list2_vals)
                merged = func(l1, l2)
                self.assertEqual(linked_list_to_list(merged), expected)

    def test_all_algorithms_identical(self):
        """随机测试，确保所有方法结果相同"""
        import random

        for _ in range(50):
            size1 = random.randint(0, 30)
            size2 = random.randint(0, 30)
            list1_vals = sorted([random.randint(-100, 100) for _ in range(size1)])
            list2_vals = sorted([random.randint(-100, 100) for _ in range(size2)])
            expected = sorted(list1_vals + list2_vals)
            results = []
            for name, func in self.algorithms:
                l1 = list_to_linked_list(list1_vals)
                l2 = list_to_linked_list(list2_vals)
                merged = func(l1, l2)
                results.append(linked_list_to_list(merged))
            self.assertEqual(
                len(set(tuple(r) for r in results)),
                1,
                f"Inconsistent results for list1={list1_vals}, list2={list2_vals}",
            )


if __name__ == "__main__":
    unittest.main()
