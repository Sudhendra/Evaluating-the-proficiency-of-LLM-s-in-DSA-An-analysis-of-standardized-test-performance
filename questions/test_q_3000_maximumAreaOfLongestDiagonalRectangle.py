import pytest
from q_3000_maximumAreaOfLongestDiagonalRectangle import Solution


@pytest.mark.parametrize(
    "dimensions, output", [([[9, 3], [8, 6]], 48), ([[3, 4], [4, 3]], 12)]
)
class TestSolution:
    def test_areaOfMaxDiagonal(self, dimensions: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.areaOfMaxDiagonal(
                dimensions,
            )
            == output
        )
