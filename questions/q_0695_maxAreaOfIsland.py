front_matter = {
    "qid": 695,
    "title": "Max Area of Island",
    "titleSlug": "max-area-of-island",
    "difficulty": "Medium",
    "tags": [
        "Array",
        "Depth-First Search",
        "Breadth-First Search",
        "Union Find",
        "Matrix",
    ],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s (representing land) connected **4-directionally** (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

    The **area** of an island is the number of cells with a value `1` in the island.

    Return *the maximum **area** of an island in* `grid`. If there is no island, return `0`.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)
    ```
    Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    Output: 6
    Explanation: The answer is not 11, because the island must be connected 4-directionally.
    ```
    **Example 2:**

    ```
    Input: grid = [[0,0,0,0,0,0,0,0]]
    Output: 0
    ```


    **Constraints:**

    * `m == grid.length`
    * `n == grid[i].length`
    * `1 <= m, n <= 50`
    * `grid[i][j]` is either `0` or `1`.
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
