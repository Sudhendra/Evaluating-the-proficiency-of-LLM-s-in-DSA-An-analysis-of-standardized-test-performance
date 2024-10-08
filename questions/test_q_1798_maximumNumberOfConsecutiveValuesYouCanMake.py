import pytest
from q_1798_maximumNumberOfConsecutiveValuesYouCanMake import Solution


@pytest.mark.parametrize(
    "coins, output", [([1, 3], 2), ([1, 1, 1, 4], 8), ([1, 4, 10, 3, 1], 20)]
)
class TestSolution:
    def test_getMaximumConsecutive(self, coins: List[int], output: int):
        sc = Solution()
        assert (
            sc.getMaximumConsecutive(
                coins,
            )
            == output
        )
