import pytest
from q_1573_numberOfWaysToSplitAString import Solution


@pytest.mark.parametrize("s, output", [("10101", 4), ("1001", 0), ("0000", 3)])
class TestSolution:
    def test_numWays(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.numWays(
                s,
            )
            == output
        )
