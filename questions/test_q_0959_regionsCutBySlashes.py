import pytest
from q_0959_regionsCutBySlashes import Solution


@pytest.mark.parametrize(
    "grid, output", [([" /", "/ "], 2), ([" /", "  "], 1), (["/\\", "\\/"], 5)]
)
class TestSolution:
    def test_regionsBySlashes(self, grid: List[str], output: int):
        sc = Solution()
        assert (
            sc.regionsBySlashes(
                grid,
            )
            == output
        )
