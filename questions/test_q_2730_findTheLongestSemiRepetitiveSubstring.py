import pytest
from q_2730_findTheLongestSemiRepetitiveSubstring import Solution


@pytest.mark.parametrize("s, output", [("52233", 4), ("5494", 4), ("1111111", 2)])
class TestSolution:
    def test_longestSemiRepetitiveSubstring(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.longestSemiRepetitiveSubstring(
                s,
            )
            == output
        )
