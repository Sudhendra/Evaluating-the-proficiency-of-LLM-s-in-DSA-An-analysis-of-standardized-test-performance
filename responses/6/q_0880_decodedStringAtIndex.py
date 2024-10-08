class Solution:
    
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_length = 0
        n = len(s)
        
        for i in range(n):
            if s[i].isdigit():
                decoded_length *= int(s[i])
            else:
                decoded_length += 1
                
            if decoded_length >= k:
                for j in range(i, -1, -1):
                    if s[j].isdigit():
                        decoded_length /= int(s[j])
                        k %= decoded_length
                    else:
                        if k == 0 or k == decoded_length:
                            return s[j]
                        else:
                            decoded_length -= 1
        
        return ''
