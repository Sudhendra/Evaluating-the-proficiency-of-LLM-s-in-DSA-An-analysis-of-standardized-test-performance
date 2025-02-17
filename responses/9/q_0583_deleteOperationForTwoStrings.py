front_matter = {
    "qid": 583,
    "title": "Delete Operation for Two Strings",
    "titleSlug": "delete-operation-for-two-strings",
    "difficulty": "Medium",
    "tags": ["String", "Dynamic Programming"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given two strings `word1` and `word2`, return *the minimum number of **steps** required to make* `word1` *and* `word2` *the same*.

    In one **step**, you can delete exactly one character in either string.

    **Example 1:**
    ```
    Input: word1 = "sea", word2 = "eat"
    Output: 2
    Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
    ```
    **Example 2:**
    ```
    Input: word1 = "leetcode", word2 = "etco"
    Output: 4
    ```

    **Constraints:**
    * `1 <= word1.length, word2.length <= 500`
    * `word1` and `word2` consist of only lowercase English letters.
    """

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        return m + n - 2 * dp[m][n]