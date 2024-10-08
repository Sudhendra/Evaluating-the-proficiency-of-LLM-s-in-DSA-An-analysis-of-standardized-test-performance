import pytest
from q_0387_firstUniqueCharacterInAString import Solution


@pytest.mark.parametrize(
    "s, output", [("leetcode", 0), ("loveleetcode", 2), ("aabb", -1)]
)
class TestSolution:
    def test_firstUniqChar(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.firstUniqChar(
                s,
            )
            == output
        )
