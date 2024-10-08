import pytest
from q_2500_deleteGreatestValueInEachRow import Solution


@pytest.mark.parametrize("grid, output", [([[1, 2, 4], [3, 3, 1]], 8), ([[10]], 10)])
class TestSolution:
    def test_deleteGreatestValue(self, grid: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.deleteGreatestValue(
                grid,
            )
            == output
        )
