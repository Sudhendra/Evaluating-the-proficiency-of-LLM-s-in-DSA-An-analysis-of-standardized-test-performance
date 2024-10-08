import pytest
from q_0452_minimumNumberOfArrowsToBurstBalloons import Solution


@pytest.mark.parametrize(
    "points, output",
    [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ],
)
class TestSolution:
    def test_findMinArrowShots(self, points: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.findMinArrowShots(
                points,
            )
            == output
        )
