import pytest
from q_2596_checkKnightTourConfiguration import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        (
            [
                [0, 11, 16, 5, 20],
                [17, 4, 19, 10, 15],
                [12, 1, 8, 21, 6],
                [3, 18, 23, 14, 9],
                [24, 13, 2, 7, 22],
            ],
            True,
        ),
        ([[0, 3, 6], [5, 8, 1], [2, 7, 4]], False),
    ],
)
class TestSolution:
    def test_checkValidGrid(self, grid: List[List[int]], output: bool):
        sc = Solution()
        assert (
            sc.checkValidGrid(
                grid,
            )
            == output
        )
