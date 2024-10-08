import pytest
from q_2507_smallestValueAfterReplacingWithSumOfPrimeFactors import Solution


@pytest.mark.parametrize("n, output", [(15, 5), (3, 3)])
class TestSolution:
    def test_smallestValue(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.smallestValue(
                n,
            )
            == output
        )
