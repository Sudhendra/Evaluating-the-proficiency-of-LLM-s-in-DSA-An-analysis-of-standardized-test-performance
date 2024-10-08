class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def make_special(s):
            # Separate the string into special substrings
            count, i = 0, 0
            specials = []
            for j, char in enumerate(s):
                count += 1 if char == '1' else -1
                if count == 0:
                    specials.append('1' + make_special(s[i+1:j]) + '0')
                    i = j + 1
            return ''.join(sorted(specials, reverse=True))
        
        return make_special(s)
