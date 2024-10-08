import pytest
from q_1878_getBiggestThreeRhombusSumsInAGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [
        (
            [
                [3, 4, 5, 1, 3],
                [3, 3, 4, 2, 3],
                [20, 30, 200, 40, 10],
                [1, 5, 5, 4, 1],
                [4, 3, 2, 2, 5],
            ],
            [228, 216, 211],
        ),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [20, 9, 8]),
        ([[7, 7, 7]], [7]),
    ],
)
class TestSolution:
    def test_getBiggestThree(self, grid: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.getBiggestThree(
                grid,
            )
            == output
        )
