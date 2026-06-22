from typing import List
def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        
        # Check if this character exists at position i in all strings
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]
    
    return strs[0]
def longest_common_prefix_horizontal(strs: List[str]) -> str:
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for i in range(1, len(strs)):
        # Find common prefix between current prefix and strs[i]
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix
def longest_common_prefix_divide_conquer(strs: List[str]) -> str:
    if not strs:
        return ""
    
    def lcp_helper(left: int, right: int) -> str:
        if left == right:
            return strs[left]
        
        mid = (left + right) // 2
        lcp_left = lcp_helper(left, mid)
        lcp_right = lcp_helper(mid + 1, right)
        
        return common_prefix(lcp_left, lcp_right)
    
    def common_prefix(s1: str, s2: str) -> str:
        min_len = min(len(s1), len(s2))
        for i in range(min_len):
            if s1[i] != s2[i]:
                return s1[:i]
        return s1[:min_len]
    
    return lcp_helper(0, len(strs) - 1)
def longest_common_prefix_trie(strs: List[str]) -> str:
    if not strs:
        return ""
    
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False
    
    # Build trie
    root = TrieNode()
    for s in strs:
        node = root
        for char in s:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    # Find longest common prefix
    prefix = []
    node = root
    
    while len(node.children) == 1 and not node.is_end:
        char = next(iter(node.children))
        prefix.append(char)
        node = node.children[char]
    
    return ''.join(prefix)
