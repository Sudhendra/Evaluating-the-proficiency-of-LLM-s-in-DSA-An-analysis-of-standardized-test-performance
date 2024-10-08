import pytest
from q_1931_paintingAGridWithThreeDifferentColors import Solution


@pytest.mark.parametrize("m, n, output", [(1, 1, 3), (1, 2, 6), (5, 5, 580986)])
class TestSolution:
    def test_colorTheGrid(self, m: int, n: int, output: int):
        sc = Solution()
        assert (
            sc.colorTheGrid(
                m,
                n,
            )
            == output
        )
