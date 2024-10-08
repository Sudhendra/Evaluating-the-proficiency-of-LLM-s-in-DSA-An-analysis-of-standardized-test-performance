class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_str = ""
        
        for char in s:
            if char.isalpha():
                decoded_str += char
                if len(decoded_str) >= k:
                    return decoded_str[k-1]
            elif char.isdigit():
                decoded_str = decoded_str * int(char)
        
        return decoded_str[k-1]
