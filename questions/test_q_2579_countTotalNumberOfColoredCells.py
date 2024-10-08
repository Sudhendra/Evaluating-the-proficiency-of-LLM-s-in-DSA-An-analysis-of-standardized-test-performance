import pytest
from q_2579_countTotalNumberOfColoredCells import Solution


@pytest.mark.parametrize("n, output", [(1, 1), (2, 5)])
class TestSolution:
    def test_coloredCells(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.coloredCells(
                n,
            )
            == output
        )
