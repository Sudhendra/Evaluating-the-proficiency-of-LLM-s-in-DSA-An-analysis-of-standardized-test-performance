import pytest
from q_2894_divisibleAndNonDivisibleSumsDifference import Solution


@pytest.mark.parametrize("n, m, output", [(10, 3, 19), (5, 6, 15), (5, 1, -15)])
class TestSolution:
    def test_differenceOfSums(self, n: int, m: int, output: int):
        sc = Solution()
        assert (
            sc.differenceOfSums(
                n,
                m,
            )
            == output
        )
