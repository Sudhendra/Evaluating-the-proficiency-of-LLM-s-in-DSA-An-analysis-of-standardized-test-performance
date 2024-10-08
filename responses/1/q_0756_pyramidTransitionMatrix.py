class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def build(pyramid):
            if len(pyramid) == 1:
                return True
            for i in range(len(pyramid) - 1):
                next_blocks = [j for j in allowed if j[:2] == pyramid[i:i+2]]
                if not next_blocks:
                    return False
                for block in next_blocks:
                    if build(pyramid[1:i] + block[2] + pyramid[i+1:]):
                        return True
            return False
        
        return build(bottom)