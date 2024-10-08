import pytest
from q_0909_snakesAndLadders import Solution


@pytest.mark.parametrize(
    "board, output",
    [
        (
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1],
            ],
            4,
        ),
        ([[-1, -1], [-1, 3]], 1),
    ],
)
class TestSolution:
    def test_snakesAndLadders(self, board: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.snakesAndLadders(
                board,
            )
            == output
        )
