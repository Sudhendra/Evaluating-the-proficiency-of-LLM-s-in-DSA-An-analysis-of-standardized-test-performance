front_matter = {
    "qid": 2472,
    "title": "Maximum Number of Non-overlapping Palindrome Substrings",
    "titleSlug": "maximum-number-of-non-overlapping-palindrome-substrings",
    "difficulty": "Hard",
    "tags": ["String", "Dynamic Programming"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a string `s` and a **positive** integer `k`.

    Select a set of **non-overlapping** substrings from the string `s` that satisfy the following conditions:

    * The **length** of each substring is **at least** `k`.
    * Each substring is a **palindrome**.

    Return *the **maximum** number of substrings in an optimal selection*.

    A **substring** is a contiguous sequence of characters within a string.



    **Example 1:**

    ```
    Input: s = "abaccdbbd", k = 3
    Output: 2
    Explanation: We can select the substrings underlined in s = "**aba**cc**dbbd**". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
    It can be shown that we cannot find a selection with more than two valid substrings.
    ```
    **Example 2:**

    ```
    Input: s = "adbcda", k = 2
    Output: 0
    Explanation: There is no palindrome substring of length at least 2 in the string.
    ```


    **Constraints:**

    * `1 <= k <= s.length <= 2000`
    * `s` consists of lowercase English letters.
    """

    def maxPalindromes(self, s: str, k: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
