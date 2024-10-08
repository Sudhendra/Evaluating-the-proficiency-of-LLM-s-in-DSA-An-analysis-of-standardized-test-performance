import pytest
from q_1061_lexicographicallySmallestEquivalentString import Solution


@pytest.mark.parametrize(
    "s1, s2, baseStr, output",
    [
        ("parker", "morris", "parser", "makkek"),
        ("hello", "world", "hold", "hdld"),
        ("leetcode", "programs", "sourcecode", "aauaaaaada"),
    ],
)
class TestSolution:
    def test_smallestEquivalentString(
        self, s1: str, s2: str, baseStr: str, output: str
    ):
        sc = Solution()
        assert (
            sc.smallestEquivalentString(
                s1,
                s2,
                baseStr,
            )
            == output
        )
