class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        count = [0] * (1 << 16)
        for i in nums:
            for j in nums:
                count[i & j] += 1
        
        result = 0
        for k in nums:
            for i in range(1 << 16):
                if (i & k) == 0:
                    result += count[i]
        
        return result
