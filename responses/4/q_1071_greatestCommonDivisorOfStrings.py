class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        if len(str1) < len(str2):
            str1, str2 = str2, str1

        if str1 + str2 != str2 + str1:
            return ""

        return str1[:gcd(len(str1), len(str2))]
