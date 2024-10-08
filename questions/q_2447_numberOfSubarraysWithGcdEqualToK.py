front_matter = {
    "qid": 2447,
    "title": "Number of Subarrays With GCD Equal to K",
    "titleSlug": "number-of-subarrays-with-gcd-equal-to-k",
    "difficulty": "Medium",
    "tags": ["Array", "Math", "Number Theory"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given an integer array `nums` and an integer `k`, return *the number of **subarrays** of* `nums` *where the greatest common divisor of the subarray's elements is* `k`.

    A **subarray** is a contiguous non-empty sequence of elements within an array.

    The **greatest common divisor of an array** is the largest integer that evenly divides all the array elements.



    **Example 1:**

    ```
    Input: nums = [9,3,1,2,6,3], k = 3
    Output: 4
    Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
    - [9,**3**,1,2,6,3]
    - [9,3,1,2,6,**3**]
    - [**9,3**,1,2,6,3]
    - [9,3,1,2,**6,3**]
    ```
    **Example 2:**

    ```
    Input: nums = [4], k = 7
    Output: 0
    Explanation: There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.
    ```


    **Constraints:**

    * `1 <= nums.length <= 1000`
    * `1 <= nums[i], k <= 10^{9}`
    """

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
