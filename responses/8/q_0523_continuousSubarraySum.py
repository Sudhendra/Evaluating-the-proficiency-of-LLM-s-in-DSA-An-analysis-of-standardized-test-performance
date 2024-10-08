class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cumulative_sum = 0
        seen_remainders = {0: -1}

        for i, num in enumerate(nums):
            cumulative_sum += num
            remainder = cumulative_sum % k if k != 0 else cumulative_sum

            if remainder in seen_remainders:
                if i - seen_remainders[remainder] > 1:
                    return True
            else:
                seen_remainders[remainder] = i

        return False
