import pytest
from q_2577_minimumTimeToVisitACellInAGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]], 7),
        ([[0, 2, 4], [3, 2, 1], [1, 0, 4]], -1),
    ],
)
class TestSolution:
    def test_minimumTime(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minimumTime(
                grid,
            )
            == output
        )
