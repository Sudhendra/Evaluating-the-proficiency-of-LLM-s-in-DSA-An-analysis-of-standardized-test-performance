front_matter = {
    "qid": 2007,
    "title": "Find Original Array From Doubled Array",
    "titleSlug": "find-original-array-from-doubled-array",
    "difficulty": "Medium",
    "tags": ["Array", "Hash Table", "Greedy", "Sorting"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """An integer array `original` is transformed into a **doubled** array `changed` by appending **twice the value** of every element in `original`, and then randomly **shuffling** the resulting array.

    Given an array `changed`, return `original` *if* `changed` *is a **doubled** array. If* `changed` *is not a **doubled** array, return an empty array. The elements in* `original` *may be returned in **any** order*.



    **Example 1:**

    ```
    Input: changed = [1,3,4,2,6,8]
    Output: [1,3,4]
    Explanation: One possible original array could be [1,3,4]:
    - Twice the value of 1 is 1 * 2 = 2.
    - Twice the value of 3 is 3 * 2 = 6.
    - Twice the value of 4 is 4 * 2 = 8.
    Other original arrays could be [4,3,1] or [3,1,4].
    ```
    **Example 2:**

    ```
    Input: changed = [6,3,0,1]
    Output: []
    Explanation: changed is not a doubled array.
    ```
    **Example 3:**

    ```
    Input: changed = [1]
    Output: []
    Explanation: changed is not a doubled array.
    ```


    **Constraints:**

    * `1 <= changed.length <= 10^{5}`
    * `0 <= changed[i] <= 10^{5}`
    """

    def findOriginalArray(self, changed: List[int]) -> List[int]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
