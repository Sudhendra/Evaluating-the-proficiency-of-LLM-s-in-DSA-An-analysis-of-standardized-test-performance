class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counts = collections.Counter(ransomNote)
        magazine_counts = collections.Counter(magazine)
        
        for char, count in ransom_counts.items():
            if magazine_counts[char] < count:
                return False
        
        return True