front_matter = {
    "qid": 678,
    "title": "Valid Parenthesis String",
    "titleSlug": "valid-parenthesis-string",
    "difficulty": "Medium",
    "tags": ["String", "Dynamic Programming", "Stack", "Greedy"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given a string `s` containing only three types of characters: `'('`, `')'` and `'*'`, return `true` *if* `s` *is **valid***.

    The following rules define a **valid** string:

    * Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
    * Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
    * Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
    * `'*'` could be treated as a single right parenthesis `')'` or a single left parenthesis `'('` or an empty string `""`.



    **Example 1:**

    ```
    Input: s = "()"
    Output: true
    ```
    **Example 2:**

    ```
    Input: s = "(*)"
    Output: true
    ```
    **Example 3:**

    ```
    Input: s = "(*))"
    Output: true
    ```


    **Constraints:**

    * `1 <= s.length <= 100`
    * `s[i]` is `'('`, `')'` or `'*'`.
    """

    def checkValidString(self, s: str) -> bool:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
