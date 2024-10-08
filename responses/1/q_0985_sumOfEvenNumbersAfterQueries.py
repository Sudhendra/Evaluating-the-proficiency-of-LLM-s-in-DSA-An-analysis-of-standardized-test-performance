from typing import List

class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        result = []

        for val, index in queries:
            current_num = nums[index]
            is_even = current_num % 2 == 0
            if is_even:
                even_sum -= current_num

            nums[index] += val
            new_num = nums[index]
            if new_num % 2 == 0:
                even_sum += new_num

            result.append(even_sum)

        return result
