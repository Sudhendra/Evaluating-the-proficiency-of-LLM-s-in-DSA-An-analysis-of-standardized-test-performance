class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        result = 0
        counter = collections.Counter(nums)
        
        for num in counter.keys():
            if k == 0:
                if counter[num] > 1:
                    result += 1
            else:
                if num + k in counter:
                    result += 1
        
        return result
