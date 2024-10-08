front_matter = {
    "qid": 130,
    "title": "Surrounded Regions",
    "titleSlug": "surrounded-regions",
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
    """Given an `m x n` matrix `board` containing `'X'` and `'O'`, *capture all regions that are 4-directionally surrounded by* `'X'`.

    A region is **captured** by flipping all `'O'`s into `'X'`s in that surrounded region.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)
    ```
    Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    Explanation: Notice that an 'O' should not be flipped if:
    - It is on the border, or
    - It is adjacent to an 'O' that should not be flipped.
    The bottom 'O' is on the border, so it is not flipped.
    The other three 'O' form a surrounded region, so they are flipped.
    ```
    **Example 2:**

    ```
    Input: board = [["X"]]
    Output: [["X"]]
    ```


    **Constraints:**

    * `m == board.length`
    * `n == board[i].length`
    * `1 <= m, n <= 200`
    * `board[i][j]` is `'X'` or `'O'`.
    """

    def solve(self, board: List[List[str]]) -> None:
        pass
        """
        Do not return anything, modify board in-place instead.
        """

    # If you have multiple solutions, add them all here as methods of the same class.
