import pytest
from q_1914_cyclicallyRotatingAGrid import Solution


@pytest.mark.parametrize(
    "grid, k, output",
    [
        ([[40, 10], [30, 20]], 1, [[10, 20], [40, 30]]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            2,
            [[3, 4, 8, 12], [2, 11, 10, 16], [1, 7, 6, 15], [5, 9, 13, 14]],
        ),
    ],
)
class TestSolution:
    def test_rotateGrid(self, grid: List[List[int]], k: int, output: List[List[int]]):
        sc = Solution()
        assert (
            sc.rotateGrid(
                grid,
                k,
            )
            == output
        )
