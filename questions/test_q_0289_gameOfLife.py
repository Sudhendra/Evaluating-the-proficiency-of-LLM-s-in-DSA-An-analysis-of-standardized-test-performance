import pytest
from q_0289_gameOfLife import Solution


@pytest.mark.parametrize(
    "board, output",
    [
        (
            [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]],
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
        ),
        ([[1, 1], [1, 0]], [[1, 1], [1, 1]]),
    ],
)
class TestSolution:
    def test_gameOfLife(self, board: List[List[int]], output: None):
        sc = Solution()
        assert (
            sc.gameOfLife(
                board,
            )
            == output
        )
