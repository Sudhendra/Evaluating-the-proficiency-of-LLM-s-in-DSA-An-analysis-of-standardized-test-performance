import pytest
from q_2048_nextGreaterNumericallyBalancedNumber import Solution


@pytest.mark.parametrize("n, output", [(1, 22), (1000, 1333), (3000, 3133)])
class TestSolution:
    def test_nextBeautifulNumber(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.nextBeautifulNumber(
                n,
            )
            == output
        )
