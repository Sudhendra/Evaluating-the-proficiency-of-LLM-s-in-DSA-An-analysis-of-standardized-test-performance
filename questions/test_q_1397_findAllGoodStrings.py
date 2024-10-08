import pytest
from q_1397_findAllGoodStrings import Solution


@pytest.mark.parametrize(
    "n, s1, s2, evil, output",
    [
        (2, "aa", "da", "b", 51),
        (8, "leetcode", "leetgoes", "leet", 0),
        (2, "gx", "gz", "x", 2),
    ],
)
class TestSolution:
    def test_findGoodStrings(self, n: int, s1: str, s2: str, evil: str, output: int):
        sc = Solution()
        assert (
            sc.findGoodStrings(
                n,
                s1,
                s2,
                evil,
            )
            == output
        )
