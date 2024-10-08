front_matter = {
    "qid": 547,
    "title": "Number of Provinces",
    "titleSlug": "number-of-provinces",
    "difficulty": "Medium",
    "tags": ["Depth-First Search", "Breadth-First Search", "Union Find", "Graph"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

    A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

    You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i^{th}` city and the `j^{th}` city are directly connected, and `isConnected[i][j] = 0` otherwise.

    Return *the total number of **provinces***.



    **Example 1:**

    ![](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)
    ```
    Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    Output: 2
    ```
    **Example 2:**

    ![](https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg)
    ```
    Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
    Output: 3
    ```


    **Constraints:**

    * `1 <= n <= 200`
    * `n == isConnected.length`
    * `n == isConnected[i].length`
    * `isConnected[i][j]` is `1` or `0`.
    * `isConnected[i][i] == 1`
    * `isConnected[i][j] == isConnected[j][i]`
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
