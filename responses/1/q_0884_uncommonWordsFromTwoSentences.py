class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter
        
        uncommon_words = []
        s1_words = s1.split()
        s2_words = s2.split()
        
        count_s1 = Counter(s1_words)
        count_s2 = Counter(s2_words)
        
        for word, count in count_s1.items():
            if count == 1 and count_s2.get(word, 0) == 0:
                uncommon_words.append(word)
                
        for word, count in count_s2.items():
            if count == 1 and count_s1.get(word, 0) == 0:
                uncommon_words.append(word)
        
        return uncommon_words
