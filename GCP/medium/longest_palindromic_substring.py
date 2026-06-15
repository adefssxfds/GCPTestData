def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    def expand_around_center(left: int, right: int) -> int:
        """Expand around center and return length of palindrome."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        current_max = max(len1, len2)
        
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]


def longest_palindrome_dp(s: str) -> str:
    if not s:
        return ""
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    start = 0
    max_len = 1
    
    for i in range(n):
        dp[i][i] = True
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    start = i
                    max_len = length
    
    return s[start:start + max_len]


def longest_palindrome_manacher(s: str) -> str:
    if not s:
        return ""
    processed = '#'.join('^{}$'.format(s))
    n = len(processed)
    P = [0] * n
    center = right = 0
    
    for i in range(1, n - 1):
        mirror = 2 * center - i
        
        if i < right:
            P[i] = min(right - i, P[mirror])
        try:
            while processed[i + P[i] + 1] == processed[i - P[i] - 1]:
                P[i] += 1
        except IndexError:
            pass
        if i + P[i] > right:
            center, right = i, i + P[i]
    max_len = max(P)
    center_index = P.index(max_len)
    start = (center_index - max_len) // 2
    return s[start:start + max_len]
