import pytest
from q_0509_fibonacciNumber import Solution


@pytest.mark.parametrize("n, output", [(2, 1), (3, 2), (4, 3)])
class TestSolution:
    def test_fib(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.fib(
                n,
            )
            == output
        )
