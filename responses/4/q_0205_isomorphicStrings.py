class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False

        char_map_s = {}
        char_map_t = {}

        for char_s, char_t in zip(s, t):
            if char_s in char_map_s:
                if char_map_s[char_s] != char_t:
                    return False
            else:
                char_map_s[char_s] = char_t

            if char_t in char_map_t:
                if char_map_t[char_t] != char_s:
                    return False
            else:
                char_map_t[char_t] = char_s

        return True
