from collections import Counter
import heapq
from functools import total_ordering

@total_ordering
class Word:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    
    def __eq__(self, other):
        if self.count == other.count:
            return self.word < other.word
        return self.count > other.count
    
    def __lt__(self, other):
        return (self.count < other.count) or (self.count == other.count and self.word > other.word)

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        min_heap = []
        
        for word, freq in count.items():
            heapq.heappush(min_heap, Word(freq, word))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        result = []
        while min_heap:
            result.insert(0, heapq.heappop(min_heap).word)
        
        return result

# Test cases
solution = Solution()
print(solution.topKFrequent(["i","love","leetcode","i","love","coding"], 2))  # Output: ["i", "love"]
print(solution.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4))  # Output: ["the", "is", "sunny", "day"]
```
