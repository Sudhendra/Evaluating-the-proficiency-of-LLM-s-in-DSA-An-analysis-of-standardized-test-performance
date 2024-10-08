import pytest
from q_3070_countSubmatricesWithTopLeftElementAndSumLessThanK import Solution


@pytest.mark.parametrize(
    "grid, k, output",
    [([[7, 6, 3], [6, 6, 1]], 18, 4), ([[7, 2, 9], [1, 5, 0], [2, 6, 6]], 20, 6)],
)
class TestSolution:
    def test_countSubmatrices(self, grid: List[List[int]], k: int, output: int):
        sc = Solution()
        assert (
            sc.countSubmatrices(
                grid,
                k,
            )
            == output
        )
