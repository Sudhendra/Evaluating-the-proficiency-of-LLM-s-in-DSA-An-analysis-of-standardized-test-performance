front_matter = {
    "qid": 2264,
    "title": "Largest 3-Same-Digit Number in String",
    "titleSlug": "largest-3-same-digit-number-in-string",
    "difficulty": "Easy",
    "tags": ["String"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a string `num` representing a large integer. An integer is **good** if it meets the following conditions:

    * It is a **substring** of `num` with length `3`.
    * It consists of only one unique digit.

    Return *the **maximum good** integer as a **string** or an empty string* `""` *if no such integer exists*.

    Note:

    * A **substring** is a contiguous sequence of characters within a string.
    * There may be **leading zeroes** in `num` or a good integer.



    **Example 1:**

    ```
    Input: num = "6**777**133339"
    Output: "777"
    Explanation: There are two distinct good integers: "777" and "333".
    "777" is the largest, so we return "777".
    ```
    **Example 2:**

    ```
    Input: num = "23**000**19"
    Output: "000"
    Explanation: "000" is the only good integer.
    ```
    **Example 3:**

    ```
    Input: num = "42352338"
    Output: ""
    Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.
    ```


    **Constraints:**

    * `3 <= num.length <= 1000`
    * `num` only consists of digits.
    """

    def largestGoodInteger(self, num: str) -> str:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
