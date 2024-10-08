front_matter = {
    "qid": 2269,
    "title": "Find the K-Beauty of a Number",
    "titleSlug": "find-the-k-beauty-of-a-number",
    "difficulty": "Easy",
    "tags": ["Math", "String", "Sliding Window"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """The **k-beauty** of an integer `num` is defined as the number of **substrings** of `num` when it is read as a string that meet the following conditions:

    * It has a length of `k`.
    * It is a divisor of `num`.

    Given integers `num` and `k`, return *the k-beauty of* `num`.

    Note:

    * **Leading zeros** are allowed.
    * `0` is not a divisor of any value.

    A **substring** is a contiguous sequence of characters in a string.



    **Example 1:**

    ```
    Input: num = 240, k = 2
    Output: 2
    Explanation: The following are the substrings of num of length k:
    - "24" from "**24**0": 24 is a divisor of 240.
    - "40" from "2**40**": 40 is a divisor of 240.
    Therefore, the k-beauty is 2.
    ```
    **Example 2:**

    ```
    Input: num = 430043, k = 2
    Output: 2
    Explanation: The following are the substrings of num of length k:
    - "43" from "**43**0043": 43 is a divisor of 430043.
    - "30" from "4**30**043": 30 is not a divisor of 430043.
    - "00" from "43**00**43": 0 is not a divisor of 430043.
    - "04" from "430**04**3": 4 is not a divisor of 430043.
    - "43" from "4300**43**": 43 is a divisor of 430043.
    Therefore, the k-beauty is 2.
    ```


    **Constraints:**

    * `1 <= num <= 10^{9}`
    * `1 <= k <= num.length` (taking `num` as a string)
    """

    def divisorSubstrings(self, num: int, k: int) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
