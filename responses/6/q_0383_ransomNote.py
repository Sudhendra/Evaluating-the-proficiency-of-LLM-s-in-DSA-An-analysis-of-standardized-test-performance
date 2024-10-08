class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        ransom_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        
        for char, count in ransom_counts.items():
            if magazine_counts[char] < count:
                return False
        
        return True
