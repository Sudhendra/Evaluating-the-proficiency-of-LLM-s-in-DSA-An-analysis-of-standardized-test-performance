import pytest
from q_0375_guessNumberHigherOrLowerIi import Solution


@pytest.mark.parametrize("n, output", [(10, 16), (1, 0), (2, 1)])
class TestSolution:
    def test_getMoneyAmount(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.getMoneyAmount(
                n,
            )
            == output
        )
