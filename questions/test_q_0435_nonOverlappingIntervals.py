import pytest
from q_0435_nonOverlappingIntervals import Solution


@pytest.mark.parametrize(
    "intervals, output",
    [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
    ],
)
class TestSolution:
    def test_eraseOverlapIntervals(self, intervals: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.eraseOverlapIntervals(
                intervals,
            )
            == output
        )
