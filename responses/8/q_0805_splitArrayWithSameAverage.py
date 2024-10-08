from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)
        
        possible_sums = [{0}]
        is_possible = False
        
        for num in nums:
            new_sums = []
            for sums in possible_sums:
                for prev_sum in sums:
                    new_sum = prev_sum + num
                    new_sums.append(new_sum)
                    if 0 < new_sum * n == new_sum * len(sums) == total_sum * len(sums) // n:
                        is_possible = True
                        break
            possible_sums.extend(new_sums)
        
        return is_possible

# Additional solutions can be added within the same class if needed
