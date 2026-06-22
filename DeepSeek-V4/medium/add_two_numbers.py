from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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


def add_two_numbers_recursive(l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
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


def add_two_numbers_optimized(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
