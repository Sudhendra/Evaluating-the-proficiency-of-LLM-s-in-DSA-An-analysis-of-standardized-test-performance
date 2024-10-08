import pytest
from q_1260_shift2DGrid import Solution


@pytest.mark.parametrize(
    "grid, k, output",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [[9, 1, 2], [3, 4, 5], [6, 7, 8]]),
        (
            [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]],
            4,
            [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]],
        ),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    ],
)
class TestSolution:
    def test_shiftGrid(self, grid: List[List[int]], k: int, output: List[List[int]]):
        sc = Solution()
        assert (
            sc.shiftGrid(
                grid,
                k,
            )
            == output
        )
