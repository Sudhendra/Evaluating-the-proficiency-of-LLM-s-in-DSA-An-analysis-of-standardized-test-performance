from typing import List

class Solution:
    
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2, candidate1, candidate2 = 0, 0, None, None

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        if nums.count(candidate1) > len(nums) // 3:
            result.append(candidate1)
        if candidate2 is not None and nums.count(candidate2) > len(nums) // 3:
            result.append(candidate2)

        return result