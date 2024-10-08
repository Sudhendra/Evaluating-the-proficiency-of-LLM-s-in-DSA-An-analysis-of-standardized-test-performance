import pytest
from q_0498_diagonalTraverse import Solution


@pytest.mark.parametrize(
    "mat, output",
    [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
    ],
)
class TestSolution:
    def test_findDiagonalOrder(self, mat: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.findDiagonalOrder(
                mat,
            )
            == output
        )
