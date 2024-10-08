import pytest
from q_0778_swimInRisingWater import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        ([[0, 2], [1, 3]], 3),
        (
            [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ],
            16,
        ),
    ],
)
class TestSolution:
    def test_swimInWater(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.swimInWater(
                grid,
            )
            == output
        )
