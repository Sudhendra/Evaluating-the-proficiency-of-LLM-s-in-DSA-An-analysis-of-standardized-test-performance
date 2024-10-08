from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        
        for char in s:
            for it in waiting.pop(char, ()):
                waiting[next(it, None)].append(it)
                
        return len(waiting[None])
