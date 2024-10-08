import pytest
from q_1422_maximumScoreAfterSplittingAString import Solution


@pytest.mark.parametrize("s, output", [("011101", 5), ("00111", 5), ("1111", 3)])
class TestSolution:
    def test_maxScore(self, s: str, output: int):
        sc = Solution()
        assert (
            sc.maxScore(
                s,
            )
            == output
        )
