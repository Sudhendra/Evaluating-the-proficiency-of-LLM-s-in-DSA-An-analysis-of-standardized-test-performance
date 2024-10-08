front_matter = {
    "qid": 953,
    "title": "Verifying an Alien Dictionary",
    "titleSlug": "verifying-an-alien-dictionary",
    "difficulty": "Easy",
    "tags": ["Array", "Hash Table", "String"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different `order`. The `order` of the alphabet is some permutation of lowercase letters.

    Given a sequence of `words` written in the alien language, and the `order` of the alphabet, return `true` if and only if the given `words` are sorted lexicographically in this alien language.



    **Example 1:**

    ```
    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
    ```
    **Example 2:**

    ```
    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
    ```
    **Example 3:**

    ```
    Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
    Output: false
    Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character ([More info](https://en.wikipedia.org/wiki/Lexicographical_order)).
    ```


    **Constraints:**

    * `1 <= words.length <= 100`
    * `1 <= words[i].length <= 20`
    * `order.length == 26`
    * All characters in `words[i]` and `order` are English lowercase letters.
    """

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
