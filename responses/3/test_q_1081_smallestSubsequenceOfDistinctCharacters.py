import pytest
from q_1081_smallestSubsequenceOfDistinctCharacters import Solution


@pytest.mark.parametrize("s, output", [("bcabc", "abc"), ("cbacdcbc", "acdb")])
class TestSolution:
    def test_smallestSubsequence(self, s: str, output: str):
        sc = Solution()
        assert (
            sc.smallestSubsequence(
                s,
            )
            == output
        )
