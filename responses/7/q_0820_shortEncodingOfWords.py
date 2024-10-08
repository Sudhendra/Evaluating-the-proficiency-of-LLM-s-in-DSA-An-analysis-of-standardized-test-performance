class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)  # Convert the list to a set to remove duplicates
        result = 0
        for word in words:
            for i in range(1, len(word)):  # For each possible suffix
                if word[i:] in words:
                    break
            else:
                result += len(word) + 1  # Add word length + '#'
        return result
