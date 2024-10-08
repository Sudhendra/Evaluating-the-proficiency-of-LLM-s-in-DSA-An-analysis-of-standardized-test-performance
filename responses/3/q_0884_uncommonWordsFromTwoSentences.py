class Solution:
    
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = s1.split()
        s2_words = s2.split()
        
        freq_map = {}
        for word in s1_words + s2_words:
            freq_map[word] = freq_map.get(word, 0) + 1
        
        return [word for word, count in freq_map.items() if count == 1]