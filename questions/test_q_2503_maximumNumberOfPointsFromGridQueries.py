import pytest
from q_2503_maximumNumberOfPointsFromGridQueries import Solution


@pytest.mark.parametrize(
    "grid, queries, output",
    [
        ([[1, 2, 3], [2, 5, 7], [3, 5, 1]], [5, 6, 2], [5, 8, 1]),
        ([[5, 2, 1], [1, 1, 2]], [3], [0]),
    ],
)
class TestSolution:
    def test_maxPoints(
        self, grid: List[List[int]], queries: List[int], output: List[int]
    ):
        sc = Solution()
        assert (
            sc.maxPoints(
                grid,
                queries,
            )
            == output
        )
