class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        result = []
        if not words:
            return result
        
        common_chars = set(words[0])
        for word in words[1:]:
            common_chars.intersection_update(set(word))
        
        for char in common_chars:
            min_count = min(word.count(char) for word in words)
            result.extend([char] * min_count)
        
        return result