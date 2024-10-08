from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum_remainder = defaultdict(int)  # Dictionary to store the remainder of prefix sums
        prefix_sum_remainder[0] = 1  # Initialize with 0 to account for subarrays starting at index 0

        running_sum = 0
        count = 0

        for num in nums:
            running_sum = (running_sum + num) % k
            count += prefix_sum_remainder[running_sum]
            prefix_sum_remainder[running_sum] += 1

        return count
