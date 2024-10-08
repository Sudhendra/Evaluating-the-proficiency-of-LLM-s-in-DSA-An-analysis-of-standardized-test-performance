from collections import defaultdict
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        
        for char in s:
            if char in waiting:
                for it in waiting[char]:
                    next_char = next(it, None)
                    if next_char is not None:
                        waiting[next_char].append(it)
        
        return sum(1 for it in waiting.values() if not it)

# Time complexity analysis:
# Let n be the length of string s and m be the total number of characters in the words list.
# The time complexity of this solution is O(n + m) since we iterate over each character in s once and iterate over each character in the words list.
