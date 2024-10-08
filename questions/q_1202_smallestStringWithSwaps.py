front_matter = {
    "qid": 1202,
    "title": "Smallest String With Swaps",
    "titleSlug": "smallest-string-with-swaps",
    "difficulty": "Medium",
    "tags": [
        "Array",
        "Hash Table",
        "String",
        "Depth-First Search",
        "Breadth-First Search",
        "Union Find",
        "Sorting",
    ],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a string `s`, and an array of pairs of indices in the string `pairs` where `pairs[i] = [a, b]` indicates 2 indices(0-indexed) of the string.

    You can swap the characters at any pair of indices in the given `pairs` **any number of times**.

    Return the lexicographically smallest string that `s` can be changed to after using the swaps.



    **Example 1:**

    ```
    Input: s = "dcab", pairs = [[0,3],[1,2]]
    Output: "bacd"
    **Explaination:**
    Swap s[0] and s[3], s = "bcad"
    Swap s[1] and s[2], s = "bacd"
    ```
    **Example 2:**

    ```
    Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
    Output: "abcd"
    **Explaination:**
    Swap s[0] and s[3], s = "bcad"
    Swap s[0] and s[2], s = "acbd"
    Swap s[1] and s[2], s = "abcd"
    ```
    **Example 3:**

    ```
    Input: s = "cba", pairs = [[0,1],[1,2]]
    Output: "abc"
    **Explaination:**
    Swap s[0] and s[1], s = "bca"
    Swap s[1] and s[2], s = "bac"
    Swap s[0] and s[1], s = "abc"
    ```


    **Constraints:**

    * `1 <= s.length <= 10^5`
    * `0 <= pairs.length <= 10^5`
    * `0 <= pairs[i][0], pairs[i][1] < s.length`
    * `s` only contains lower case English letters.
    """

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
