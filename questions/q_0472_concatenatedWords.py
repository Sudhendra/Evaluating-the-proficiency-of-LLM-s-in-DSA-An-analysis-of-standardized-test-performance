front_matter = {
    "qid": 472,
    "title": "Concatenated Words",
    "titleSlug": "concatenated-words",
    "difficulty": "Hard",
    "tags": ["Array", "String", "Dynamic Programming", "Depth-First Search", "Trie"],
}
# ====================== DO NOT EDIT ABOVE THIS LINE ======================
class Solution:
    """Given an array of strings `words` (**without duplicates**), return *all the **concatenated words** in the given list of* `words`.

    A **concatenated word** is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.



    **Example 1:**

    ```
    Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
    Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
    "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
    "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
    ```
    **Example 2:**

    ```
    Input: words = ["cat","dog","catdog"]
    Output: ["catdog"]
    ```


    **Constraints:**

    * `1 <= words.length <= 10^{4}`
    * `1 <= words[i].length <= 30`
    * `words[i]` consists of only lowercase English letters.
    * All the strings of `words` are **unique**.
    * `1 <= sum(words[i].length) <= 10^{5}`
    """

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        pass

    # If you have multiple solutions, add them all here as methods of the same class.
