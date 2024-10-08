front_matter = {
    "qid": 2222,
    "title": "Number of Ways to Select Buildings",
    "titleSlug": "number-of-ways-to-select-buildings",
    "difficulty": "Medium",
    "tags": ["String", "Dynamic Programming", "Prefix Sum"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """You are given a **0-indexed** binary string `s` which represents the types of buildings along a street where:

    * `s[i] = '0'` denotes that the `i^{th}` building is an office and
    * `s[i] = '1'` denotes that the `i^{th}` building is a restaurant.

    As a city official, you would like to **select** 3 buildings for random inspection. However, to ensure variety, **no two consecutive** buildings out of the **selected** buildings can be of the same type.

    * For example, given `s = "0**0**1**1**0**1**"`, we cannot select the `1^{st}`, `3^{rd}`, and `5^{th}` buildings as that would form `"0**11**"` which is **not** allowed due to having two consecutive buildings of the same type.

    Return *the **number of valid ways** to select 3 buildings.*



    **Example 1:**

    ```
    Input: s = "001101"
    Output: 6
    Explanation:
    The following sets of indices selected are valid:
    - [0,2,4] from "**0**0**1**1**0**1" forms "010"
    - [0,3,4] from "**0**01**10**1" forms "010"
    - [1,2,4] from "0**01**1**0**1" forms "010"
    - [1,3,4] from "0**0**1**10**1" forms "010"
    - [2,4,5] from "00**1**1**01**" forms "101"
    - [3,4,5] from "001**101**" forms "101"
    No other selection is valid. Thus, there are 6 total ways.
    ```
    **Example 2:**

    ```
    Input: s = "11100"
    Output: 0
    Explanation: It can be shown that there are no valid selections.
    ```


    **Constraints:**

    * `3 <= s.length <= 10^{5}`
    * `s[i]` is either `'0'` or `'1'`.
    """

    def numberOfWays(self, s: str) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
