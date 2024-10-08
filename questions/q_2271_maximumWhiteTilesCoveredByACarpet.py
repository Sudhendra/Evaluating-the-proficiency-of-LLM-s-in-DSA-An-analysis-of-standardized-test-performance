front_matter = {
    "qid": 2271,
    "title": "Maximum White Tiles Covered by a Carpet",
    "titleSlug": "maximum-white-tiles-covered-by-a-carpet",
    "difficulty": "Medium",
    "tags": ["Array", "Binary Search", "Greedy", "Sorting", "Prefix Sum"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a 2D integer array `tiles` where `tiles[i] = [li, ri]` represents that every tile `j` in the range `li <= j <= ri` is colored white.

    You are also given an integer `carpetLen`, the length of a single carpet that can be placed **anywhere**.

    Return *the **maximum** number of white tiles that can be covered by the carpet*.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2022/03/25/example1drawio3.png)
    ```
    Input: tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
    Output: 9
    Explanation: Place the carpet starting on tile 10.
    It covers 9 white tiles, so we return 9.
    Note that there may be other places where the carpet covers 9 white tiles.
    It can be shown that the carpet cannot cover more than 9 white tiles.
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2022/03/24/example2drawio.png)
    ```
    Input: tiles = [[10,11],[1,1]], carpetLen = 2
    Output: 2
    Explanation: Place the carpet starting on tile 10.
    It covers 2 white tiles, so we return 2.
    ```


    **Constraints:**

    * `1 <= tiles.length <= 5 * 10^{4}`
    * `tiles[i].length == 2`
    * `1 <= li <= ri <= 10^{9}`
    * `1 <= carpetLen <= 10^{9}`
    * The `tiles` are **non-overlapping**.
    """

    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
