class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_string = ""
        for char in s:
            if char.isalpha():
                decoded_string += char
                if len(decoded_string) >= k:
                    return decoded_string[k - 1]
            else:
                decoded_string = decoded_string * int(char)
        return ""