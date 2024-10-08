class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)
        possible_sums = {0}
        
        for num in nums:
            new_sums = set()
            for s in possible_sums:
                new_sums.add(s)
                new_sums.add(s + num)
            possible_sums = new_sums
        
        for i in range(1, n//2 + 1):
            if total_sum * i % n == 0 and total_sum * i // n in possible_sums:
                return True
        
        return False