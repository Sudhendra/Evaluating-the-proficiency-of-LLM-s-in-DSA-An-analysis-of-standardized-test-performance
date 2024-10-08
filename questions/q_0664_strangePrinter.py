front_matter = {
    "qid": 664,
    "title": "Strange Printer",
    "titleSlug": "strange-printer",
    "difficulty": "Hard",
    "tags": ["String", "Dynamic Programming"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """There is a strange printer with the following two special properties:

    * The printer can only print a sequence of **the same character** each time.
    * At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.

    Given a string `s`, return *the minimum number of turns the printer needed to print it*.



    **Example 1:**

    ```
    Input: s = "aaabbb"
    Output: 2
    Explanation: Print "aaa" first and then print "bbb".
    ```
    **Example 2:**

    ```
    Input: s = "aba"
    Output: 2
    Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
    ```


    **Constraints:**

    * `1 <= s.length <= 100`
    * `s` consists of lowercase English letters.
    """

    def strangePrinter(self, s: str) -> int:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
