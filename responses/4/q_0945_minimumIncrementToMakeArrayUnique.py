from collections import Counter

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        taken = set()
        result = 0
        for num, freq in counter.items():
            while freq > 1 or num in taken:
                if freq > 1:
                    result += freq - 1
                    taken.add(num)
                    freq -= 1
                num += 1
        return result
