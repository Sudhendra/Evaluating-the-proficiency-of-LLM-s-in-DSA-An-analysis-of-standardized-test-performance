class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        charIndexMap = {}
        
        for i, char in enumerate(s):
            if char in charIndexMap and start <= charIndexMap[char]:
                start = charIndexMap[char] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            
            charIndexMap[char] = i
        
        return maxLength
