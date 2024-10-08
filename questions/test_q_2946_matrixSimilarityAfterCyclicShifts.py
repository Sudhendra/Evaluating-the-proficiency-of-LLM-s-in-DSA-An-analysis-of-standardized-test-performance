import pytest
from q_2946_matrixSimilarityAfterCyclicShifts import Solution


@pytest.mark.parametrize(
    "mat, k, output",
    [
        ([[1, 2, 1, 2], [5, 5, 5, 5], [6, 3, 6, 3]], 2, True),
        ([[2, 2], [2, 2]], 3, True),
        ([[1, 2]], 1, False),
    ],
)
class TestSolution:
    def test_areSimilar(self, mat: List[List[int]], k: int, output: bool):
        sc = Solution()
        assert (
            sc.areSimilar(
                mat,
                k,
            )
            == output
        )
