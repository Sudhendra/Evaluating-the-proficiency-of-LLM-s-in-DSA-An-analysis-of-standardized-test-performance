class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        if str1[:len(str2)] == str2 and str1.count(str2) == len(str1) // len(str2) and str2.count(str2) == 1:
            return str2
        elif len(str2) == 1:
            return str1 if str1 == str1[:len(str1) * len(str2)] else ""
        else:
            return self.gcdOfStrings(str2, str1[len(str2):])
