front_matter = {
    "qid": 409,
    "title": "Longest Palindrome",
    "titleSlug": "longest-palindrome",
    "difficulty": "Easy",
    "tags": ["Hash Table", "String", "Greedy"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a string `s` which consists of lowercase or uppercase letters, return *the length of the **longest palindrome*** that can be built with those letters.

    Letters are **case sensitive**, for example, `"Aa"` is not considered a palindrome here.

    **Example 1:**

    ```
    Input: s = "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
    ```

    **Example 2:**

    ```
    Input: s = "a"
    Output: 1
    Explanation: The longest palindrome that can be built is "a", whose length is 1.
    ```

    **Constraints:**

    * `1 <= s.length <= 2000`
    * `s` consists of lowercase **and/or** uppercase English letters only.
    """

    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        odd_count = sum(val % 2 for val in counts.values())
        return len(s) if odd_count <= 1 else len(s) - odd_count + 1

    # If you have multiple solutions, add them all here as methods of the same class.