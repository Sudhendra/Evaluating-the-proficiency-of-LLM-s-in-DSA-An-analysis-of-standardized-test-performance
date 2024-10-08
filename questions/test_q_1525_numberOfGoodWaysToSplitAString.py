import pytest
from q_1525_numberOfGoodWaysToSplitAString import Solution


@pytest.mark.parametrize("s, output", [("aacaba", 2), ("abcd", 1)])
class TestSolution:
    def test_numSplits(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.numSplits(
                s,
            )
            == output
        )
