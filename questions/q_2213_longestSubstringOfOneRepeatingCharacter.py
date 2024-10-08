front_matter = {
    "qid": 2213,
    "title": "Longest Substring of One Repeating Character",
    "titleSlug": "longest-substring-of-one-repeating-character",
    "difficulty": "Hard",
    "tags": ["Array", "String", "Segment Tree", "Ordered Set"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a **0-indexed** string `s`. You are also given a **0-indexed** string `queryCharacters` of length `k` and a **0-indexed** array of integer **indices** `queryIndices` of length `k`, both of which are used to describe `k` queries.

    The `i^{th}` query updates the character in `s` at index `queryIndices[i]` to the character `queryCharacters[i]`.

    Return *an array* `lengths` *of length* `k` *where* `lengths[i]` *is the **length** of the **longest substring** of* `s` *consisting of **only one repeating** character **after** the* `i^{th}` *query* *is performed.*



    **Example 1:**

    ```
    Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
    Output: [3,3,4]
    Explanation:
    - 1^{st} query updates s = "b**b**bacc". The longest substring consisting of one repeating character is "bbb" with length 3.
    - 2^{nd} query updates s = "bbb**c**cc".
      The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
    - 3^{rd} query updates s = "bbb**b**cc". The longest substring consisting of one repeating character is "bbbb" with length 4.
    Thus, we return [3,3,4].
    ```
    **Example 2:**

    ```
    Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
    Output: [2,3]
    Explanation:
    - 1^{st} query updates s = "ab**a**zz". The longest substring consisting of one repeating character is "zz" with length 2.
    - 2^{nd} query updates s = "a**a**azz". The longest substring consisting of one repeating character is "aaa" with length 3.
    Thus, we return [2,3].
    ```


    **Constraints:**

    * `1 <= s.length <= 10^{5}`
    * `s` consists of lowercase English letters.
    * `k == queryCharacters.length == queryIndices.length`
    * `1 <= k <= 10^{5}`
    * `queryCharacters` consists of lowercase English letters.
    * `0 <= queryIndices[i] < s.length`
    """

    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
