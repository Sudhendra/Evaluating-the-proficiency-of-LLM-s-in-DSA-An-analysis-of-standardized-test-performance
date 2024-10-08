from typing import List

class Solution:
    """Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

    In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

    ![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)


    **Example 1:**

    ```
    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    ```
    **Example 2:**

    ```
    Input: numRows = 1
    Output: [[1]]
    ```


    **Constraints:**

    * `1 <= numRows <= 30`
    """

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        result = [[1]]

        for i in range(1, numRows):
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)

        return result
