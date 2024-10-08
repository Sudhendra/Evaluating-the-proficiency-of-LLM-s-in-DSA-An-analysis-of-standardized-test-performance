import pytest
from q_2056_numberOfValidMoveCombinationsOnChessboard import Solution


@pytest.mark.parametrize(
    "pieces, positions, output",
    [(["rook"], [[1, 1]], 15), (["queen"], [[1, 1]], 22), (["bishop"], [[4, 3]], 12)],
)
class TestSolution:
    def test_countCombinations(
        self, pieces: List[str], positions: List[List[int]], output: int
    ):
        sc = Solution()
        assert (
            sc.countCombinations(
                pieces,
                positions,
            )
            == output
        )
