import pytest
from q_1815_maximumNumberOfGroupsGettingFreshDonuts import Solution


@pytest.mark.parametrize(
    "batchSize, groups, output",
    [(3, [1, 2, 3, 4, 5, 6], 4), (4, [1, 3, 2, 5, 2, 2, 1, 6], 4)],
)
class TestSolution:
    def test_maxHappyGroups(self, batchSize: int, groups: List[int], output: int):
        sc = Solution()
        assert (
            sc.maxHappyGroups(
                batchSize,
                groups,
            )
            == output
        )
