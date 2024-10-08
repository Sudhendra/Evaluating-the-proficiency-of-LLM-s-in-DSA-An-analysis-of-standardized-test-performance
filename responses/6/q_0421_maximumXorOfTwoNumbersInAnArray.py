class Solution:
    def findMaximumXOR(self, nums):
        ans = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= 1 << i
            prefixes = set()
            for num in nums:
                prefixes.add(num & mask)
            
            candidate = ans | 1 << i
            for prefix in prefixes:
                if prefix ^ candidate in prefixes:
                    ans = candidate
                    break
        
        return ans
