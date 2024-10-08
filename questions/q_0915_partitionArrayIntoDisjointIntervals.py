front_matter = {
    "qid": 915,
    "title": "Partition Array into Disjoint Intervals",
    "titleSlug": "partition-array-into-disjoint-intervals",
    "difficulty": "Medium",
    "tags": ["Array"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given an integer array `nums`, partition it into two (contiguous) subarrays `left` and `right` so that:

    * Every element in `left` is less than or equal to every element in `right`.
    * `left` and `right` are non-empty.
    * `left` has the smallest possible size.

    Return *the length of* `left` *after such a partitioning*.

    Test cases are generated such that partitioning exists.



    **Example 1:**

    ```
    Input: nums = [5,0,3,8,6]
    Output: 3
    Explanation: left = [5,0,3], right = [8,6]
    ```
    **Example 2:**

    ```
    Input: nums = [1,1,1,0,6,12]
    Output: 4
    Explanation: left = [1,1,1,0], right = [6,12]
    ```


    **Constraints:**

    * `2 <= nums.length <= 10^{5}`
    * `0 <= nums[i] <= 10^{6}`
    * There is at least one valid answer for the given input.
    """

    def partitionDisjoint(self, nums: List[int]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
