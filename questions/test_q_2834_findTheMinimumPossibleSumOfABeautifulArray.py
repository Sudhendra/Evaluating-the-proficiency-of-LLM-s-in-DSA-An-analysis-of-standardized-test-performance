import pytest
from q_2834_findTheMinimumPossibleSumOfABeautifulArray import Solution


@pytest.mark.parametrize("n, target, output", [(2, 3, 4), (3, 3, 8), (1, 1, 1)])
class TestSolution:
    def test_minimumPossibleSum(self, n: int, target: int, output: int):
        sc = Solution()
        assert (
            sc.minimumPossibleSum(
                n,
                target,
            )
            == output
        )
