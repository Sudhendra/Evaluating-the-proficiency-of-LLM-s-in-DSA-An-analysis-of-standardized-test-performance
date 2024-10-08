front_matter = {
    "qid": 2957,
    "title": "Remove Adjacent Almost-Equal Characters",
    "titleSlug": "remove-adjacent-almost-equal-characters",
    "difficulty": "Medium",
    "tags": ["String", "Dynamic Programming", "Greedy"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a **0-indexed** string `word`.

    In one operation, you can pick any index `i` of `word` and change `word[i]` to any lowercase English letter.

    Return *the **minimum** number of operations needed to remove all adjacent **almost-equal** characters from* `word`.

    Two characters `a` and `b` are **almost-equal** if `a == b` or `a` and `b` are adjacent in the alphabet.



    **Example 1:**

    ```
    Input: word = "aaaaa"
    Output: 2
    Explanation: We can change word into "a**c**a**c**a" which does not have any adjacent almost-equal characters.
    It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
    ```
    **Example 2:**

    ```
    Input: word = "abddez"
    Output: 2
    Explanation: We can change word into "**y**bd**o**ez" which does not have any adjacent almost-equal characters.
    It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 2.
    ```
    **Example 3:**

    ```
    Input: word = "zyxyxyz"
    Output: 3
    Explanation: We can change word into "z**a**x**a**x**a**z" which does not have any adjacent almost-equal characters.
    It can be shown that the minimum number of operations needed to remove all adjacent almost-equal characters from word is 3.
    ```


    **Constraints:**

    * `1 <= word.length <= 100`
    * `word` consists only of lowercase English letters.
    """

    def removeAlmostEqualCharacters(self, word: str) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
