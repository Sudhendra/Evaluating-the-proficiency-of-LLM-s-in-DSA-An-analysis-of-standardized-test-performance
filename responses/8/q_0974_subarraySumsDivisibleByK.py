from typing import List

class Solution:
    """Given an integer array `nums` and an integer `k`, return *the number of non-empty **subarrays** that have a sum divisible by* `k`.

    A **subarray** is a **contiguous** part of an array.

    **Example 1:**

    ```
    Input: nums = [4,5,0,-2,-3,1], k = 5
    Output: 7
    Explanation: There are 7 subarrays with a sum divisible by k = 5:
    [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
    ```
    **Example 2:**

    ```
    Input: nums = [5], k = 9
    Output: 0
    ```


    **Constraints:**

    * `1 <= nums.length <= 3 * 10^{4}`
    * `-10^{4} <= nums[i] <= 10^{4}`
    * `2 <= k <= 10^{4}`
    """

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        mods = {0: 1}

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            count += mods.get(prefix_sum, 0)
            mods[prefix_sum] = mods.get(prefix_sum, 0) + 1

        return count
