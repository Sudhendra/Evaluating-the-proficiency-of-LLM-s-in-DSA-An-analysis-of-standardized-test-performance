from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        return [num for num, _ in heapq.nlargest(k, counter.items(), key=lambda x: x[1])]
