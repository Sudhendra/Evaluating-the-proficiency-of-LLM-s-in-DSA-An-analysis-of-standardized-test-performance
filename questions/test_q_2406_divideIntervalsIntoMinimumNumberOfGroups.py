import pytest
from q_2406_divideIntervalsIntoMinimumNumberOfGroups import Solution


@pytest.mark.parametrize(
    "intervals, output",
    [
        ([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]], 3),
        ([[1, 3], [5, 6], [8, 10], [11, 13]], 1),
    ],
)
class TestSolution:
    def test_minGroups(self, intervals: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minGroups(
                intervals,
            )
            == output
        )
