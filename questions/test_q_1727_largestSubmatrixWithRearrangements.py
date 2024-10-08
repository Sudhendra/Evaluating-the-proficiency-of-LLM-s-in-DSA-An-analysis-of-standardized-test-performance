import pytest
from q_1727_largestSubmatrixWithRearrangements import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [
        ([[0, 0, 1], [1, 1, 1], [1, 0, 1]], 4),
        ([[1, 0, 1, 0, 1]], 3),
        ([[1, 1, 0], [1, 0, 1]], 2),
    ],
)
class TestSolution:
    def test_largestSubmatrix(self, matrix: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.largestSubmatrix(
                matrix,
            )
            == output
        )
