import pytest
from q_2146_kHighestRankedItemsWithinAPriceRange import Solution


@pytest.mark.parametrize(
    "grid, pricing, start, k, output",
    [
        (
            [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]],
            [2, 5],
            [0, 0],
            3,
            [[0, 1], [1, 1], [2, 1]],
        ),
        (
            [[1, 2, 0, 1], [1, 3, 3, 1], [0, 2, 5, 1]],
            [2, 3],
            [2, 3],
            2,
            [[2, 1], [1, 2]],
        ),
        ([[1, 1, 1], [0, 0, 1], [2, 3, 4]], [2, 3], [0, 0], 3, [[2, 1], [2, 0]]),
    ],
)
class TestSolution:
    def test_highestRankedKItems(
        self,
        grid: List[List[int]],
        pricing: List[int],
        start: List[int],
        k: int,
        output: List[List[int]],
    ):
        sc = Solution()
        assert (
            sc.highestRankedKItems(
                grid,
                pricing,
                start,
                k,
            )
            == output
        )
