class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        
        count = Counter(s)
        length = 0
        odd_present = False
        
        for c in count:
            if count[c] % 2 == 0:
                length += count[c]
            else:
                length += count[c] - 1
                odd_present = True
        
        if odd_present:
            return length + 1
        else:
            return length
