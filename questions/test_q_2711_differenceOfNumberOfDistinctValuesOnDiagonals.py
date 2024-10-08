import pytest
from q_2711_differenceOfNumberOfDistinctValuesOnDiagonals import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[1, 2, 3], [3, 1, 5], [3, 2, 1]], [[1, 1, 0], [1, 0, 1], [0, 1, 1]]),
        ([[1]], [[0]]),
    ],
)
class TestSolution:
    def test_differenceOfDistinctValues(
        self, grid: List[List[int]], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.differenceOfDistinctValues(
                grid,
            )
            == output
        )
