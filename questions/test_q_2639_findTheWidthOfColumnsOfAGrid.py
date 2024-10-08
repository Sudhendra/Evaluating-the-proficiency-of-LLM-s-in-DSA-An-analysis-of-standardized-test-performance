import pytest
from q_2639_findTheWidthOfColumnsOfAGrid import Solution


@pytest.mark.parametrize(
    "grid, output",
    [([[1], [22], [333]], [3]), ([[-15, 1, 3], [15, 7, 12], [5, 6, -2]], [3, 1, 2])],
)
class TestSolution:
    def test_findColumnWidth(self, grid: List[List[int]], output: List[int]):
        sc = Solution()
        assert (
            sc.findColumnWidth(
                grid,
            )
            == output
        )
