import pytest
from q_1876_substringsOfSizeThreeWithDistinctCharacters import Solution


@pytest.mark.parametrize("s, output", [("xyzzaz", 1), ("aababcabc", 4)])
class TestSolution:
    def test_countGoodSubstrings(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.countGoodSubstrings(
                s,
            )
            == output
        )
