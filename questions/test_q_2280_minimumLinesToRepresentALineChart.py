import pytest
from q_2280_minimumLinesToRepresentALineChart import Solution


@pytest.mark.parametrize(
    "stockPrices, output",
    [
        ([[1, 7], [2, 6], [3, 5], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1]], 3),
        ([[3, 4], [1, 2], [7, 8], [2, 3]], 1),
    ],
)
class TestSolution:
    def test_minimumLines(self, stockPrices: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minimumLines(
                stockPrices,
            )
            == output
        )
