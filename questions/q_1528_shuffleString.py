front_matter = {
    "qid": 1528,
    "title": "Shuffle String",
    "titleSlug": "shuffle-string",
    "difficulty": "Easy",
    "tags": ["Array", "String"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a string `s` and an integer array `indices` of the **same length**. The string `s` will be shuffled such that the character at the `i^{th}` position moves to `indices[i]` in the shuffled string.

    Return *the shuffled string*.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2020/07/09/q1.jpg)
    ```
    Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
    Output: "leetcode"
    Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.
    ```
    **Example 2:**

    ```
    Input: s = "abc", indices = [0,1,2]
    Output: "abc"
    Explanation: After shuffling, each character remains in its position.
    ```


    **Constraints:**

    * `s.length == indices.length == n`
    * `1 <= n <= 100`
    * `s` consists of only lowercase English letters.
    * `0 <= indices[i] < n`
    * All values of `indices` are **unique**.
    """

    def restoreString(self, s: str, indices: List[int]) -> str:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
