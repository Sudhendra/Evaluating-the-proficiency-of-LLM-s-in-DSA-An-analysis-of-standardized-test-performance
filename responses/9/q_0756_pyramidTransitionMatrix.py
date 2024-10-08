from typing import List

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        def build_pyramid_level(current, above, allowed_set):
            if len(current) == 1:
                return True

            if len(current) == len(above) + 1:
                return build_pyramid_level("", current, allowed_set)

            pos = len(above)
            for pattern in allowed_set:
                if current[pos:pos+2] not in pattern[:2]:
                    continue

                if build_pyramid_level(current + pattern[2], above, allowed_set):
                    return True

            return False

        allowed_set = set(allowed)

        return build_pyramid_level(bottom, "", allowed_set)
