class Solution:
    def findLHS(self, nums):
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        
        max_length = 0
        for num in num_freq:
            if num+1 in num_freq:
                max_length = max(max_length, num_freq[num] + num_freq[num+1])
        
        return max_length