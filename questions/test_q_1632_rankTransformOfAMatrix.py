import pytest
from q_1632_rankTransformOfAMatrix import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [
        ([[1, 2], [3, 4]], [[1, 2], [2, 3]]),
        ([[7, 7], [7, 7]], [[1, 1], [1, 1]]),
        (
            [[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]],
            [[4, 2, 3], [1, 3, 4], [5, 1, 6], [1, 3, 4]],
        ),
    ],
)
class TestSolution:
    def test_matrixRankTransform(
        self, matrix: List[List[int]], output: List[List[int]]
    ):
        sc = Solution()
        assert (
            sc.matrixRankTransform(
                matrix,
            )
            == output
        )
