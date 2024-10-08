import pytest
from q_1463_cherryPickupIi import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]], 24),
        (
            [
                [1, 0, 0, 0, 0, 0, 1],
                [2, 0, 0, 0, 0, 3, 0],
                [2, 0, 9, 0, 0, 0, 0],
                [0, 3, 0, 5, 4, 0, 0],
                [1, 0, 2, 3, 0, 0, 6],
            ],
            28,
        ),
    ],
)
class TestSolution:
    def test_cherryPickup(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.cherryPickup(
                grid,
            )
            == output
        )
