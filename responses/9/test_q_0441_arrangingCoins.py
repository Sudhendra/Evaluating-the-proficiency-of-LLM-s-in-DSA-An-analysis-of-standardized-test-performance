import pytest
from q_0441_arrangingCoins import Solution


@pytest.mark.parametrize("n, output", [(5, 2), (8, 3)])
class TestSolution:
    def test_arrangeCoins(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.arrangeCoins(
                n,
            )
            == output
        )
