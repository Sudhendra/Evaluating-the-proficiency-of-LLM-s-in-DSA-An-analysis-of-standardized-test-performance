front_matter = {
    "qid": 1727,
    "title": "Largest Submatrix With Rearrangements",
    "titleSlug": "largest-submatrix-with-rearrangements",
    "difficulty": "Medium",
    "tags": ["Array", "Greedy", "Sorting", "Matrix"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a binary matrix `matrix` of size `m x n`, and you are allowed to rearrange the **columns** of the `matrix` in any order.

    Return *the area of the largest submatrix within* `matrix` *where **every** element of the submatrix is* `1` *after reordering the columns optimally.*



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40536-pm.png)
    ```
    Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
    Output: 4
    Explanation: You can rearrange the columns as shown above.
    The largest submatrix of 1s, in bold, has an area of 4.
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40852-pm.png)
    ```
    Input: matrix = [[1,0,1,0,1]]
    Output: 3
    Explanation: You can rearrange the columns as shown above.
    The largest submatrix of 1s, in bold, has an area of 3.
    ```
    **Example 3:**

    ```
    Input: matrix = [[1,1,0],[1,0,1]]
    Output: 2
    Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
    ```


    **Constraints:**

    * `m == matrix.length`
    * `n == matrix[i].length`
    * `1 <= m * n <= 10^{5}`
    * `matrix[i][j]` is either `0` or `1`.
    """

    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
