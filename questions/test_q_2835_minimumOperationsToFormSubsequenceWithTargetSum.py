import pytest
from q_2835_minimumOperationsToFormSubsequenceWithTargetSum import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    [([1, 2, 8], 7, 1), ([1, 32, 1, 2], 12, 2), ([1, 32, 1], 35, -1)],
)
class TestSolution:
    def test_minOperations(self, nums: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.minOperations(
                nums,
                target,
            )
            == output
        )
