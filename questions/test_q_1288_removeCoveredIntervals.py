import pytest
from q_1288_removeCoveredIntervals import Solution


@pytest.mark.parametrize(
    "intervals, output", [([[1, 4], [3, 6], [2, 8]], 2), ([[1, 4], [2, 3]], 1)]
)
class TestSolution:
    def test_removeCoveredIntervals(self, intervals: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.removeCoveredIntervals(
                intervals,
            )
            == output
        )
