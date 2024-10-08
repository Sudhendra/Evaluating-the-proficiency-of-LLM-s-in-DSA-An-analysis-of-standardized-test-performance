import pytest
from q_2477_minimumFuelCostToReportToTheCapital import Solution


@pytest.mark.parametrize(
    "roads, seats, output",
    [
        ([[0, 1], [0, 2], [0, 3]], 5, 3),
        ([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2, 7),
        ([], 1, 0),
    ],
)
class TestSolution:
    def test_minimumFuelCost(self, roads: List[List[int]], seats: int, output: int):
        sc = Solution()
        assert (
            sc.minimumFuelCost(
                roads,
                seats,
            )
            == output
        )
