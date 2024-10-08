import pytest
from q_0313_superUglyNumber import Solution


@pytest.mark.parametrize(
    "n, primes, output", [(12, [2, 7, 13, 19], 32), (1, [2, 3, 5], 1)]
)
class TestSolution:
    def test_nthSuperUglyNumber(self, n: int, primes: List[int], output: int):
        sc = Solution()
        assert (
            sc.nthSuperUglyNumber(
                n,
                primes,
            )
            == output
        )
