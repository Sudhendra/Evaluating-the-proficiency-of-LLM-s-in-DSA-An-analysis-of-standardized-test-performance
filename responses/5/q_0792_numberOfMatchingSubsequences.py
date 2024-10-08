from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        
        count = 0
        for char in s:
            if char in waiting:
                next_iter = waiting[char]
                waiting[char] = []
                for it in next_iter:
                    nxt = next(it, None)
                    if nxt is not None:
                        waiting[nxt].append(it)
                    else:
                        count += 1
                
        return count
