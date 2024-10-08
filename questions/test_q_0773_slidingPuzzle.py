import pytest
from q_0773_slidingPuzzle import Solution


@pytest.mark.parametrize(
    "board, output",
    [
        ([[1, 2, 3], [4, 0, 5]], 1),
        ([[1, 2, 3], [5, 4, 0]], -1),
        ([[4, 1, 2], [5, 0, 3]], 5),
    ],
)
class TestSolution:
    def test_slidingPuzzle(self, board: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.slidingPuzzle(
                board,
            )
            == output
        )
