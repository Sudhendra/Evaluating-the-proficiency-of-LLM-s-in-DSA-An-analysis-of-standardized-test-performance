import pytest
from q_1012_numbersWithRepeatedDigits import Solution


@pytest.mark.parametrize("n, output", [(20, 1), (100, 10), (1000, 262)])
class TestSolution:
    def test_numDupDigitsAtMostN(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.numDupDigitsAtMostN(
                n,
            )
            == output
        )
