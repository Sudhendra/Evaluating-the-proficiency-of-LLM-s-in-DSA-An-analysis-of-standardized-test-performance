front_matter = {
    "qid": 2718,
    "title": "Sum of Matrix After Queries",
    "titleSlug": "sum-of-matrix-after-queries",
    "difficulty": "Medium",
    "tags": ["Array", "Hash Table"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given an integer `n` and a **0-indexed** **2D array** `queries` where `queries[i] = [typei, indexi, vali]`.

    Initially, there is a **0-indexed** `n x n` matrix filled with `0`'s. For each query, you must apply one of the following changes:

    * if `typei == 0`, set the values in the row with `indexi` to `vali`, overwriting any previous values.
    * if `typei == 1`, set the values in the column with `indexi` to `vali`, overwriting any previous values.

    Return *the sum of integers in the matrix after all queries are applied*.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2023/05/11/exm1.png)
    ```
    Input: n = 3, queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
    Output: 23
    Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 23.
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2023/05/11/exm2.png)
    ```
    Input: n = 3, queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
    Output: 17
    Explanation: The image above describes the matrix after each query. The sum of the matrix after all queries are applied is 17.
    ```


    **Constraints:**

    * `1 <= n <= 10^{4}`
    * `1 <= queries.length <= 5 * 10^{4}`
    * `queries[i].length == 3`
    * `0 <= typei <= 1`
    * `0 <= indexi < n`
    * `0 <= vali <= 10^{5}`
    """

    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
