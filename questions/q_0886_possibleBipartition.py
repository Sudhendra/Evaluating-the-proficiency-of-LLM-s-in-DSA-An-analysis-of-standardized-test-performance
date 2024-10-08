front_matter = {
    "qid": 886,
    "title": "Possible Bipartition",
    "titleSlug": "possible-bipartition",
    "difficulty": "Medium",
    "tags": ["Depth-First Search", "Breadth-First Search", "Union Find", "Graph"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """We want to split a group of `n` people (labeled from `1` to `n`) into two groups of **any size**. Each person may dislike some other people, and they should not go into the same group.

    Given the integer `n` and the array `dislikes` where `dislikes[i] = [ai, bi]` indicates that the person labeled `ai` does not like the person labeled `bi`, return `true` *if it is possible to split everyone into two groups in this way*.



    **Example 1:**

    ```
    Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
    Output: true
    Explanation: The first group has [1,4], and the second group has [2,3].
    ```
    **Example 2:**

    ```
    Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
    Output: false
    Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.
    ```


    **Constraints:**

    * `1 <= n <= 2000`
    * `0 <= dislikes.length <= 10^{4}`
    * `dislikes[i].length == 2`
    * `1 <= ai < bi <= n`
    * All the pairs of `dislikes` are **unique**.
    """

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
