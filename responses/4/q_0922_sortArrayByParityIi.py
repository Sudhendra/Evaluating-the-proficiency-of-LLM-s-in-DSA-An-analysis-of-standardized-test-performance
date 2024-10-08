from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_idx = 0  # index for even numbers
        odd_idx = 1   # index for odd numbers
        n = len(nums)

        while even_idx < n and odd_idx < n:
            if nums[even_idx] % 2 == 0:  # even number found at even index
                even_idx += 2
            else:
                if nums[odd_idx] % 2 == 1:  # odd number found at odd index
                    odd_idx += 2
                else:  # swap the numbers
                    nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
                    even_idx += 2
                    odd_idx += 2

        return nums

#     # Another solution using two passes
#     def sortArrayByParityII(self, nums: List[int]) -> List[int]:
#         even, odd = [], []
#         result = [0] * len(nums)

#         for num in nums:
#             if num % 2 == 0:
#                 even.append(num)
#             else:
#                 odd.append(num)

#         for i in range(len(nums)):
#             if i % 2 == 0:
#                 result[i] = even.pop()
#             else:
#                 result[i] = odd.pop()

#         return result
