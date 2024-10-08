class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        
        count = 0
        pairs = set()
        nums.sort()
        
        if k == 0:
            unique_nums = set()
            for num in nums:
                if nums.count(num) >= 2:
                    unique_nums.add(num)
            return len(unique_nums)
        
        for i in range(len(nums)):
            if nums[i] + k in pairs:
                count += 1
                pairs.remove(nums[i] + k)
            pairs.add(nums[i])
        
        return count
