front_matter = {
    "qid": 907,
    "title": "Sum of Subarray Minimums",
    "titleSlug": "sum-of-subarray-minimums",
    "difficulty": "Medium",
    "tags": ["Array", "Dynamic Programming", "Stack", "Monotonic Stack"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given an array of integers arr, find the sum of `min(b)`, where `b` ranges over every (contiguous) subarray of `arr`. Since the answer may be large, return the answer **modulo** `10^{9} + 7`.



    **Example 1:**

    ```
    Input: arr = [3,1,2,4]
    Output: 17
    Explanation:
    Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
    Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
    Sum is 17.
    ```
    **Example 2:**

    ```
    Input: arr = [11,81,94,43,3]
    Output: 444
    ```


    **Constraints:**

    * `1 <= arr.length <= 3 * 10^{4}`
    * `1 <= arr[i] <= 3 * 10^{4}`
    """

    def sumSubarrayMins(self, arr: List[int]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
