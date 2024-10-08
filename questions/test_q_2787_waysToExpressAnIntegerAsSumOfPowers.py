import pytest
from q_2787_waysToExpressAnIntegerAsSumOfPowers import Solution


@pytest.mark.parametrize("n, x, output", [(10, 2, 1), (4, 1, 2)])
class TestSolution:
    def test_numberOfWays(self, n: int, x: int, output: int):
        sc = Solution()
        assert (
            sc.numberOfWays(
                n,
                x,
            )
            == output
        )
