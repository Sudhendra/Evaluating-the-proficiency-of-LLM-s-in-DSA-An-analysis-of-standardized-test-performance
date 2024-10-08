import pytest
from q_2549_countDistinctNumbersOnBoard import Solution


@pytest.mark.parametrize("n, output", [(5, 4), (3, 2)])
class TestSolution:
    def test_distinctIntegers(self, n: int, output: int):
        sc = Solution()
        assert (
            sc.distinctIntegers(
                n,
            )
            == output
        )
