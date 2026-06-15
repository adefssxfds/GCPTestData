from typing import Optional


# 链表节点定义
class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1. 迭代法（dummy 节点，最推荐）
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


# 2. 递归法
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


# 3. 原地修改法（不使用 dummy）
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


# ==================== 工具函数 ====================
# 列表 -> 链表
def build_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    cur = head
    for num in arr[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head


# 链表 -> 列表
def linked_list_to_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


# ==================== 测试代码 ====================
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),  # 示例1
        ([], [], []),  # 示例2
        ([], [0], [0]),  # 示例3
        ([1], [1], [1, 1]),  # 相同值
        ([2], [1], [1, 2]),  # 顺序颠倒
        ([5], [1, 3, 4], [1, 3, 4, 5]),  # 一长一短
    ]

    functions = [
        ("迭代法 dummy", merge_two_lists),
        ("递归法", merge_two_lists_recursive),
        ("原地修改法", merge_two_lists_in_place),
    ]

    print("===== 合并两个有序链表 测试开始 =====\n")

    for idx, (l1_arr, l2_arr, expect) in enumerate(test_cases, 1):
        print(f"测试用例 {idx}")
        print(f"list1 = {l1_arr}, list2 = {l2_arr}")
        print(f"预期结果: {expect}")

        for name, func in functions:
            l1 = build_linked_list(l1_arr)
            l2 = build_linked_list(l2_arr)
            merged = func(l1, l2)
            output = linked_list_to_list(merged)
            status = "✅ 通过" if output == expect else "❌ 失败"
            print(f"  {name}: {output} | {status}")

        print("-" * 50)

    print("\n===== 所有测试完成 =====")
