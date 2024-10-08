import pytest
from q_0172_factorialTrailingZeroes import Solution


@pytest.mark.parametrize("n, output", [(3, 0), (5, 1), (0, 0)])
class TestSolution:
    def test_trailingZeroes(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.trailingZeroes(
                n,
            )
            == output
        )
