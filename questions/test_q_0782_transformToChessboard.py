import pytest
from q_0782_transformToChessboard import Solution


@pytest.mark.parametrize(
    "board, output",
    [
        ([[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]], 2),
        ([[0, 1], [1, 0]], 0),
        ([[1, 0], [1, 0]], -1),
    ],
)
class TestSolution:
    def test_movesToChessboard(self, board: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.movesToChessboard(
                board,
            )
            == output
        )
