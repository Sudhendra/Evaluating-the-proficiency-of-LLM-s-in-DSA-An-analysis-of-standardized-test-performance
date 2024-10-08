from collections import defaultdict

class Solution:
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_subsequence(word):
            itr = iter(s)
            return all(c in itr for c in word)
        
        waiting = defaultdict(list)
        count = 0
        
        for word in words:
            if waiting.get(word):
                count += 1
                continue
            elif is_subsequence(word):
                count += 1
                waiting[word].append(True)
            else:
                waiting[word].append(False)
        
        return count
