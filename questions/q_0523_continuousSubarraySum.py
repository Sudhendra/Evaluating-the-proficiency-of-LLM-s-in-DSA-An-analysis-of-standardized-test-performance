front_matter = {
    "qid": 523,
    "title": "Continuous Subarray Sum",
    "titleSlug": "continuous-subarray-sum",
    "difficulty": "Medium",
    "tags": ["Array", "Hash Table", "Math", "Prefix Sum"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given an integer array nums and an integer k, return `true` *if* `nums` *has a **good subarray** or* `false` *otherwise*.

    A **good subarray** is a subarray where:

    * its length is **at least two**, and
    * the sum of the elements of the subarray is a multiple of `k`.

    **Note** that:

    * A **subarray** is a contiguous part of the array.
    * An integer `x` is a multiple of `k` if there exists an integer `n` such that `x = n * k`. `0` is **always** a multiple of `k`.



    **Example 1:**

    ```
    Input: nums = [23,2,4,6,7], k = 6
    Output: true
    Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
    ```
    **Example 2:**

    ```
    Input: nums = [23,2,6,4,7], k = 6
    Output: true
    Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
    42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
    ```
    **Example 3:**

    ```
    Input: nums = [23,2,6,4,7], k = 13
    Output: false
    ```


    **Constraints:**

    * `1 <= nums.length <= 10^{5}`
    * `0 <= nums[i] <= 10^{9}`
    * `0 <= sum(nums[i]) <= 2^{31} - 1`
    * `1 <= k <= 2^{31} - 1`
    """

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
