import pytest
from q_2485_findThePivotInteger import Solution


@pytest.mark.parametrize("n, output", [(8, 6), (1, 1), (4, -1)])
class TestSolution:
    def test_pivotInteger(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.pivotInteger(
                n,
            )
            == output
        )
