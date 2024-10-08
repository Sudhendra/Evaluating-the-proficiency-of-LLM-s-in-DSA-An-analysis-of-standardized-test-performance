from itertools import combinations

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        possible_sums = {0}
        
        for num in nums:
            new_sums = set()
            for val in possible_sums:
                new_sums.add(val)
                new_sums.add(val + num)
            possible_sums = new_sums
        
        for i in range(1, n // 2 + 1):
            if total * i % n == 0 and total * i // n in possible_sums:
                return True
        return False
