import pytest
from q_2335_minimumAmountOfTimeToFillCups import Solution


@pytest.mark.parametrize(
    "amount, output", [([1, 4, 2], 4), ([5, 4, 4], 7), ([5, 0, 0], 5)]
)
class TestSolution:
    def test_fillCups(self, amount: List[int], output: int):
        sc = Solution()
        assert (
            sc.fillCups(
                amount,
            )
            == output
        )
