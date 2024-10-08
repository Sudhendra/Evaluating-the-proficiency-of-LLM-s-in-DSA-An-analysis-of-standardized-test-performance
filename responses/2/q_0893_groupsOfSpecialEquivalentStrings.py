class Solution:
    
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def get_key(word):
            even = sorted(word[0::2])
            odd = sorted(word[1::2])
            return tuple(even + odd)
        
        groups = set()
        for word in words:
            groups.add(get_key(word))
        
        return len(groups)