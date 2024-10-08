class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def count_special_equivalent(s):
            even_chars = ''.join(sorted(s[::2]))
            odd_chars = ''.join(sorted(s[1::2]))
            return (even_chars, odd_chars)

        groups = set()
        for word in words:
            groups.add(count_special_equivalent(word))

        return len(groups)