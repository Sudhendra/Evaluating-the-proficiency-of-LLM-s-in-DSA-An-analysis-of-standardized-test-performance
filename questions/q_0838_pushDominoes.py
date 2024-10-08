front_matter = {
    "qid": 838,
    "title": "Push Dominoes",
    "titleSlug": "push-dominoes",
    "difficulty": "Medium",
    "tags": ["Two Pointers", "String", "Dynamic Programming"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """There are `n` dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

    After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

    When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

    For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

    You are given a string `dominoes` representing the initial state where:

    * `dominoes[i] = 'L'`, if the `i^{th}` domino has been pushed to the left,
    * `dominoes[i] = 'R'`, if the `i^{th}` domino has been pushed to the right, and
    * `dominoes[i] = '.'`, if the `i^{th}` domino has not been pushed.

    Return *a string representing the final state*.



    **Example 1:**

    ```
    Input: dominoes = "RR.L"
    Output: "RR.L"
    Explanation: The first domino expends no additional force on the second domino.
    ```
    **Example 2:**

    ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/05/18/domino.png)
    ```
    Input: dominoes = ".L.R...LR..L.."
    Output: "LL.RR.LLRRLL.."
    ```


    **Constraints:**

    * `n == dominoes.length`
    * `1 <= n <= 10^{5}`
    * `dominoes[i]` is either `'L'`, `'R'`, or `'.'`.
    """

    def pushDominoes(self, dominoes: str) -> str:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
