import pytest
from q_0240_searchA2DMatrixIi import Solution


@pytest.mark.parametrize(
    "matrix, target, output",
    [
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            5,
            True,
        ),
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            20,
            False,
        ),
    ],
)
class TestSolution:
    def test_searchMatrix(self, matrix: List[List[int]], target: int, output: bool):
        sc = Solution()
        assert (
            sc.searchMatrix(
                matrix,
                target,
            )
            == output
        )
