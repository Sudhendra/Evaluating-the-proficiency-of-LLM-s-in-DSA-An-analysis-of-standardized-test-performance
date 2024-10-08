import pytest
from q_1823_findTheWinnerOfTheCircularGame import Solution


@pytest.mark.parametrize("n, k, output", [(5, 2, 3), (6, 5, 1)])
class TestSolution:
    def test_findTheWinner(self, n: int, k: int, output: int):
        sc = Solution()
        assert (
            sc.findTheWinner(
                n,
                k,
            )
            == output
        )
