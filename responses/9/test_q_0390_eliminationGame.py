import pytest
from q_0390_eliminationGame import Solution


@pytest.mark.parametrize("n, output", [(9, 6), (1, 1)])
class TestSolution:
    def test_lastRemaining(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.lastRemaining(
                n,
            )
            == output
        )
