import pytest
from q_1546_maximumNumberOfNonOverlappingSubarraysWithSumEqualsTarget import Solution


@pytest.mark.parametrize(
    "nums, target, output", [([1, 1, 1, 1, 1], 2, 2), ([-1, 3, 5, 1, 4, 2, -9], 6, 2)]
)
class TestSolution:
    def test_maxNonOverlapping(self, nums: List[int], target: int, output: int):
        sc = Solution()
        assert (
            sc.maxNonOverlapping(
                nums,
                target,
            )
            == output
        )
