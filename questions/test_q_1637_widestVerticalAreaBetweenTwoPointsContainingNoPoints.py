import pytest
from q_1637_widestVerticalAreaBetweenTwoPointsContainingNoPoints import Solution


@pytest.mark.parametrize(
    "points, output",
    [
        ([[8, 7], [9, 9], [7, 4], [9, 7]], 1),
        ([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]], 3),
    ],
)
class TestSolution:
    def test_maxWidthOfVerticalArea(self, points: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxWidthOfVerticalArea(
                points,
            )
            == output
        )
