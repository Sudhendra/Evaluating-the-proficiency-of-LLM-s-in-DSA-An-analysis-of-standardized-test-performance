class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def get_unique_representation(word):
            even_chars = "".join(sorted(word[::2]))
            odd_chars = "".join(sorted(word[1::2]))
            return even_chars + odd_chars
        
        unique_words = set()
        for word in words:
            unique_words.add(get_unique_representation(word))
        
        return len(unique_words)
