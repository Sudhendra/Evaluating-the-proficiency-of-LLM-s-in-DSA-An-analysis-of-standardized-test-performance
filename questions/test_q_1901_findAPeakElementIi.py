import pytest
from q_1901_findAPeakElementIi import Solution


@pytest.mark.parametrize(
    "mat, output",
    [([[1, 4], [3, 2]], [0, 1]), ([[10, 20, 15], [21, 30, 14], [7, 16, 32]], [1, 1])],
)
class TestSolution:
    def test_findPeakGrid(self, mat: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.findPeakGrid(
                mat,
            )
            == output
        )
