class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        if k < 0:
            return 0
        count = Counter(nums)
        pairs = 0
        for num in count:
            if k == 0:
                if count[num] > 1:
                    pairs += 1
            else:
                if num + k in count:
                    pairs += 1
        return pairs