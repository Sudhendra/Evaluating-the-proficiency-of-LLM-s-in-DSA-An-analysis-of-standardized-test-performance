import pytest
from q_2931_maximumSpendingAfterBuyingItems import Solution


@pytest.mark.parametrize(
    "values, output",
    [
        ([[8, 5, 2], [6, 4, 1], [9, 7, 3]], 285),
        ([[10, 8, 6, 4, 2], [9, 7, 5, 3, 2]], 386),
    ],
)
class TestSolution:
    def test_maxSpending(self, values: List[List[int]], output: int):
        sc = Solution()
        assert (
            sc.maxSpending(
                values,
            )
            == output
        )
