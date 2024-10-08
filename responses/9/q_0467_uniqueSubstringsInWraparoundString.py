front_matter = {
    "qid": 467,
    "title": "Unique Substrings in Wraparound String",
    "titleSlug": "unique-substrings-in-wraparound-string",
    "difficulty": "Medium",
    "tags": ["String", "Dynamic Programming"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """We define the string `base` to be the infinite wraparound string of `"abcdefghijklmnopqrstuvwxyz"`, so `base` will look like this:

    * `"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...."`.

    Given a string `s`, return *the number of **unique non-empty substrings** of* `s` *are present in* `base`.

    **Example 1:**

    ```
    Input: s = "a"
    Output: 1
    Explanation: Only the substring "a" of s is in base.
    ```
    **Example 2:**

    ```
    Input: s = "cac"
    Output: 2
    Explanation: There are two substrings ("a", "c") of s in base.
    ```
    **Example 3:**

    ```
    Input: s = "zab"
    Output: 6
    Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of s in base.
    ```

    **Constraints:**

    * `1 <= s.length <= 10^{5}`
    * `s` consists of lowercase English letters.
    """

    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0

        longest_substring_ending_here = [0] * 26
        longest_substring_ending_here[ord(s[0]) - ord('a')] = 1
        current_max_length = 1

        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
                current_max_length += 1
            else:
                current_max_length = 1

            idx = ord(s[i]) - ord('a')
            longest_substring_ending_here[idx] = max(longest_substring_ending_here[idx], current_max_length)

        return sum(longest_substring_ending_here)