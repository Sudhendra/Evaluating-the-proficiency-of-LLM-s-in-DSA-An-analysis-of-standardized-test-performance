import pytest
from q_2025_maximumNumberOfWaysToPartitionAnArray import Solution


@pytest.mark.parametrize(
    "nums, k, output",
    [
        ([2, -1, 2], 3, 1),
        ([0, 0, 0], 1, 2),
        ([22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14], -33, 4),
    ],
)
class TestSolution:
    def test_waysToPartition(self, nums: List[int], k: int, output: int):
        sc = Solution()
        assert (
            sc.waysToPartition(
                nums,
                k,
            )
            == output
        )
