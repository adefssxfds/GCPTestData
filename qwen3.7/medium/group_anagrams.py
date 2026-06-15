from typing import List, Dict
from collections import defaultdict
def group_anagrams(strs: List[str]) -> List[List[str]]:
    anagram_groups: Dict[str, List[str]] = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())


def group_anagrams_counting(strs: List[str]) -> List[List[str]]:
    anagram_groups: Dict[tuple, List[str]] = defaultdict(list)
    
    for s in strs:
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - ord('a')] += 1
        
        key = tuple(char_count)
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())


def group_anagrams_prime(strs: List[str]) -> List[List[str]]:
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    
    anagram_groups: Dict[int, List[str]] = defaultdict(list)
    
    for s in strs:
        key = 1
        for char in s:
            key *= primes[ord(char) - ord('a')]
        anagram_groups[key].append(s)
    
    return list(anagram_groups.values())
