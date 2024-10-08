front_matter = {
    "qid": 1004,
    "title": "Max Consecutive Ones III",
    "titleSlug": "max-consecutive-ones-iii",
    "difficulty": "Medium",
    "tags": ["Array", "Binary Search", "Sliding Window", "Prefix Sum"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a binary array `nums` and an integer `k`, return *the maximum number of consecutive* `1`*'s in the array if you can flip at most* `k` `0`'s.



    **Example 1:**

    ```
    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,**1**,1,1,1,1,**1**]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    ```
    **Example 2:**

    ```
    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,**1**,**1**,1,1,1,**1**,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    ```


    **Constraints:**

    * `1 <= nums.length <= 10^{5}`
    * `nums[i]` is either `0` or `1`.
    * `0 <= k <= nums.length`
    """

    def longestOnes(self, nums: List[int], k: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
