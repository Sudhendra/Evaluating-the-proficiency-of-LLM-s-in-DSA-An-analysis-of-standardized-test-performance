import pytest
from q_0343_integerBreak import Solution


@pytest.mark.parametrize("n, output", [(2, 1), (10, 36)])
class TestSolution:
    def test_integerBreak(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.integerBreak(
                n,
            )
            == output
        )
