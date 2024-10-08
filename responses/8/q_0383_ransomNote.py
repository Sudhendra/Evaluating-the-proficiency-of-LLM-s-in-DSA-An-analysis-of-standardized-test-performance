class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counts = {}
        magazine_counts = {}

        for char in ransomNote:
            ransom_counts[char] = ransom_counts.get(char, 0) + 1

        for char in magazine:
            magazine_counts[char] = magazine_counts.get(char, 0) + 1

        for char, count in ransom_counts.items():
            if char not in magazine_counts or magazine_counts[char] < count:
                return False

        return True
