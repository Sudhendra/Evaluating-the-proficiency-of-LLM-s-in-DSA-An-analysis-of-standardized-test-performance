class Solution:
    def is_palindrome(self, num: str) -> bool:
        return num == num[::-1]

    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        if num < 10:
            return str(num - 1)

        def diff(x):
            return (abs(int(x) - num), int(x))

        if num == 10**len(n) - 1:
            return str(10**len(n) + 1)
        
        candidates = {str(10**len(n) - 1), str(10**len(n) + 1)}
        prefix = int(n[:len(n)//2 + len(n) % 2])
        for start in (prefix - 1, prefix, prefix + 1):
            s = str(start)
            candidates.add(s + (s[:-1] if len(n) % 2 == 0 else s)[:-1][::-1])

        return str(min(diff(x)[1] for x in candidates if x != n and not self.is_palindrome(x)))
