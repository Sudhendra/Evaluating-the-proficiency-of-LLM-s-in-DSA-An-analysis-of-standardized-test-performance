import pytest
from q_2790_maximumNumberOfGroupsWithIncreasingLength import Solution


@pytest.mark.parametrize(
    "usageLimits, output", [([1, 2, 5], 3), ([2, 1, 2], 2), ([1, 1], 1)]
)
class TestSolution:
    def test_maxIncreasingGroups(self, usageLimits: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxIncreasingGroups(
                usageLimits,
            )
            == output
        )
