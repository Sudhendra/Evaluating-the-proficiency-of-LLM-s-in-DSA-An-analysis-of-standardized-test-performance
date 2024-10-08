front_matter = {
    "qid": 790,
    "title": "Domino and Tromino Tiling",
    "titleSlug": "domino-and-tromino-tiling",
    "difficulty": "Medium",
    "tags": ["Dynamic Programming"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You have two types of tiles: a `2 x 1` domino shape and a tromino shape. You may rotate these shapes.

    ![](https://assets.leetcode.com/uploads/2021/07/15/lc-domino.jpg)
    Given an integer n, return *the number of ways to tile an* `2 x n` *board*. Since the answer may be very large, return it **modulo** `10^{9} + 7`.

    In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2021/07/15/lc-domino1.jpg)
    ```
    Input: n = 3
    Output: 5
    Explanation: The five different ways are show above.
    ```
    **Example 2:**

    ```
    Input: n = 1
    Output: 1
    ```


    **Constraints:**

    * `1 <= n <= 1000`
    """

    def numTilings(self, n: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
