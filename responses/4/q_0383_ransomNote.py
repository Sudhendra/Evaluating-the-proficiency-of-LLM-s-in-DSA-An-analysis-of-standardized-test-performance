class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        ransom_count = collections.Counter(ransomNote)
        magazine_count = collections.Counter(magazine)
        
        for char, count in ransom_count.items():
            if char not in magazine_count or magazine_count[char] < count:
                return False
        
        return True
