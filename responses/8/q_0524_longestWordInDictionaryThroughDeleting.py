from typing import List

class Solution:
    """Given a string `s` and a string array `dictionary`, return the longest string in the dictionary that can be formed by deleting some of the given string characters.
    If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.
    """

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subsequence(word, s):
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            return i == len(word)

        res = ""
        for word in dictionary:
            if is_subsequence(word, s):
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word
        return res
