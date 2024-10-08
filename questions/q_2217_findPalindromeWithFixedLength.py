front_matter = {
    "qid": 2217,
    "title": "Find Palindrome With Fixed Length",
    "titleSlug": "find-palindrome-with-fixed-length",
    "difficulty": "Medium",
    "tags": ["Array", "Math"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given an integer array `queries` and a **positive** integer `intLength`, return *an array* `answer` *where* `answer[i]` *is either the* `queries[i]^{th}` *smallest **positive palindrome** of length* `intLength` *or* `-1` *if no such palindrome exists*.

    A **palindrome** is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.



    **Example 1:**

    ```
    Input: queries = [1,2,3,4,5,90], intLength = 3
    Output: [101,111,121,131,141,999]
    Explanation:
    The first few palindromes of length 3 are:
    101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
    The 90^{th} palindrome of length 3 is 999.
    ```
    **Example 2:**

    ```
    Input: queries = [2,4,6], intLength = 4
    Output: [1111,1331,1551]
    Explanation:
    The first six palindromes of length 4 are:
    1001, 1111, 1221, 1331, 1441, and 1551.
    ```


    **Constraints:**

    * `1 <= queries.length <= 5 * 10^{4}`
    * `1 <= queries[i] <= 10^{9}`
    * `1 <= intLength <= 15`
    """

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
