class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def get_special_eqv_key(word):
            return tuple(sorted(word[::2]) + sorted(word[1::2]))

        special_eqvs = set()
        for word in words:
            special_eqv_key = get_special_eqv_key(word)
            special_eqvs.add(special_eqv_key)

        return len(special_eqvs)