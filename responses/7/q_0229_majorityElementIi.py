from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count1, count2 = 0, 0
        candidate1, candidate2 = None, None

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
        if nums.count(candidate1) > n // 3:
            result.append(candidate1)
        if nums.count(candidate2) > n // 3:
            result.append(candidate2)

        return result
