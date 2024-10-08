import pytest
from q_1808_maximizeNumberOfNiceDivisors import Solution


@pytest.mark.parametrize("primeFactors, output", [(5, 6), (8, 18)])
class TestSolution:
    def test_maxNiceDivisors(self, primeFactors: int, output: int):
        sc = Solution()
        assert (
            sc.maxNiceDivisors(
                primeFactors,
            )
            == output
        )
