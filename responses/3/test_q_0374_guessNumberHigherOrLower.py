import pytest
from q_0374_guessNumberHigherOrLower import Solution


@pytest.mark.parametrize("n, pick, output", [(10, 6, 6), (1, 1, 1), (2, 1, 1)])
class TestSolution:
    def test_guessNumber(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.guessNumber(
                n,
                pick,
            )
            == output
        )
