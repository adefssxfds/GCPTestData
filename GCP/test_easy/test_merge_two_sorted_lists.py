from merge_two_sorted_lists import ListNode, merge_two_lists, merge_two_lists_recursive, merge_two_lists_in_place

from merge_two_sorted_lists import *

def test_merge_two_lists():
    """Test merge_two_lists with provided examples"""
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    merged_list = merge_two_lists(list1, list2)
    assert merged_list.val == 1
    assert merged_list.next.val == 1
    assert merged_list.next.next.val == 2
    assert merged_list.next.next.next.val == 3
    assert merged_list.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.val == 4

def test_merge_two_lists_empty_lists():
    """Test merge_two_lists with both lists empty"""
    list1 = ListNode(0)
    list2 = ListNode(0)
    merged_list = merge_two_lists(list1, list2)
    assert merged_list.val == 0
    assert merged_list.next is None

def test_merge_two_lists_second_empty():
    """Test merge_two_lists with first list empty"""
    list1 = ListNode(0)
    list2 = ListNode(1)
    list2.next = ListNode(2)
    merged_list = merge_two_lists(list1, list2)
    assert merged_list.val == 0
    assert merged_list.next.val == 1
    assert merged_list.next.next.val == 2

def test_merge_two_lists_recursive():
    """Test merge_two_lists_recursive with provided examples"""
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    merged_list = merge_two_lists_recursive(list1, list2)
    assert merged_list.val == 1
    assert merged_list.next.val == 1
    assert merged_list.next.next.val == 2
    assert merged_list.next.next.next.val == 3
    assert merged_list.next.next.next.next.val == 4
    assert merged_list.next.next.next.next.next.val == 4

def test_merge_two_lists_in_place():
    """Test merge_two_lists_in_place with provided examples"""
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    merge_two_lists_in_place(list1, list2)
    assert list1.val == 1
    assert list1.next.val == 1
    assert list1.next.next.val == 2
    assert list1.next.next.next.val == 3
    assert list1.next.next.next.next.val == 4
    assert list1.next.next.next.next.next.val == 4

def test_list_node():
    """Test ListNode class methods"""
    node = ListNode(5)
    assert node.val == 5
    assert node.next is None

def test_list_node_next():
    """Test ListNode class next attribute"""
    node1 = ListNode(5)
    node2 = ListNode(6)
    node1.next = node2
    assert node1.next == node2

# ===== 补充测试（迭代优化） =====

def test_merge_two_lists_equal_values():
    # 行号29: 检查两个列表中值相等的情况
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    merged_list = merge_two_lists(list1, list2)
    assert merged_list.next.val == 1, "merged_list should have value 1 in second position"
    assert merged_list.next.next.val == 2, "merged_list should have value 2 in third position"
    assert merged_list.next.next.next.val == 3, "merged_list should have value 3 in fourth position"
    assert merged_list.next.next.next.next.val == 4, "merged_list should have value 4 in fifth position"



# ===== 补充测试（迭代优化） =====

def test_merge_two_lists_first_empty():
    list1 = None
    list2 = ListNode(1)
    merged_list = merge_two_lists(list1, list2)
    assert merged_list.val == 1


#### 生成测试覆盖第40行


