# ====================== DO NOT EDIT ABOVE THIS LINE ======================
from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_counts = Counter(words)
        heap = [(-freq, word) for word, freq in word_counts.items()]
        heapify(heap)
        return [heappop(heap)[1] for _ in range(k)]

# The solution uses a Counter to count the frequency of each word, then converts the freq-word pairs to a max heap and pops k most frequent words.
