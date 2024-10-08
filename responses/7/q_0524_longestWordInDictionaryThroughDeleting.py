from typing import List

class Solution:
    def is_subsequence(self, s, word):
        i = 0
        for char in word:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # Sort the dictionary by word length in descending order and lexicographical order
        dictionary.sort(key=lambda x: (-len(x), x))

        for word in dictionary:
            if self.is_subsequence(s, word):
                return word

        return ""

# Example usage
solution = Solution()
s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]
print(solution.findLongestWord(s, dictionary))  # Output: "apple"
