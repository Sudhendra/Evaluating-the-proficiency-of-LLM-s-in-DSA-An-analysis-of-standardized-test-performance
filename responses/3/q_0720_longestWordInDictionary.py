class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        words_set = set(words)
        longest_word = ""
        
        for word in words:
            if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                if all(word[:i] in words_set for i in range(1, len(word))):
                    longest_word = word
                    
        return longest_word