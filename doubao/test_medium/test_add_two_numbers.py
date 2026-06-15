from typing import Optional


# 链表节点定义
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 三种解法
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


# ===================== 工具函数 =====================
# 将列表转换为链表
def list_to_linkedlist(arr):
    dummy = ListNode(0)
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next


# 将链表转换为列表（方便打印查看结果）
def linkedlist_to_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


# 统一测试函数
def test_solution(func, l1_arr, l2_arr, expected):
    l1 = list_to_linkedlist(l1_arr)
    l2 = list_to_linkedlist(l2_arr)
    result_head = func(l1, l2)
    result = linkedlist_to_list(result_head)
    status = "PASS" if result == expected else "FAIL"
    print(f"输入l1: {l1_arr}, 输入l2: {l2_arr}")
    print(f"预期结果: {expected}, 实际结果: {result} -> {status}\n")


# ===================== 测试用例 =====================
if __name__ == "__main__":
    # 测试用例1：基础示例 342 + 465 = 807
    print("===== 测试用例 1 =====")
    test_solution(add_two_numbers, [2, 4, 3], [5, 6, 4], [7, 0, 8])
    test_solution(add_two_numbers_recursive, [2, 4, 3], [5, 6, 4], [7, 0, 8])
    test_solution(add_two_numbers_optimized, [2, 4, 3], [5, 6, 4], [7, 0, 8])

    # 测试用例2：零值情况 0 + 0 = 0
    print("===== 测试用例 2 =====")
    test_solution(add_two_numbers, [0], [0], [0])
    test_solution(add_two_numbers_recursive, [0], [0], [0])
    test_solution(add_two_numbers_optimized, [0], [0], [0])

    # 测试用例3：超长链表+连续进位 9999999 + 9999 = 10009998
    print("===== 测试用例 3 =====")
    test_solution(
        add_two_numbers, [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]
    )
    test_solution(
        add_two_numbers_recursive,
        [9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9],
        [8, 9, 9, 9, 0, 0, 0, 1],
    )
    test_solution(
        add_two_numbers_optimized,
        [9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9],
        [8, 9, 9, 9, 0, 0, 0, 1],
    )

    # 测试用例4：长度不一致的普通情况
    print("===== 测试用例 4 =====")
    test_solution(add_two_numbers, [1, 2], [3, 4, 5], [4, 6, 5])
    test_solution(add_two_numbers_recursive, [1, 2], [3, 4, 5], [4, 6, 5])
    test_solution(add_two_numbers_optimized, [1, 2], [3, 4, 5], [4, 6, 5])

    # 测试用例5：最高位进位
    print("===== 测试用例 5 =====")
    test_solution(add_two_numbers, [9, 9], [1], [0, 0, 1])
    test_solution(add_two_numbers_recursive, [9, 9], [1], [0, 0, 1])
    test_solution(add_two_numbers_optimized, [9, 9], [1], [0, 0, 1])
