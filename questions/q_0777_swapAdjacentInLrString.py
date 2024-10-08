front_matter = {
    "qid": 777,
    "title": "Swap Adjacent in LR String",
    "titleSlug": "swap-adjacent-in-lr-string",
    "difficulty": "Medium",
    "tags": ["Two Pointers", "String"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """In a string composed of `'L'`, `'R'`, and `'X'` characters, like `"RXXLRXRXL"`, a move consists of either replacing one occurrence of `"XL"` with `"LX"`, or replacing one occurrence of `"RX"` with `"XR"`. Given the starting string `start` and the ending string `end`, return `True` if and only if there exists a sequence of moves to transform one string to the other.



    **Example 1:**

    ```
    Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
    Output: true
    Explanation: We can transform start to end following these steps:
    RXXLRXRXL ->
    XRXLRXRXL ->
    XRLXRXRXL ->
    XRLXXRRXL ->
    XRLXXRRLX
    ```
    **Example 2:**

    ```
    Input: start = "X", end = "L"
    Output: false
    ```


    **Constraints:**

    * `1 <= start.length <= 10^{4}`
    * `start.length == end.length`
    * Both `start` and `end` will only consist of characters in `'L'`, `'R'`, and `'X'`.
    """

    def canTransform(self, start: str, end: str) -> bool:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
