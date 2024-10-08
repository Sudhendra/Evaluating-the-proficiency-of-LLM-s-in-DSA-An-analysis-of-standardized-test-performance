class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        result = []
        low = 0
        high = n
        
        for char in s:
            if char == 'I':
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        
        result.append(low)
        
        return result
