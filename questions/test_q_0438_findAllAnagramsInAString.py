import pytest
from q_0438_findAllAnagramsInAString import Solution


@pytest.mark.parametrize(
    "s, p, output", [("cbaebabacd", "abc", [0, 6]), ("abab", "ab", [0, 1, 2])]
)
class TestSolution:
    def test_findAnagrams(self, s: str, p: str, output: List[int]):
        sc = Solution()
        assert (
            sc.findAnagrams(
                s,
                p,
            )
            == output
        )
