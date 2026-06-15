from typing import List


# 1. 纵向扫描法
def longest_common_prefix(strs: List[str]) -> str:
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]

        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]

    return strs[0]


# 2. 横向扫描法
def longest_common_prefix_horizontal(strs: List[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]

    for i in range(1, len(strs)):
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


# 3. 分治法
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


# 4. 字典树 (Trie) 法
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

    return "".join(prefix)


# ==================== 测试代码 ====================
if __name__ == "__main__":
    # 测试用例：(输入数组, 预期输出)
    test_cases = [
        (["flower", "flow", "flight"], "fl"),  # 示例1
        (["dog", "racecar", "car"], ""),  # 示例2
        (["leetcode", "leet", "lee", "le"], "le"),  # 逐步缩短
        (["a"], "a"),  # 单个字符串
        (["ab", "a"], "a"),  # 前缀更短
        (["apple", "apple", "apple"], "apple"),  # 全部相同
        (["", "abc"], ""),  # 包含空字符串
    ]

    # 四个函数
    functions = [
        ("纵向扫描", longest_common_prefix),
        ("横向扫描", longest_common_prefix_horizontal),
        ("分治", longest_common_prefix_divide_conquer),
        ("字典树", longest_common_prefix_trie),
    ]

    print("===== 最长公共前缀 测试开始 =====\n")

    for idx, (strs_input, expect) in enumerate(test_cases, 1):
        print(f"测试用例 {idx}")
        print(f"输入: {strs_input}")
        print(f"预期: '{expect}'")

        for name, func in functions:
            output = func(strs_input)
            status = "✅ 通过" if output == expect else "❌ 失败"
            print(f"  {name}: '{output}' {status}")

        print("-" * 50)

    print("\n===== 所有测试完成 =====")
