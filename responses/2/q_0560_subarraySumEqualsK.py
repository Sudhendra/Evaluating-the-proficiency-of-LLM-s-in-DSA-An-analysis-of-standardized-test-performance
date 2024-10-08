class Solution:
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        sum_count = {0: 1}
        
        for num in nums:
            prefix_sum += num
            count += sum_count.get(prefix_sum - k, 0)
            sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
        
        return count