import pytest
from q_0931_minimumFallingPathSum import Solution


@pytest.mark.parametrize(
    "matrix, output",
    [([[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13), ([[-19, 57], [-40, -5]], -59)],
)
class TestSolution:
    def test_minFallingPathSum(self, matrix: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.minFallingPathSum(
                matrix,
            )
            == output
        )
