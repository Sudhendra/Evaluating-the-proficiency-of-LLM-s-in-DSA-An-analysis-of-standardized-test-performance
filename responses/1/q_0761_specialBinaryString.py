class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        count, i = 0, 0
        res = []
        for j, char in enumerate(s):
            count += 1 if char == "1" else -1
            if count == 0:
                res.append("1" + self.makeLargestSpecial(s[i + 1:j]) + "0")
                i = j + 1
        return "".join(sorted(res, reverse=True))
