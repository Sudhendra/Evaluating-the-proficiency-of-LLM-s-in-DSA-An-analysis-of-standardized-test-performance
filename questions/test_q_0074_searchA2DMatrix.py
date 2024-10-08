import pytest
from q_0074_searchA2DMatrix import Solution


@pytest.mark.parametrize(
    "matrix, target, output",
    [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
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
